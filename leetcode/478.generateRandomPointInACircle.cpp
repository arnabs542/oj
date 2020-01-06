/**
 *
478. Generate Random Point in a Circle
Medium

Given the radius and x-y positions of the center of a circle, write a function randPoint which generates a uniform random point in the circle.

Note:

1. input and output values are in floating-point.
2. radius and x-y position of the center of the circle is passed into the class constructor.
3. a point on the circumference of the circle is considered to be in the circle.
4. randPoint returns a size 2 array containing x-position and y-position of the random point, in that order.

Example 1:

Input:
["Solution","randPoint","randPoint","randPoint"]
[[1,0,0],[],[],[]]
Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]
Example 2:

Input:
["Solution","randPoint","randPoint","randPoint"]
[[10,5,-7.5],[],[],[]]
Output: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has three arguments, the radius, x-position of the center, and y-position of the center of the circle. randPoint has no arguments. Arguments are always wrapped with a list, even if there aren't any.

SOLUTION
================================================================================

1. Conditional probability
This is conditional probability again.
Similar to "implement rand10 using rand7".

p((x,y)|(x, y) in circle) = p((x,y)|x^2+y^2 <= r^2)
Then we can just sample (x,y), until the condition is met.

The problem is how to generate uniform random floating number?
We can approximate with rand()/RAND_MAX...

2. Polar coordinate
Now just generate uniformly distributed (r, \theta).
The problem is, r is not uniformly distributed.

In 2D space, the probability of a region is proportional to its area.
And for a circle with radius r, its area is \pi*r^2.


 */

#include <debug.hpp>
#include <random>
#include <cstdlib>

class Solution {
public:
    Solution(double radius, double x_center, double y_center) {
        this->mRadius = radius;
        this->mXCenter = x_center;
        this->mYCenter = y_center;
    }

    vector<double> randPoint() {
        vector<double> result;
        result = randPointConditionalProbability();
        //result = randPointConditionalProbability();

         //cout << result << endl;

         return result;
    }

    vector<double> randPointConditionalProbability() {
        if (this->mRadius == 0) return {0, 0};
        vector<double> results{0, 0};
        while (true) {
            double x = (rand()*1.0 / RAND_MAX)*2 - 1; // x, [-1,1]
            double y = (rand()*1.0 / RAND_MAX)*2 - 1; // y, [-1,1]
            results = {mXCenter + x * mRadius, mYCenter + y * mRadius};
            if (x*x + y*y <= 1) return results; // condition met
        }

        return results;
    }

    vector<double> randPointPolarCoordinate() {
        vector<double> results{0, 0};
        if (mRadius == 0) return results;
        double r = sqrt(rand()*1.0/RAND_MAX) * mRadius;
        double theta = 2*3.1415926*(rand()*1.0/RAND_MAX);
        results = {mXCenter + r*cos(theta), mYCenter + r*sin(theta)};
        return results;
    }

    double mRadius;
    double mXCenter;
    double mYCenter;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(radius, x_center, y_center);
 * vector<double> param_1 = obj->randPoint();
 */

vector<int> test(vector<string> &ops, vector<vector<int>> &nums) {
    double radius, x, y;

    Solution solution(10.0, 0.0, 0.0);

    for (int i = 0; i < 10; ++i) {
        cout << solution.randPoint() << endl;
    }

    radius = 100, x = 10.0, y = -10.0;
    cout << radius << ", " << x << ", " << y << endl;
    solution = Solution(100.0, 10.0, -10.0);

    for (int i = 0; i < 10; ++i) {
        cout << solution.randPoint() << endl;
    }
    //cout << solution.randPoint() << endl;
    // TODO: test

    return {};
}

int main(int argc, char *argv[])
{
    //Solution solution();
    vector<string> ops;
    vector<vector<int>> nums;
    test(ops, nums);

    return 0;
}
