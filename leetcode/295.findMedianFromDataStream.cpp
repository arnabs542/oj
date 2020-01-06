/**
 *

295. Find Median from Data Stream

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

    void addNum(int num) - Add a integer number from the data stream to the data structure.
    double findMedian() - Return the median of all elements so far.

For example:

    addNum(1)
    addNum(2)
    findMedian() -> 1.5
    addNum(3)
    findMedian() -> 2

Credits:
Special thanks to @Louis1992 for adding this problem and creating all test cases.

==============================================================================================
SOLUTION

1. Brute force SORT
For each new element, sort the data list, and find the median.

Complexity: O(NlogN) for sorting, O(1) for finding median.

2. Maintain the sorted data list

So we don't have to sort from scratch every time.
For each new element, insert the new element into the sorted data structure. And find the
median.

To maintain a sorted data list, there are two data structure: binary search tree, a list.

Insertion sorting list:
find where to insert with binary search: O(logN)
insert: O(N)
O(logN) + O(N) = O(N)

Balanced Binary search tree has
    search: log(N)
    insert: log(N)
    delete: log(N)

Complexity: O(logN) for sorting, O(N/2) finding the median.

3. Heaps

Heaps are naturally good fit for ORDER STATISTICS problem.

Two heaps, separating the data into two non-overlapping segments: top half, and bottom half

To find the median, we need to find the middle element(s).
There are at most two middle elements. Each one of them is a lower bound or upper bound
of half of the data list.
The middle element or elements separate the data into two non-overlapping intervals:
subset with smaller elements and subset with larger elements.

This illustrates DIVIDE AND CONQUER idea. And we want to separate the data list into TOP HALF
and BOTTOM HALF.

Lower bound or upper bound means minimal and maximal value, which indicates that we
can make use of HEAP data structure to maintain such property.

Thus, we can maintain two heaps:
A min heap containing larger half elements. (keeping top half of data)
A max heap containing smaller half elements. (keeping bottom half of data)

For each new element, there are several operations:
- add new element into the larger heap if it's larger than(or equal to) the min heap top
- add new element into the larger heap if it's less than the max heap top
- move one heap top to another heap, and push the new element.

----------------------------------------------------------------------------------------------
Complexity
Add element to heap: O(logN)
pop top of heap: O(logN)
get top: O(1)

Complexity: O(logN), O(N)

4. Balanced binary search tree with iterator POINTER
C++ multiset is implemented with balanced binary search tree, and enables iterating over the
container.

Thus, keep track of the median pointer.
C++ multiset always insert element at the last position of same value.

Insert: log(N)
Update median pointer: amortized O(1)

*/

#include <debug.hpp>


class MedianFinder {
public:
    /** initialize your data structure here. */
    MedianFinder() {

    }

    virtual void addNum(int num) {
        cout << "addNum, NOT IMPLEMENTED!" << endl;
    }

    virtual double findMedian() {
        cout << "findMedian, NOT IMPLEMENTED!" << endl;
        return 0;
    }
};

class Comparator {
    bool m_reverse;
    public:
    Comparator(bool reverse) {
        m_reverse = reverse;
    }
    bool operator () (const int &lhs, const int &rhs) {
        return m_reverse ? lhs > rhs : lhs < rhs;
    }
};

typedef priority_queue<int, vector<int>, Comparator> pq;

class MedianFinderHeaps: public MedianFinder {
public:
    pq m_minheap;
    pq m_maxheap;

    MedianFinderHeaps(): MedianFinder(), m_minheap(pq(Comparator(true))), m_maxheap(pq(Comparator(false))) {
        //m_minheap = pq(Comparator(true));
        //m_maxheap = pq(Comparator(false));
    }

    void addNum(int num) {
        pq *sourceQ = NULL, *targetQ = NULL;
        if (m_minheap.empty() || m_minheap.top() <= num) {
            sourceQ = &m_minheap;
            targetQ = &m_maxheap;
        } else {
            sourceQ = &m_maxheap;
            targetQ = &m_minheap;
        }
        sourceQ->push(num); // push first to make sure no overlapping
        if (int(sourceQ->size() - targetQ->size()) >= 2) {
            // move top of sourceQ to targetQ
            int n = sourceQ->top(); sourceQ->pop();
            targetQ->push(n);
        }
    }

