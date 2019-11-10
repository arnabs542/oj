/**
432. All O`one Data Structure
Hard

Implement a data structure supporting the following operations:

Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
Challenge: Perform all these in O(1) time complexity.

Accepted 23.5K Submissions 76.2K

SOLUTION
================================================================================

1. Brute force
- map: <key, value>
Complexity:
Inc: O(1)
Dec: O(1)
GetMaxKey: O(n)
GetMinKey: O(n)

2. Separate chaining - bucket (linked list) - just like in LFU cache!

Similar problem to least frequently used cache, bucket separate chaining can
be used for keys with same value.
But the difference is, when value of a key is deleted, we need to find
second smallest value in O(1) time! In LFU, when an item is deleted, the new
smallest frequency is always 1, but not in this case.
This means that the first dimension data structure has to be ordered linked list.

Maintain two data structure:
- linked list: <frequency, list of a bucket>
- bucket(separate chaining): list or hash set that supports O(1) insert/delete

Optimize
--------
Data structure for bucket list can be implemented with hash set, then we don't
need to maintain the mapping from value to bucket.


*/

#include <debug.hpp>

class AllOne {
public:
    /** Initialize your data structure here. */
    AllOne() {

    }

    /** Inserts a new key <Key> with value 1. Or increments an existing key by 1. */
    virtual void inc(string key) {

    }

    /** Decrements an existing key by 1. If Key's value is 1, remove it from the data structure. */
    virtual void dec(string key) {

    }

    /** Returns one of the keys with maximal value. */
    virtual string getMaxKey() {

    }

    /** Returns one of the keys with Minimal value. */
    virtual string getMinKey() {

    }
};


class AllOneSeparateChain: public AllOne {
public:
    /** Initialize your data structure here. */
    AllOneSeparateChain() {

    }

    /** Inserts a new key <Key> with value 1. Or increments an existing key by 1. */
    virtual void inc(string key) {
        pair<string, int> item {key, 1};
        list<Bucket>::iterator it;
        if (mKeyToItr.find(key) != mKeyToItr.end()) { // already exists
            item.second = mKeyToItr.at(key)->second;
            list<Bucket>::iterator it0 = mValueToBucket[item.second++];
            it = next(it0);
            it0->nodes.erase(mKeyToItr.at(key)); // remove from old list
            if (it0->nodes.empty()) {
                mBucketList.erase(it0); // delete empty bucket
                mValueToBucket.erase(item.second-1);
            }
        } else { it = mBucketList.begin(); }

        if (it == mBucketList.end() || (it->value != item.second)) { // found the bucket
            mValueToBucket[item.second] = it = mBucketList.insert(it, {item.second, {}}); // new bucket
        }
        mKeyToItr[key] = it->nodes.insert(it->nodes.end(), item); // update mapping
    }

    /** Decrements an existing key by 1. If Key's value is 1, remove it from the data structure. */
    virtual void dec(string key) {
        if (mKeyToItr.find(key) == mKeyToItr.end()) return;
        pair<string, int> item = *mKeyToItr[key];

        list<Bucket>::iterator it = mValueToBucket.at(item.second--);
        list<Bucket>::iterator it1 = prev(it);
        it->nodes.erase(mKeyToItr[key]); // remove from old list

        if (!item.second) {
            mKeyToItr.erase(key); //  remove 0 value
        } else {
            if (it1 == mBucketList.end() || it1->value != item.second) {
                it1 = mBucketList.insert(it, Bucket{item.second, {}}); // new bucket
            }
            mValueToBucket[item.second] = it1;
            mKeyToItr[key] = it1->nodes.insert(it1->nodes.end(), item);
        }

        if (it->nodes.empty()) {
            mValueToBucket.erase(it->value);
            mBucketList.erase(it); // delete bucket?
        }
    }

