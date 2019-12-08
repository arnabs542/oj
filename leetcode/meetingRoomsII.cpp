/**
 *
253. Meeting Rooms II

Hard

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1

SOLUTION
================================================================================

1. Brute force - dynamic programming - group non-overlapping intervals
First sort the intervals with key=(end time, start time).
For each interval, we have multiple choices with respect to which existing room
to reuse, thus we can keep track of vector<vector<int>> list of rooms set, and
choose the scheme of smallest list size.

#Define state: f[i] = list of rooms ending here={e1, e2, ..., em}.
Define state: f[i] list of rooms set, ending here(interval i is last).
State transition:
    f[i] = min(f[j])

2. Greedy with heap of latest finish time - group NON-OVERLAPPING INTERVALS

For this INTERVAL SCHEDULING problem, we can apply GREEDY strategy to group
non-overlapping intervals: prefer rooms that's released earliest to reuse.

TODO: how to prove the greedy strategy?

1) Sort intervals
2) Maintain a min heap of rooms. Use a MIN HEAP, each element indicates a
room, represented with latest FINISH TIME of intervals in this room.
3) Scan the intervals. For each interval(sᵢ,eᵢ), check whether it's possible to
reuse the HEAP TOP room, which finishes earliest. If not, push a new room eᵢ
into the heap.

Why using a heap? Because heap data structure provides O(logN) complexity for
updating/querying minimum element, naturally fit for greedy strategy!

Complexity: O(NlogN)


In ANOTHER PERSPECTIVE, we can exploit the overlapping intervals state transition.
The problem can be transformed into:
    finding the MAXIMUM NUMBER OF OVERLAPPING INTERVALS, of a all the time.
This can be solved with methods:
    - brute force comparing O(n^2)
    - sweeping line (TODO:)
    - maximum prefix sum

3. State machine - Maximum prefix sum - maximum OVERLAPPING INTERVALS
The start and end of an interval can be represent with +1 and -1.
With +1, it means an interval started, and with -1, it means an interval ended.

To scan the time horizon, it takes too much time.
But if the start and end timestamps of intervals are sorted, this problem can be
viewed as MAXIMUM PREFIX SUM problem.

When an interval opens, we add 1, and when it closes, we subtract 1 from the
prefix sum. Thus the prefix sum indicates how many intervals open right now.

[[1, 2]]
[s1, e2]
[1, -1] => 1

[[7, 10], [2, 4]]
[s2, e4, s7, e10]
[1,  -1, 1,  -1] => max prefix sum is 1

[[0, 30], [5, 10], [15, 20]]
[s0, s5, e10, s15, e20, e30]
[1,  1,   -1,  1,   -1, -1] => max prefix sum is 2

Since the prefix sum is always larger or equal to 0, so maximum prefix sum is
equivalent to maximum prefix sum.

Complexity: O(NlogN)

4. Sweep line - overlapping intervals
Put start times and end times along with which job they belong to in to array.
Then scan the sorted array, when an interval opens add it to the active set of
intervals, and when it closes, we remove it.

Data structure:
    - list of (sᵢ, i), (eᵢ, i).
    - data structure to add & remove intervals efficiently, heap?

 *
 */

#include <debug.hpp>
#include <queue>

class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        int result;
        //result = minMeetingRoomsGreedyWithHeap(intervals);
        result = minMeetingRoomsOverlappingIntervalsMaxPrefixSum(intervals);
        return result;
    }

    int minMeetingRoomsGreedyWithHeap(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](const vector<int> &a, const vector<int> &b){
                if (a[0] < b[0]) return true;
                else if (a[0] == b[0]) return (a[1] < b[1]);
                else return false;
                });
        priority_queue<int, vector<int>, std::greater<int>> heap; // min heap
        for (const vector<int> &interval: intervals) {
            if (!heap.empty() && heap.top() <= interval[0]) { // reuse room
                heap.pop();
            }
            heap.push(interval[1]); // update room, top element

            //continue;
            //
            //if (heap.empty() || heap.top() > interval[0]) heap.push(interval[1]);
            //else {
                //heap.pop();
                //heap.push(interval[1]);
            //}
        }

        return heap.size();
    }

    int minMeetingRoomsOverlappingIntervalsMaxPrefixSum(
            vector<vector<int>> &intervals) {
        map<int, int> timeToValue; // sorted pairs of <time, v>, where v in [-1, 1]
        for (vector<int> &interval: intervals) {
            timeToValue[interval[0]] += 1;
            timeToValue[interval[1]] -= 1;
        }
        int maxPrefixSum = 0; // max prefix sum
        int prefixSum = 0; // prefix sum ending here
        for (pair<const int, int> &item: timeToValue) {
            //prefixSum = max(item.second, item.second + prefixSum);
            prefixSum += item.second;
            maxPrefixSum = max(maxPrefixSum, prefixSum);
        }
        return maxPrefixSum;
    }

};

int test() {
    Solution solution;
    vector<vector<int>> intervals;
    int result;

    intervals = {};
    result = 0;
    assert(solution.minMeetingRooms(intervals) == result);

    intervals = {{1, 10}};
    result = 1;
    assert(solution.minMeetingRooms(intervals) == result);

    intervals = {{7, 10}, {2, 4}};
    result = 1;
    assert(solution.minMeetingRooms(intervals) == result);

    intervals = {{0, 30}, {5, 10}, {15, 20}};
    result = 2;
    assert(solution.minMeetingRooms(intervals) == result);

    cout << "self test passed!" << endl;

    return 0;
}

int main(int argc, char *argv[])
{
    test();
    return 0;
}
