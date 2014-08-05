#include <iostream>
#include <map>
#include <string>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int is_integer(char *s,int n)
{
    int i;
    for(i=0;i<n && isdigit(s[i]);i++);
    if (i != n)
    {
        return 0;
    }
    return 1;
}

int get_votes()
{
    std::map<std::string,int> map_vote;
    int voteid;
    char candidate[10];
    while(scanf("%d%s",&voteid,candidate)!= EOF)
    {
        if (is_integer(candidate,strlen(candidate)))
        {

        }
        else
        {
            std::string s(candidate);

        }
        printf("%d,%s\n",voteid,candidate);
    }
    return 0;
}

int main(int argc,char **argv)
{
    //std::string id;
    //int vote;
    //while(std::cin>>id>>vote)
    //{
        //std::cout<<id<<" "<<vote<<std::endl;
    //}


    return 0;
}
