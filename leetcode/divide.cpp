#include <iostream>

class Solution
{
  public:
    int divide(int dividend, int divisor)
    {
        int a = dividend >= 0 ? dividend : -dividend;
        int b = divisor >= 0 ? divisor : -divisor;
        int sign = (dividend < 0) ^ (divisor < 0);
        int quotient = 0;
        int c = b;
        int order = 0;
        while (a >= b)
        {
            order = 0;
            c = b;
            while (c << 1 <= a)
            {
                c = c << 1;
                order += 1;
            }
            a -= c << order;
            quotient += 1 << order;
        }

        if (sign > 0)
        {
            return -quotient;
        }
        else
            return quotient;
    }
};

int main(int argc, char **argv)
{
    std::cout << "4 / 2 == " << Solution().divide(4, -3) << std::endl;
    return 0;
}
