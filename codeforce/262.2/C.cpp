#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#define lol long long
using namespace std;

const lol MAXVAL = 1000100000;
lol n, m, w;
vector<lol> a;

void read()
{
    cin >> n >> m >> w; // m - number of moves,  w - width
    a.resize(n);
    for (lol i = 0; i < n; i++)
        cin >> a[i];
}

bool check(lol x)
{
    vector<lol> st(n, 0);
    lol scurr = 0;
    lol moves = 0;
    for (lol i = 0; i < n; i++)
    {
        scurr -= i - w >= 0 ? st[i - w] : 0;
        if (a[i] + scurr < x)
        {
            st[i] = x - a[i] - scurr;
            scurr += st[i];
            moves += st[i];
        }
        if (moves > m)
            return 0;
    }
    return moves <= m;
}

void solve()
{
    lol l = 1;
    lol r = MAXVAL;
    lol x;
    while (l <= r)
    {
        lol md = (l + r) >> 1;
        if (check(md))
        {
            x = md;
            l = md + 1;
        }
        else
            r = md - 1;
    }

    cout << x << endl;
}

int main()
{
    ios_base::sync_with_stdio(0);
    read();
    solve();
    return 0;
}
