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
--------------------------------------------------------------------------------
The problem can be transformed into:
    finding the MAXIMUM NUMBER OF OVERLAPPING INTERVALS, of a all the time.
This can be solved with methods:
    - BRUTE FORCE comparing O(n^2)
    - sort, MIN HEAP to keep track of intervals overlapping with each other.
  Intervals can be represented by finish time only.
    - COUNT AS SUM: maximum PREFIX SUM(similar to sweep line scanning)
    - sweep line scan(TODO:)

3. State machine - Maximum prefix sum - maximum OVERLAPPING INTERVALS

To find maximum overlapping interval, scan all the end times, and for each
end time, and check how many intervals have opened but not closed.

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
equivalent to maximum subarray here.

Complexity: O(NlogN)

This approached can be optimized to O(N) using BUCKETS to store
ordered interval ends.
Since open/close ends of all intervals are in finite space [min(s), max(e)],
we don't need a self-balancing tree to keep them ordered. Just put the values
in buckets of an array of size (max(e)-min(s) + 1).

Complexity: O(N)

4. Sweep line - overlapping intervals
Put start times and end times along with which job they belong to in to array.
Then scan the sorted array, when an interval opens add it to the active set of
intervals, and when it closes, we remove it.

Data structure:
    - list of (sᵢ, i), (eᵢ, i).
    - data structure to add & remove intervals efficiently, heap?

Complexity: O(NlogN)

5. Start time and end time alignment - overlapping intervals

Complexity: O(NlogN)

FOLLOW UP
================================================================================
What if [1, 2] and [2, 3] are considered overlapping?
In this case, sᵢ=p and eᵢ=p has different meaning for p: eᵢ=p<sᵢ=p.

- Then heap approach still works, only needing to modify heap pop condition(<).
- The prefix sum method loses information about whether p is start or end.
We need to modify the code to put eᵢ before sᵢ if there are equal!
- Align method: modify the condition(to <=) about when to increase number of overlapping
intervals.

 *
 */

#include <debug.hpp>
#include <queue>

class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        int result;
        //result = minMeetingRoomsGreedyNonoverlappingIntervalsWithHeap(intervals);
        //result = minMeetingRoomsOverlappingIntervalsMaxPrefixSum(intervals);
        //result = minMeetingRoomsOverlappingIntervalsWithHeap(intervals);
        //result = minMeetingRoomsOverlappingIntervalsAlign(intervals);
        result = minMeetingRoomsOverlappingIntervalsLineSweep(intervals);

        cout << "input: " << intervals << " => " << result << endl;

        return result;
    }

    /**
     * group non-overlapping intervals with heap
     */
    int minMeetingRoomsGreedyNonoverlappingIntervalsWithHeap(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](const vector<int> &a, const vector<int> &b){
                if (a[0] < b[0]) return true;
                else if (a[0] == b[0]) return (a[1] < b[1]);
                else return false;
                });
        priority_queue<int, vector<int>, std::greater<int>> heap; // min heap, containing number of rooms
        for (const vector<int> &interval: intervals) {
            if (!heap.empty() && heap.top() <= interval[0]) { // reuse room
                heap.pop();
            }
            heap.push(interval[1]); // update room, top element

            // another form
            //if (heap.empty() || heap.top() > interval[0]) heap.push(interval[1]);
            //else {
                //heap.pop();
                //heap.push(interval[1]);
            //}
        }

        return heap.size();
    }

    /**
     * Find maximum number of intervals overlapping with each other, with a heap.
     * Actually it's the same algorithm with above heap approach, which tries to
     * group non-overlapping intervals together.
     */
    int minMeetingRoomsOverlappingIntervalsWithHeap(vector<vector<int>> &intervals) {
        std::sort(intervals.begin(), intervals.end(),
                [](const vector<int> &a, const vector<int> &b){ return a[0] < b[0]; });
        int maxNumOverlapping = 0;
        priority_queue<int, vector<int>, std::greater<int>> heap;
        for (const vector<int> &interval: intervals) {
            while (!heap.empty() && heap.top() <= interval[0]) {
                heap.pop(); // a new interval opens
            }
            heap.push(interval[1]);
            maxNumOverlapping = max(maxNumOverlapping, (int)heap.size()); // heap size is number of current overlapping intervals
        }
        return maxNumOverlapping;
    }

    /**
     * Find maximum number of intervals overlapping with each other, with prefix sum(count as sum).
     */
    int minMeetingRoomsOverlappingIntervalsMaxPrefixSum(
            vector<vector<int>> &intervals) {
        map<int, int> timeToValue; // sorted pairs of <time, v>, where v in [-1, 1]
        for (vector<int> &interval: intervals) {
            timeToValue[interval[0]] += 1;
            timeToValue[interval[1]] -= 1; // XXX: how about (s₁, e), (e, e₂)?
        }
        int prefixSum = 0, maxPrefixSum = 0; //  prefix sum ending here, max prefix sum
        for (pair<const int, int> &item: timeToValue) {
            //prefixSum = max(item.second, item.second + prefixSum);
            prefixSum += item.second;
            maxPrefixSum = max(maxPrefixSum, prefixSum);
        }
        return maxPrefixSum;
    }

    /**
     * Line sweeping with aligning separate starts and ends points.
     */
    int minMeetingRoomsOverlappingIntervalsAlign(
            vector<vector<int>> &intervals) {
        vector<int> starts;
        vector<int> ends;
        for (int i = 0; i < (int)intervals.size(); ++i) {
            starts.push_back(intervals[i][0]);
            ends.push_back(intervals[i][1]);
        }

        sort(starts.begin(), starts.end());
        sort(ends.begin(), ends.end());

        //cout << starts << endl;
        //cout << ends << endl;

        int i = 0, j = 0;
        int currentOverlapping = 0, maxOverlapping = 0; // number of overlapping
        while (i < (int)intervals.size() && j < (int)intervals.size()) {
            if (starts[i] < ends[j]) {
                ++currentOverlapping;
                ++i;
            } else if (starts[i] > ends[j]){
                ++j;
                --currentOverlapping;
            }
            else {
                ++i; ++j;
            }

            maxOverlapping = std::max(maxOverlapping, currentOverlapping);
        }

        // XXX:
        currentOverlapping += std::max(0, (int)intervals.size() - i);
        currentOverlapping -= std::max(0, (int)intervals.size() - j);

        return maxOverlapping;
    }

    int minMeetingRoomsOverlappingIntervalsLineSweep(vector<vector<int>> &intervals) {
        int result = 0;
        vector<vector<int>> points; // line sweep points: (point, +-interval index)
        for (int i = 0; i < (int)intervals.size(); ++i) {
            points.push_back({intervals[i][0], +1, i});
            points.push_back({intervals[i][1], -1, i}); // XXX: same time, end time comes first
        }

        sort(points.begin(), points.end());
        multiset<int> tree; // ree
        for (auto p: points) {
            int flag = p[1], i = p[2];
            if (flag > 0) { // interval opens
                tree.insert(i);
                result = std::max(result, (int)tree.size());
            } else if (flag < 0) { // interval ends
                tree.erase(tree.find(i));
            }
        }

        return result;
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

    intervals = {{1, 2}, {1, 2}};
    result = 2;
    assert(solution.minMeetingRooms(intervals) == result);

    intervals = {{1, 2}, {2, 3}};
    result = 1; // XXX: 1 or 2?
    assert(solution.minMeetingRooms(intervals) == result);

    cout << "self test passed!" << endl;

    return 0;
}

int main(int argc, char *argv[])
{
    // TODO: submit
    test();
    return 0;
}
