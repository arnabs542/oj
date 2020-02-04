/**
 *
850. Rectangle Area II
Hard

We are given a list of (axis-aligned) rectangles.  Each rectangle[i] = [x1, y1, x2, y2] , where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the ith rectangle.

Find the total area covered by all rectangles in the plane.  Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:

Input: [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: As illustrated in the picture.
Example 2:

Input: [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 = (-7)^2 = 49.
Note:

1 <= rectangles.length <= 200
rectanges[i].length = 4
0 <= rectangles[i][j] <= 10^9
The total area covered by all rectangles will never exceed 2^63 - 1 and thus will fit in a 64-bit signed integer.


Accepted
9,470
Submissions
20,465

================================================================================
SOLUTION

This is a classic computational geometry problem involving interval intersecting.
For interval overlapping problem, line sweep algorithm suits well.

Process the rectangles in a manner with a line sweeping through rectangle sides.

1. Line sweep - scan along x axis - keep track of OVERLAPPING INTERVALS, ordered by key (y1, y2) ,
First we need to sort rectangle left and right sides, represented with tuple (x, y1, y2).
Then line sweep  through the sides/intervals along x axis.

And we need to use a data structure to maintain overlapping rectangles(similar to
overlapping intervals). And we need this structure to calculate area in between two
adjacent sweep line, so we need this data structure to be ordered with respect to
key (y1, y2), and also identifiable by the original rectangle.

For left side (x, y1, y2):
    1) compute area between current side and previous side: +dy*(x-x0),
    2) insert tuple (y1, y2, x) into ordered data structure.
For right side (x, y1, y2):
    3) do 1)
    4) pop out corresponding left side (x₀, y1, y2).
Termination: scanned all rectangle sides.

Corner case:
1) duplicate rectangles: using ordered tree supporting duplicate keys, fine with the procedure above
2) rectangles with same (y1, y2), how to find corresponding left & right segment:
    can be combined into one larger rectangle, no need to corresponding one.

Complexity: O(NlogN), worst O(N²) for same x values

TODO: optimize
1) No need to scan overlapped rectangles to compute, if left side x is equal to
previous one.
2) Deal with worst case specifically

2. Segment tree - interval overlapping

================================================================================
https://community.topcoder.com/stat?c=problem_statement&pm=4463&rd=6536

 *
 */

#include <debug.hpp>

class Solution {
public:
    int rectangleArea(vector<vector<int>>& rectangles) {
        int result;
        result = rectangleAreaLineSweep(rectangles);

        cout << rectangles << " => " << result << endl;

        return result;
    }

    int rectangleAreaLineSweep(vector<vector<int>> &rectangles) {
        //vector<vector<int>> segments; // (x, y1, y2, s), s: 1, -1 for left and right segments respectively
        vector<tuple<int, int, int, int>> segments; // (x, y1, y2, s), s: 1, -1 for left and right segments respectively
        for (vector<int> &rect: rectangles) {
            segments.push_back({rect[0], rect[1], rect[3], 1}); // begin side segment
            segments.push_back({rect[2], rect[1], rect[3], -1}); // end side
        }
        sort(segments.begin(), segments.end());

        //multiset<vector<int>> ordered; // ordered tree
        multiset<tuple<int, int>> ordered; // ordered tree, of (y1, y2)
        //for (vector<int> &segment: segments) {
        int MOD = 1000000000 + 7; // MODULO_BASE
        long area = 0;
        int xp = 0; // previous x
        for (auto &segment: segments) { // line sweep
            int x, y1, y2, s;
            std::tie(x, y1, y2, s) = segment;
            int yp = std::numeric_limits<int>::min();
            for (auto it = ordered.begin(); it != ordered.end(); ++it) {
                //int y1, y2;
                int y3, y4;
                std::tie(y3, y4) = *it;
                y3 = max(y3, yp);
                if (y4 > y3) {
                    area += ((long)(y4 - y3)) * ((long)(x - xp)) % MOD;
                }
                yp = max(yp, y4); // previous y
            }
            xp = x;
            if (s == 1) {
                //ordered.insert({y1, y2}); // XXX: ?
                ordered.insert(make_tuple(y1, y2));
                //cout << "inserting " << vector<int>{y1, y2} << endl;
            } else if (s == -1) {
                int a, b;
                std::tie(a, b) = *ordered.begin();
                //cout << "first " << a << " " << b << " size: " << ordered.size() << endl;
                ordered.erase(ordered.find({y1, y2}));
            }
        }

        return area % MOD; // 10⁹
    }
};

int test() {
    Solution solution;

    vector<vector<int>> rectangles;
    int output;

    rectangles = {};
    output = 0;
    assert(solution.rectangleArea(rectangles) == output);

    rectangles = {{0, 0, 1, 2}};
    output = 2;
    assert(solution.rectangleArea(rectangles) == output);

    rectangles = {{0, 0, 1, 2}, {0, 0, 1, 2}};
    output = 2;
    assert(solution.rectangleArea(rectangles) == output);

    rectangles = {{0, 0, 1, 1}, {0, 0, 2, 2}};
    output = 4;
    assert(solution.rectangleArea(rectangles) == output);

    rectangles = {{0, 0, 1, 2}, {1, 0, 3, 2}};
    output = 6;
    assert(solution.rectangleArea(rectangles) == output);

    rectangles = {{0, 0, 1, 2}, {3, 0, 4, 2}};
    output = 4;
    assert(solution.rectangleArea(rectangles) == output);

    rectangles = {{0, 0, 2, 3}, {1, 0, 4, 3}};
    output = 12;
    assert(solution.rectangleArea(rectangles) == output);

    rectangles = {{0,0,2,2},{1,0,2,3},{1,0,3,1}};
    output = 6;
    assert(solution.rectangleArea(rectangles) == output);

    rectangles = {{0,0,1000000000,1000000000}};
    output = 49;
    assert(solution.rectangleArea(rectangles) == output);

    rectangles = {{224386961,128668997,546647847,318900555},{852286866,238086790,992627088,949888275},{160239672,137108804,398130330,944807066},{431047948,462092719,870611028,856851714},{736895365,511285772,906155231,721626624},{289309389,607009433,558359552,883664714},{780746435,397872372,931219192,863727103},{573523994,124874359,889018012,471879750},{619886375,149607927,727026507,446976526},{51739879,716225241,115331335,785850603},{171077223,267051983,548436248,349498903},{314437215,169054168,950814572,481179241},{64126215,646689712,595562376,829164135},{926011655,481539702,982179297,832455610},{40370235,231510218,770233582,851797196},{292546319,45032676,413358795,783606009},{424366277,369838051,453541063,777456024},{211837048,142665527,217366958,952362711},{228416869,402115549,672143142,644930626},{755018294,194555696,846854520,939022548},{192890972,586071668,992336688,759060552},{127869582,392855032,338983665,954245205},{665603955,208757599,767586006,276627875},{260384651,10960359,736299693,761411808},{46440611,559601039,911666265,904518674},{54013763,90331595,332153447,106222561},{73093292,378586103,423488105,826750366},{327100855,516514806,676134763,653520887},{930781786,407609872,960671631,510621750},{35479655,449171431,931212840,617916927}};
    output = 862275791;
    assert(solution.rectangleArea(rectangles) == output);

    cout << "test passed" << endl;
    return 0;
}

int main(int argc, char **argv) {

    test();
    return 0;
}
