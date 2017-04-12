/*
 *
 */

#include <memory>
#include <assert.h>
#include <iostream>

using namespace std;

class Solution {
public:
    int getSum(int a, int b)
    {
	if (b == 0) {
	    return a;
	}
	int s = a ^ b;
	int carry = (a & b) << 1;
	return getSum(s, carry);
    }
};

int main(int argc, char** argv)
{
    shared_ptr<Solution> solution = shared_ptr<Solution>(new Solution());

    assert(solution->getSum(1, 2) == 3);
    assert(solution->getSum(0b1111, 0b0100) == 0b10011);
    assert(solution->getSum(-1, 10) == 9);

    std::cout << "self test passed" << std::endl;
}
