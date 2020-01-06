/**
 *
460. LFU Cache
Hard

Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Note that the number of times an item is used is the number of calls to the get and put functions for that item since it was inserted. This number is set to zero when the item is removed.



Follow up:
Could you do both operations in O(1) time complexity?



Example:

LFUCache cache = new LFUCache( 2  );// capacity

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4


SOLUTION
================================================================================

1. Brute force - hash table & self balancing tree
Use a map to store (key, value) pairs, for query and insert in O(1).
To maintain the frequency each item is used, use another frequency counter.
The frequency can be maintained with self balancing tree, such as c++ multi_map.
Then the idea is to maintain two data structure:
1. Self balancing tree for frequency: (frequency, (key, value)). Sorted in
ascending order of frequency, since items with duplicate frequency is appended.
2. Hash table: (key, node in tree).

Complexity:
put: O(logN)
get: O(logN)

2. Hash table with min-heap
A min-heap can be used to keep track of least frequency.
Use two data structures:
- min heap: <frequency>
- hash table: <key, <position, frequency index>>

Complexity:
put: O(logN)
get: O(logN)

3. Separate chaining - bucket duplicate items - hash table with nested linked list

The difficulty is to maintain ordered frequency list. And the core idea is:
    CHANGE BY ONE property: frequency is changed by 1 every time accessed!
So every time we need to update the frequency data structure, we only
need to move data to adjacent position.

(Brainstorm)Data structures supports constant time insert/delete:
- LINKED LIST
- Hash table

But the problem is there are items with DUPLICATE frequency.
Group items with same frequency together in a linked list BUCKET!
The whole idea is like SEPARATE CHAINING for hash table collision resolution!

Then the state transition is much simpler, without need for balanced tree for
general insert/update of O(logN).

Maintain such two data structure:
--------------------------------
1. Hash table: <key, node(value, ...)>
2. Linked list containing nested sorted linked list: <frequency, LinkedList<key, value>>
   Each node represents frequency, a linked list of nodes(key, value).
   And the linked list of nodes can implement the least recently used cache.

"frequency"    "separate chained (key, value) nodes"
1: x -> y
2: z -> a
5: b
9: c

After hit x,
1: y
2: z -> a -> x
5: b
9: c

And also, hash table can be used to contain the nested linked list, since remove key freq
and insert key freq+1 both take O(1) time complexity.

- Get value by key is O(1) supported by hash table.
- And accessing an existing key requires incrementing its frequency, and update the minimal
frequency.
- The state change of minimal frequency is not subtle, actually:
    - access hit: min_frequency = min_frequency if (linkedList of min_frequency is empty)
      else min_frequency+1
    - access no hit: min_frequency = 1
    - access not hit and need to evict: remove lru item of min_frequency, and min_frequency = 1


Reference: http://dhruvbird.com/lfu.pdf

Complexity:
put: O(1)
get: O(1)


 *
 */

#include <debug.hpp>
#include <list>

class LFUCache {
public:
    LFUCache(int capacity) {

    }

    virtual int get(int key) {

    }

    virtual void put(int key, int value) {

    }

    virtual ~LFUCache() {};
};

class LFUCacheSeparateChain: public LFUCache {
public:
    LFUCacheSeparateChain(int capacity): LFUCache(capacity) {
        mCapacity = capacity;
    }

    int get(int key) {
        if (mKeyToItr.find(key) == mKeyToItr.end()) {
            return -1;
        }

        const int &value = incrementFrequency(key);
        return value;
    }

    inline int incrementFrequency(int key) {
        DataNode *pNode = *mKeyToItr.at(key);
        int &freq = pNode->freq;
        int &value = pNode->value;

        mFreqToList.at(freq).erase(mKeyToItr.at(key)); // remove from old list
        mFreqToList[++freq].push_back(pNode); // frequency+1, append to adjacent list
        mKeyToItr[key] = --mFreqToList[freq].end(); // update key to list iterator

        if (mFreqToList[mMinFreq].empty()) {
            ++mMinFreq; // update min frequency. TODO: trim map size?
        }

        return value;
    }

    void put(int key, int value) {
        if (mCapacity <= 0) return; // capacity = 0
        if (mKeyToItr.find(key) != mKeyToItr.end()) {
            (*mKeyToItr[key])->value = value;
            incrementFrequency(key); // hit! key value already exists, increment only
            return;
        } else {
            // edge case: capacity 0
            // evict, reaches capacity limit
            if ((int)mKeyToItr.size() >= mCapacity && !mFreqToList[mMinFreq].empty()) {
                DataNode *pNode = mFreqToList[mMinFreq].front(); // pop from list
                mFreqToList[mMinFreq].pop_front();
                mKeyToItr.erase(pNode->key); // remove from map
                delete pNode;
            }
            DataNode *pNode = new DataNode();
            pNode->key = key;
            pNode->value = value;
            pNode->freq = mMinFreq = 1; // update frequency

            mFreqToList[1].push_back(pNode); // insert key, value
            mKeyToItr[key] = --mFreqToList[1].end(); // [BUG] miswritten 1 as key.
        }
    }

public:
    struct DataNode {
        int key;
        int value;
        int freq = 0;
    };

    int mCapacity = 0;

    unordered_map<int, list<DataNode*>> mFreqToList; //<freq, list<node>>
    unordered_map<int, list<DataNode*>::iterator> mKeyToItr; // <key, iterator>
    int mMinFreq = 0;

};

vector<int> test(const vector<string> &ops, const vector<vector<int>> &nums)
{
    vector<int> result;
    assert(nums.size() == ops.size());
    if (nums.size() == 0) return result;

    int capacity = nums[0][0];

    LFUCache *obj = new LFUCacheSeparateChain(capacity);

    for (size_t i = 1; i < ops.size(); ++i)
    {
        if (ops[i] == "put")  {
            obj->put(nums[i][0], nums[i][1]);
        } else if (ops[i] == "get") {
            result.push_back(obj->get(nums[i][0]));
        }
    }
    cout << ops << endl
        << nums << endl
        << result << endl;
    delete obj;
    return result;
}

int main(int argc, char *argv[])
{

    vector<string> ops;
    vector<vector<int>> nums;
    vector<int> values;

    ops = {"LFUCache", "put", "get"};
    nums = {{0}, {1,1},{1}};
    values = {-1};
    assert(test(ops, nums) == values);

    ops = {"LFUCache", "put", "get", "put", "get", "put", "get", "get"};
    nums = {{1},       {1,1},  {1},  {1, 2}, {1},  {2, 2}, {1},  {2}};
    values = {1, 2, -1, 2};
    assert(test(ops, nums) == values);

    ops = {"LFUCache","put","put","get","put","get","get","put","get","get","get"};
    nums = {{2},      {1,1},{2,2},{1},  {3,3},{2},  {3},  {4,4},{1},  {3},  {4}};
    values = {1, -1, 3, -1, 3, 4};
    assert(test(ops, nums) == values);

    ops = {"LFUCache","put","put","get","get","get","put","get", "get"};
    nums = {{2},      {1,1},{2,2},{2},  {2},  {1},  {3,3},{1},{3}};
    values = {2, 2, 1, -1, 3};
    assert(test(ops, nums) == values);

    cout << "self test passed" << endl;

    return 0;
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