    /** Returns one of the keys with maximal value. */
    virtual string getMaxKey() {
        if (mBucketList.empty() || mBucketList.rbegin()->nodes.empty()) return "";
        return mBucketList.back().nodes.back().first;
    }

    /** Returns one of the keys with Minimal value. */
    virtual string getMinKey() {
        if (mBucketList.empty() || mBucketList.begin()->nodes.empty()) return "";
        cout <<  mBucketList.begin()->nodes.back().first << ", " << mBucketList.begin()->nodes.back().second << endl;
        return mBucketList.begin()->nodes.back().first;
    }

    typedef pair<string, int> DataType;
    struct Bucket {
        int value;
        list<DataType> nodes; // second dimension, keys with same value
    };
    list<Bucket> mBucketList; // first dimension, buckets
    unordered_map<int, list<Bucket>::iterator> mValueToBucket; // value to list
    unordered_map<string, list<DataType>::iterator> mKeyToItr; // key to iterator
};


/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne* obj = new AllOne();
 * obj->inc(key);
 * obj->dec(key);
 * string param_3 = obj->getMaxKey();
 * string param_4 = obj->getMinKey();
 */

vector<string> test(const vector<string> &ops, const vector<vector<string>> &args) {
    assert(ops.size() == args.size());
    vector<string> result;

    shared_ptr<AllOne> pObj = make_shared<AllOneSeparateChain>();
    for (size_t i = 1; i < ops.size(); ++i) {
        if (ops[i] == "getMaxKey") {
            result.push_back(pObj->getMaxKey());
        } else if (ops[i] == "getMinKey") {
            result.push_back(pObj->getMinKey());
        } else if (ops[i] == "inc") {
            pObj->inc(args[i][0]);
        } else if (ops[i] == "dec") {
            pObj->dec(args[i][0]);
        } else {
            cerr << "wrong method: " << ops[i] << endl;
            abort();
        }
    }

    cout << ops << endl
        << args << endl
        << result << endl;
    return result;
 }

 int main(int argc, char *argv[])
 {
    vector<string> ops;
    vector<vector<string>> args;
    vector<string> result;

    ops = {"AllOne", "getMaxKey", "getMinKey", "inc", "inc", "getMaxKey", "getMinKey", "dec", "dec", "getMaxKey"};
    args = {{},      {},          {}, {"a"}, {"a"},{},{},{"a"},{"a"},{}};
    result = {"", "", "a", "a", ""};
    assert(test(ops, args) == result);

    ops = {"AllOne", "inc", "inc", "inc", "getMinKey", "dec", "getMinKey"};
    args = {{},      {"a"}, {"a"}, {"b"}, {"b"},      {"b"},    {}};
    result = {"b", "a"};
    assert(test(ops, args) == result);

    ops = {"AllOne","inc","inc","getMaxKey","getMinKey","inc","getMaxKey","getMinKey"};
    args = {{},{"hello"},{"hello"},{},{},{"leet"},{},{}};
    //result = {null,null,null,"hello","hello",null,"hello","leet"};
    result = {"hello","hello","hello","leet"};
    assert(test(ops, args) == result);

    ops = {"AllOne","inc","inc","inc", "inc", "dec","getMaxKey","getMinKey"};
    args = {{},{"hello"},{"hello"},{"world"},{"world"},{"world"}, {}, {}};
    result = {"hello","world"};
    assert(test(ops, args) == result);

    ops = {"AllOne","inc","inc","inc","inc","inc","dec","getMaxKey","getMinKey","inc","inc","inc","getMaxKey","getMinKey","inc","inc","getMinKey"};
    args = {{},{"hello"},{"hello"},{"world"},{"world"},{"hello"},{"world"},{},{},{"world"},{"world"},{"leet"},{},{},{"leet"},{"leet"},{}};
    result = {"hello","world","world","leet","leet"};
    //result = {"hello","world","world","leet","world"}; // or this answer
    assert(test(ops, args) == result);

    cout << "self test passed!" << endl;

     return 0;
 }
