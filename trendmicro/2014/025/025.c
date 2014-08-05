#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

//n objects respectively weigh w[i],value of v[i]
//i = 0 to n-1
//maximum weight capacity is W
int knapsack(int *w,int *v,int n,int W)
{
    int V[n + 1][W + 1],i,j;
    int keep[n + 1][W + 1];
    for(i = 0;i<= W;i++)
    {
        V[0][i] = 0;
    }

    for (i=1;i<=n;i++)
        for(j=0;j<=W;j++)
        {
            if((w[i-1] <= j) && (v[i-1] + V[i-1][j-w[i-1]]>V[i-1][j]))
            {
                V[i][j] = v[i-1] + V[i-1][j-w[i-1]];
                keep[i][j] = 1;
            }
            else
            {
                V[i][j] = V[i-1][j];
                keep[i][j] = 0;
            }
        }

    j = W;
    int output[n],top = -1;
    printf("%d\n",V[n][W]);
    for (i=n;i>=1;i--)
        if(keep[i][j] == 1)
        {
            /*printf("%d ",i - 1);*/
            output[++top] = i - 1;
            j = j - w[i-1];
        }

    for(i=top;i>=0;i--)
    {
        printf("%d ",output[i]);
    }
    /*printf("\n");*/
    return 0;
}

int main(int argc,char **argv)
{
    float W;
    int n;
    scanf("%f%d",&W,&n);
    /*printf("Maximum weight: %.1f,n: %d\n",W,n);*/
    int w[n],v[n];
    float fa,fb;
    int i,j;
    for(i=0;i<n;i++)
    {
        /*scanf("%d%f%f",&j,w+i,v+i);*/
        scanf("%d%f%F",&j,&fa,&fb);
        w[i] = fa;
        v[i] = fb;
    }
    knapsack(w,v,n,W);
    /*for(i=0;i<n;i++)*/
    /*{*/
        /*printf("%d--->%d\n",w[i],v[i]);*/
    /*}*/
    return 0;
}
