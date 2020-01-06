/**
 *
475. Heaters
Easy

Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters separately, and your expected output will be the minimum radius standard of heaters.

Note:

Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.


Example 1:

Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.


Example 2:

Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.

SOLUTION
================================================================================


1. Linear scan
For each pair of adjacent heaters, scan houses in between.

Complexity: O(NlogN+MlogM)

2. Binary search
For each house

Complexity: O(NlogN + MlogM + NlogM)

 *
 */

#include <debug.hpp>

class Solution {
public:
    int findRadius(vector<int>& houses, vector<int>& heaters) {
        int result = 0;
        result = findRadiusLinearScan(houses, heaters);

        return result;
    }

    int findRadiusLinearScan(vector<int> &houses, vector<int> &heaters) {
        sort(houses.begin(), houses.end());
        sort(heaters.begin(), heaters.end());
        cout << houses << heaters << endl;

        int r = 0;
        int h = 0, p = 0, q = 1; // house index, heater index

        // before alignment
        while (h < (int)houses.size() && p < (int)houses.size() &&
                houses[h] < heaters[p]) {
            r = max(r, std::abs(heaters[p] - houses[h]));
            ++h;
        }
        // iterate houses
        while (q < (int)heaters.size() && h < (int)houses.size()) { // h?
            if (houses[h] <= heaters[q]) {
                int t = std::min(houses[h] - heaters[p], heaters[q] - houses[h]);
                r = max(r, t);
                ++h; // XXX
            } else {
                ++p;
                ++q;
            }

        }
        for (; h < (int) houses.size(); ++h) {
            r = std::max(r, std::abs(houses[h] - heaters[p]));
        }

        return r;
    }
};

int test() {
    Solution solution;
    vector<int> houses;
    vector<int> heaters;
    int result = 0;

    houses = {};
    heaters = {};
    result = 0;
    assert(solution.findRadius(houses, heaters) == result);

    houses = {};
    heaters = {1, 2, 3};
    result = 0;
    assert(solution.findRadius(houses, heaters) == result);

    houses = {1};
    heaters = {1};
    result = 0;
    assert(solution.findRadius(houses, heaters) == result);

    houses = {1};
    heaters = {2};
    result = 1;
    assert(solution.findRadius(houses, heaters) == result);

    houses = {1, 2, 3};
    heaters = {2};
    result = 1;
    assert(solution.findRadius(houses, heaters) == result);

    houses = {1, 2, 3, 4};
    heaters = {1, 4};
    result = 1;
    assert(solution.findRadius(houses, heaters) == result);

    houses = {1, 4};
    heaters = {1, 4};
    result = 0;
    assert(solution.findRadius(houses, heaters) == result);

    houses = {474833169,264817709,998097157,817129560};
    heaters = {197493099,404280278,893351816,505795335};
    result = 104745341;
    assert(solution.findRadius(houses, heaters) == result);

    cout << "self test passed!" << endl;
    return 0;
}

int main(int argc, char **argv) {
    test();
    return 0;
}
