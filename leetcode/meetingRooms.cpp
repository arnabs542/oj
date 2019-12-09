/**
 *
252.Meeting Rooms
Easy

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true

SOLUTION
================================================================================
Interval scheduling problem.

1. Brute force compare every pair

Complexity: O(N^2)

2. Sort and check overlapping

Complexity: O(NlogN)

 *
 */

#include <debug.hpp>

class Solution {
public:
    bool canAttendMeetings(vector<vector<int>> &intervals) {
        bool result = canAttendMeetingsSort(intervals);

        return result;
    }

    bool canAttendMeetingsSort(vector<vector<int>> &intervals) {
        std::sort(intervals.begin(), intervals.end(),
                [](const vector<int> &a, const vector<int> &b) {
                    return a[0] <= b[0];
                });
        for (int i = 1; i < (int)intervals.size(); ++i) {
            if (intervals[i][0] < intervals[i - 1][1]) return false;
        }

        return true;
    }
};

int test() {
    Solution solution;
    vector<vector<int>> intervals{};
    bool result = 0;

    intervals = {};
    result = true;
    assert(solution.canAttendMeetings(intervals) == result);

    intervals = {{0,30},{5,10},{15,20}};
    result = false;
    assert(solution.canAttendMeetings(intervals) == result);

    intervals = {{7, 10}, {2, 4}};
    result = true;
    assert(solution.canAttendMeetings(intervals) == result);

    cout << "self test passed!" << endl;

    return 0;
}

int main(int argc, char *argv[])
{
    // TODO: submit
    test();
    return 0;
}
