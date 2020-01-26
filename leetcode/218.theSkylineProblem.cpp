/**
 *
 * 218. The Skyline Problem
Hard

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

Buildings Skyline Contour
The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]


Accepted
114.4K
Submissions
344.7K

================================================================================
SOLUTION

For each building, there are two critical points: start and end points,
with another dimension height. A building start and end points correspond to
an interval.

1) The simplest case is when there are no interval overlapping.
2) What if there are overlapping intervals?

1. Brute force - line sweep scanning - interval overlapping
We can iterate over all intervals points in a line sweep approach.
For each start point, we need to determine whether there is an interval x covering
it. By cover, we mean the interval overlap and x.height is larger.
For each end point, we need to find the highest interval that overlaps with
current one.

Complexity: O(n²)

2. Heap - keep track of overlapping intervals with height
For intervals without height, we can use a heap of intervals with end point as key.
Now we have to get the highest interval that overlaps with each others.

Some observations:
1) If an interval is lower than others even it has already ended, then it can
be ignored.
2) Overlapping intervals with same height can be merged.

Use (height, end point) as key!

TODO: implement

3. Line sweep of start and end points - ordered to keep track of overlapping intervals heights
For each start point, we want to know whether there are high intervals which
overlaps with it. An overlapping interval must have its end point no less than
current start point.
So we can remove the interval when the sweeping line scans its end point!

1) Collect ordered list of (start point, -height), (start point, height)
2) Line sweep over points, use a self balancing binary search tree to
keep track of heights. For each start point, add it to ordered tree. For each end
point, pop out its start point.

Complexity: O(NlogN)

 *
 */

#include <debug.hpp>

class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        vector<vector<int>> result;
        result = getSkylineLineSweepPoints(buildings);

        cout << buildings << " => " << result << endl;

        return result;
    }

    vector<vector<int>> getSkylineHeap(vector<vector<int>> &buildings) {

    }

    vector<vector<int>> getSkylineLineSweepPoints(vector<vector<int>> &buildings) {
        vector<vector<int>> result;

        vector<vector<int>> points; // line sweep points
        for (vector<int> &interval: buildings) {
            points.push_back({interval[0], -interval[2]}); // of same height, start points come first
            points.push_back({interval[1], interval[2]});
        }
        sort(points.begin(), points.end());

        multiset<int> tree; // keep track of overlapping intervals heights
        //cout << points << endl;
        //int preH = 0, currH = 0;
        for (vector<int> &xy: points) {
            if (xy[1] < 0) {
                int h = -xy[1];
                if (tree.empty() || *tree.rbegin() < h) {
                    result.push_back({xy[0], h}); // TODO: can keep track of maximum height manually
                }
                tree.insert(h);
            } else if (xy[1] > 0) { // XXX: symmetric, no =
                //tree.erase(xy[1]); // XXX: erase(val) will remove all keys of val!
                tree.erase(tree.find(xy[1])); // pop out corresponding interval. [1, 4], [2, 3]
                int newH = tree.size() ? *tree.rbegin():0;
                if (newH < xy[1]) {
                    result.push_back({xy[0], newH}); // new height
                }
            }
        }

        return result;
    }
};

int test() {
    Solution solution;
    vector<vector<int>> buildings;
    vector<vector<int>> output;

    buildings = {{0, 1, 0}};
    output = {};
    assert(solution.getSkyline(buildings) == output);

    buildings = {{0, 1, 1}};
    output = {{0, 1}, {1, 0}};
    assert(solution.getSkyline(buildings) == output);

    buildings = {{0, 1, 1}, {1, 2, 3}};
    output = {{0, 1}, {1, 3}, {2, 0}};
    assert(solution.getSkyline(buildings) == output);

    buildings = {{0, 4, 2}, {1, 2, 1}};
    output = {{0, 2}, {4, 0}};
    assert(solution.getSkyline(buildings) == output);

    buildings = {{0,2,3},{2,5,3}}; // [0,-3],[2,-3],[2,3],[5,3]; [[0,3],[2,0],[5,0]]
    output = {{0,3},{5,0}};
    assert(solution.getSkyline(buildings) == output);

    buildings = {{2,9,10},{3,7,15},{5,12,12},{15,20,10},{19,24,8}};
    output = {{2,10},{3,15},{7,12},{12,0},{15,10},{20,8},{24,0}};
    assert(solution.getSkyline(buildings) == output);

    cout << "test passed" << endl;

    return 0;
}

int main(int argc, char **argv) {
    test();
    return 0;
}
