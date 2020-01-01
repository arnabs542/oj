/**
 *
812. Largest Triangle Area
Easy

You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation:
The five points are show in the figure below. The red triangle is the largest.


Notes:

3 <= points.length <= 50.
No points will be duplicated.
 -50 <= points[i][j] <= 50.
Answers within 10^-6 of the true value will be accepted as correct.


Accepted
18.2K
Submissions
31.8K

SOLUTION
================================================================================

1. Brute force - vector product

Area = 1/2*|AB×AC| # vector product
     = 1/2*|(xb-xa, yb-ya)×(xc-xa, yc-ya)|
     = 1/2*|(xb-xa)(yc-ya)-(yb-ya)(xc-xa)|
     = 1/2*|xb*yc-xb*ya-xa*yc-xc*yb+xa*yb+xc*ya|

Complexity: O(N³)

2. Convex hull optimization?

TODO:

Reference:
https://arxiv.org/pdf/1705.11035.pdf


 *
 */

#include <debug.hpp>


class Solution {
public:
    double largestTriangleArea(vector<vector<int>>& points) {
        double area;
        area = largestTriangleAreaBruteForceVectorProduct(points);

        cout << points << " " << area << endl;

        return area;
    }

    double largestTriangleAreaBruteForceVectorProduct(vector<vector<int>>& points) {
        double area = 0.;
        int n = points.size();
        for(int i = 0; i < n; ++i) {
            auto &a = points[i];
            for (int j = i + 1; j < n; ++j) {
                auto &b = points[j];
                for (int k = j + 1; k < n; ++k) {
                    auto &c = points[k];
                    area = std::max(area, 0.5*std::abs(
                        b[0]*c[1] + a[0]*b[1] + c[0]*a[1] - b[0]*a[1] - a[0]*c[1] - c[0]*b[1]
                                ));
                }
            }
        }

        return area;

    }
};

int main() {
    return 0;
}
