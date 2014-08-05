#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

struct point
{
    int x;
    int y;
};

struct mirror
{
    struct point p;
    char direction;
};

char mirror_dir[2]= {'/','\\'};

inline int get_direction(char x)
{
    switch(x)
    {
        case 'n':
            return 0;
        case 'e':
            return 1;
        case 's':
            return 0;
        case 'w':
            return 1;
        default:
            return -1;
    }
}

int diff_direction(char x,char y)
{
    return get_direction(x) - get_direction(y);
}

int get_mirrors(char *s)
{
    int d[5],i;
    char *ps;
    struct point mirrors[5];
    char mdir[5];
    int n_mirrors = 0;
    int j;
    for (i =0; i < 5;i++)
    {
        ps = s + i * 6;
        if (diff_direction(*(ps+2),*(ps+5)) == 0)
        {
            //same or opposite direction of in and out
            d[i] = 0;
        }
        else
        {
            //only reflected by one mirror
            d[i] = 1;
            ++n_mirrors;
            mirrors[n_mirrors - 1].x = ps[2];
            mirrors[n_mirrors - 1].y = ps[5];
            if ( (ps[2] == 'w' && ps[5] == 's') ||(ps[2] == 's' && ps[5]== 'w'))
            {
                mdir[n_mirrors - 1] = '/';
            }
            else if ((ps[2] == 'e' && ps[5] == 'n') || (ps[2] == 'n' && ps[5] == 'e'))
            {
                mdir[n_mirrors - 1] = '\\';
            }

            for ( i = 0; i < 5;i++)
            {
                if (d[i] == 0)
                {
                    if (ps[2] == 'n' || ps[2] =='s')
                    {
                        for ( j = 0;j < n_mirrors-1; j ++)
                        {
                            if (mirrors[j].y == ps[1] - '0')
                            {
                                n_mirrors ++;
                                mirrors[n_mirrors -1].x = mirrors[j].x;
                                mirrors[n_mirrors -1].y = ps[4] - '0';
                                if (ps[5] == ps[2])
                                {
                                    mdir[n_mirrors -1] = '\\';
                                }
                                else
                                {
                                    mdir[n_mirrors -1] = '/';
                                }
                                continue;
                            }

                            if(mirrors[j].y == ps[4] - '0')
                            {
                                n_mirrors ++;
                                mirrors[n_mirrors-1].x = mirrors[j].x;
                                mirrors[n_mirrors-1].y = ps[1] - '0';

                                if (ps[4] > ps[1] )
                                {
                                    mdir[n_mirrors - 1] = '\\';
                                }
                                else
                                {
                                    mdir[n_mirrors - 1] = '/';
                                }
                            }
                        }
                    }//n,s
                    else
                    {
                        // w,e
                        for (j=0;j<n_mirrors;j++)
                        {
                        if (mirrors[j].x == ps[0] - '0')
                        {
                            n_mirrors ++;
                            mirrors[n_mirrors -1].y = mirrors[j].y;
                            mirrors[n_mirrors-1].x = ps[3] - '0';
                            if (ps[5] == ps[2] )
                            {
                                mdir[n_mirrors - 1] = '\\';
                            }
                            else
                            {
                                mdir[n_mirrors - 1] ='/';
                            }
                        }
                        else
                        {
                            if (mirrors[j].y == ps[3] - '0')
                            {
                                n_mirrors ++;
                                mirrors[n_mirrors-1].y = mirrors[j].y;
                                mirrors[n_mirrors-1].x = ps[0] - '0';
                                if (ps[3] > ps[0])
                                {
                                    mdir[n_mirrors - 1] = '/';
                                }
                                else
                                {
                                    mdir[n_mirrors - 1] = '\\';
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    }
}

int main()
{
    char str[30];
    int n,i;
    n = 30;
    for(i = 0 ;i< n;i++)
    {
        scanf("%c",str+i);
        while (isspace(str[i]))
        {
            scanf("%c",str+i);
        }
            /*scanf("%*[ \n\t]%c",str+i);*/
    }
    for (i=0;i<n;i++)
        printf("%c",str[i]);
    get_mirrors(str);
    /*printf("%s",str);*/
    return 0;
}