    double findMedian() {
        if (m_minheap.size() > m_maxheap.size()) {
            return m_minheap.top();
        } else if (m_minheap.size() == m_maxheap.size()) {
            return m_minheap.size() ? 0.5 * (m_minheap.top() + m_maxheap.top()) : 0;
        } else {
            return m_maxheap.top();
        }
    }
};

class MedianFinderTree: public MedianFinder {
public:
    multiset<int> m_data;
    multiset<int>::iterator m_median; // points to the median or lower median

    MedianFinderTree(): m_median() {
    }

    void addNum(int num) {
        int n = m_data.size();
        m_data.insert(num);
        //cout << "data size: " << m_data.size() << endl;
        if (!n) {
            m_median = m_data.begin();
        } else if ((*m_median) > num) {
            if (n & 1) --m_median; // inserted before pointer
        } else if (!(n & 1)) {
            ++m_median; // inserted after m_median pointer
        }
    }

    double findMedian() {
        if (!m_data.size()) { return 0; }
        else if (m_data.size() & 1) { return *m_median; }
        else { return 0.5 * (*m_median + *next(m_median, 1)); }
    }

};

void test() {

    //typedef MedianFinderHeaps MedianFinderSolution;
    typedef MedianFinderTree MedianFinderSolution;

    shared_ptr<MedianFinder> finder;
    finder = make_shared<MedianFinderSolution>();
    //finder = MedianFinderTree();

    assert(finder->findMedian() == 0);
    finder->addNum(1);
    assert(finder->findMedian() == 1);
    finder->addNum(2);
    assert(finder->findMedian() == 1.5);
    finder->addNum(3);
    assert (finder->findMedian() == 2);

    finder = make_shared<MedianFinderSolution>();
    finder->addNum(4);
    finder->addNum(3);
    finder->addNum(2);
    assert (finder->findMedian() == 3);
    finder->addNum(9);
    assert(finder->findMedian() == 3.5);
    finder->addNum(9);
    assert(finder->findMedian() == 4);

    finder = make_shared<MedianFinderSolution>();

    for (auto i: vector<int>({12, 4, 5, 3, 8, 7})) {
        finder->addNum(i);
    }
    assert(finder->findMedian() == 6.0);

    finder = make_shared<MedianFinderSolution>();
    finder->addNum(1);
    finder->addNum(1);
    finder->addNum(1);
    finder->addNum(1);
    assert(finder->findMedian() == 1);

    vector<int> input = {40,12,16,14,35,19,34,35,28,35,26,6,8,2,14,25,25,4,33,18,10,14,27,3,35,13,24,27,14,5,0,38,19,25,11,14,31,30,11,31,0};
    vector<double> output = {40.00000, 26.00000, 16.00000, 15.00000, 16.00000, 17.50000, 19.00000, 26.50000, 28.00000, 31.00000, 28.00000, 27.00000, 26.00000, 22.50000, 19.00000, 22.00000, 25.00000, 22.00000, 25.00000, 22.00000, 19.00000, 18.50000, 19.00000, 18.50000, 19.00000, 18.50000, 19.00000, 21.50000, 19.00000, 18.50000, 18.00000, 18.50000, 19.00000, 19.00000, 19.00000, 18.50000, 19.00000, 19.00000, 19.00000, 19.00000, 19.00000};
    vector<double> result;

    finder = make_shared<MedianFinderSolution>();
    for (int a: input) {
        finder->addNum(a);
        result.push_back(finder->findMedian());
        //cout << finder->m_minheap << endl;
    }
    //std::cout.unsetf ( std::ios::floatfield );                // floatfield not set
    cout.setf(ios::fixed);
    cout.precision(5);
    cout << output.size() << endl;
    cout << result.size() << endl;
    cout << result << endl;
    assert(result == output);

    cout << "self test passed!" << endl;

}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */

int main(int argc, char *argv[])
{
    test();
    return 0;
}
