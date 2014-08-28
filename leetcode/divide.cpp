#include <iostream>

class Solution
{
  public:
    int divide(int dividend, int divisor)
    {
        int a = (dividend >= 0) ? dividend : -dividend;
        int b = (divisor >= 0) ? divisor : -divisor;
        int sign = (dividend < 0) ^ (divisor < 0);
        std::cout << "a: " << a << "b: " << b << "sign: " << sign << std::endl;
        int quotient = 0;
        int c = b;
        int order = 0;
        while (a >= b)
        {
            order = 0;
            c = b;
            while ((c << 1) <= a)
            {
                c = (c << 1);
                order += 1;
                std::cout << "a: " << a << " c: " << c << std::endl;
            }
            a -= c;
            quotient += (1 << order);
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
    std::cout << "4 / 2 == " << Solution().divide(-2147483647, 1) << std::endl;
    return 0;
}
