#include <stdio.h>
int AdditionTest(int a, int b);
int main() {
    int a = 0, b = 0;
    while (scanf("%d %d", &a, &b) == 2) {
        printf("%d\n", AdditionTest(a, b));
    }
    return 0;
}

int AdditionTest(int a, int b)
{
    return a + b;
}
