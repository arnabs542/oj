#include <stdio.h>

int min_diff(int *a,int n)
{
    if (n < 2)
    {
        return 0;
    }

    register int left = 0,right = 1,diff = a[right] - a[left];
    register int new_left = -1,new_right = -1,i;
    for (i=2;i<n;i++)
    {
        if (a[i] < a[right])
        {
            right = i;
            /*diff = a[right] - a[left];*/
            if (new_left != -1)
            {
                left = new_left;
            }
        }
        else if (a[i] > a[left] && a[i] > a[new_left])
        {
            new_left = i;
        }
        else if (new_left != -1)
        {
            if (a[i] - a[new_left] < a[right] - a[left])
            {
                left = new_left;
                right = i;
            }
        }
        /*printf("left :%d,new_left: %d,right: %d\n",*/
                /*a[left],a[new_left],a[right]);*/
    }
    printf("%d\n",a[right]-a[left]);
}

int main()
{
    int n;
    scanf("%d",&n);
    int a[n],i;
    for (i=0;i<n;i++)
    {
        scanf("%d",a+i);
    }
    min_diff(a,n);
    return 0;
}
