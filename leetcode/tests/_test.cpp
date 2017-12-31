#include "../_decorators.hpp"
#include <assert.h>
#include <iostream>

int main()
{
    auto fn = Memoized<int, int, int>([](int x, int y) -> int { return x + y; });
    assert(fn(3, 1) == 4);
    assert(fn.contains(3, 1));
    assert(fn(3, 1) == 4);
    assert(fn(5, 1) == 6);
    cout << "self test passed!" << endl;
}
