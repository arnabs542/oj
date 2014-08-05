#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

//@N: the upper bound of multiplication number
//@returns total number of factorization
static inline int factorize(int a,int N)
{
    register int i;
    register int res = 0;
    for(i=1;i<=N&& i <= sqrt((double)a); i++)
    {
        if( a%i ==0)
        {
            if (a/i <= N)
                res ++;
        }
    }
    return res;
}


static inline int distinct_num(int n)
{
    register int res = 0,i,j,num;
    register int multi=0;
    register int a;
    /*int times[n*n];*/
    /*memset(times,0,sizeof(times));*/
    for(i=1;i<=n;i++)
        for(j=i;j<=n;j++)
        {
            num = i*j;
            a = factorize(num,n);
            if (a != 1)
            {
                multi += a - 1;
                /*printf("n = %d,%d*%d is not\n",n,i,j);*/
            }
        }
    return n*(n+1)/2 - multi;
}

int main(int argc,char **argv)
{
    int n;
    while(scanf("%d",&n) != EOF)
    {
        printf("%d\n",distinct_num(n));
        /*printf("%d: %d",n,factorize());*/
    }
    return 0;
}
