#include <iostream>

class Solution
{
  public:
    long long divide(long long dividend, long long divisor)
    {
        long long a = (dividend >= 0) ? dividend : -dividend;
        long long b = (divisor >= 0) ? divisor : -divisor;
        long long sign = (dividend < 0) ^ (divisor < 0);
        std::cout << "a: " << a << "b: " << b << "sign: " << sign << std::endl;
        long long quotient = 0;
        long long c = b;
        long long order = 0;
        while (a >= b)
        {
            order = 0;
            c = b;
            while ((c << 1) <= a && (c << 1) > 0)
            {
                c = (c << 1);
                order += 1;
            }
            std::cout << "a: " << a << " c: " << c << std::endl;
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
    std::cout << "4 / 2 == " << Solution().divide(2147483647, -1) << std::endl;
    // std::cout << "4 / 2 == " << Solution().divide(-1, 2) << std::endl;
    std::cout << "4 / 2 == " << Solution().divide(-1010369383, -2147483648)
              << std::endl;
    return 0;
}
