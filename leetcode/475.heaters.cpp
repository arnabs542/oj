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
Objective: (MAXMIN) find closest heater to each house for minimal distance, and

1. Linear scan
For each pair of adjacent heaters, scan houses in between.

Complexity: O(NlogN+MlogM)

2. Linear scan - keep tracking of individual house and heater pair
Above solution tracks two adjacent heaters, making it more complex!
Since the houses and heaters can be sorted first, there are some
TRANSITIVE PROPERTY DUE TO THE ORDERING of elements!

Complexity:
O(NlogN + MlogM)

2. Binary search
For each house find nearest heater in logarithm time.

Sort, and for each house, do binary search on heaters.

TODO:

Complexity: O(MlogM + NlogM)

3. Lower bound with map

Complexity:


 *
 */

#include <debug.hpp>

class Solution {
public:
    int findRadius(vector<int>& houses, vector<int>& heaters) {
        int result = 0;
        //result = findRadiusLinearScan(houses, heaters);
        //result = findRadiusLinearScanSimple(houses, heaters);
        result = findRadiusBinarySearch(houses, heaters);

        cout << houses << " " << heaters << " " << result << endl;

        return result;
    }

    /**
     * Too complex!
     *
     */
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

    int findRadiusLinearScanSimple(vector<int> &houses, vector<int> &heaters) {
        sort(houses.begin(), houses.end());
        sort(heaters.begin(), heaters.end());

        uint i = 0, j = 0; // house, heater index
        int radius = 0;
        while (i < houses.size() && j < heaters.size()) { // for each house
            while (j < heaters.size() - 1 && abs(houses[i] - heaters[j]) >= abs(houses[i] - heaters[j+1])) ++j; // XXX: search for nearest heater
            radius = max(radius, abs(houses[i] - heaters[j]));
            //if (j == heaters.size() - 1) break;
            ++i;
        }

        return radius;
    }

    int findRadiusBinarySearch(vector<int> &houses, vector<int> &heaters) {
        sort(heaters.begin(), heaters.end());
        int radius = 0;
        //map<int, vector<int>> a{{1,{2,3,4}}};
        //cout << a << endl;
        for (int house: houses) {
            int low = 0, high = heaters.size() - 1; // XXX: high = 0,  low = heaters.size() - 1;
            int bestH = -1, minR = std::numeric_limits<int>::max(); // best index, value
            while (low <= high) {
                int mid = (low+high) >> 1;
                // binary search
                int diff = house - heaters[mid];
                if (diff > 0) {
                    low = mid + 1;
                } else if (diff < 0) {
                    high = mid - 1;
                } else {
                    bestH = mid;
                    minR = 0;
                    break;
                }

                int dis = std::abs(diff);
                //cout << "DDDD: " << house << " " << mid << " " << dis << " " << minR << endl;
                if (dis < minR) {
                    bestH = mid;
                    minR = dis;
                }
                //cout << "DDDD: " << house << " " << mid << " " << dis << " " << minR << endl;
            }
            radius = std::max(radius, minR); // max min
        }

        return radius;
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

    houses = {1, 2, 3, 4, 5, 6, 7};
    heaters = {1, 1, 2, 3, 4, 5, 6, 7};
    result = 0;
    assert(solution.findRadius(houses, heaters) == result);

    houses = {};
    heaters = {};
    for (int i = 0; i < 15225; ++i) {
        houses.push_back(i+1);
        houses.push_back(i+1);
        heaters.push_back(i+1);
        heaters.push_back(i+1);
    }
    result = 0;
    //assert(solution.findRadius(houses, heaters) == result);

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
