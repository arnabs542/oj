#!/bin/python2

import sys

def compare_slen(x,y):
    return cmp(len(x),len(y))

class Solution:
    def qs_partition(self,li,start,end,compare):
        j = start - 1
        if compare == None:
            compare = cmp

        for i in range(start,end):
            if compare(li[i],li[end]) <= 0:
                j = j + 1
                tmp = li[i]
                li[i] = li[j]
                li[j] = tmp

        tmp = li[j + 1]
        li[j+1]=li[end]
        li[end]=tmp

        return j + 1


    def quicksort(self,li,start,end,compare = None):
        if start < end:
            pivot = self.qs_partition(li,start,end,compare)
            self.quicksort(li,start,pivot - 1,compare)
            self.quicksort(li,pivot + 1,end,compare)

        return li

    def qs_sort(self,li,compare):
        return self.quicksort(li,0,len(li)-1,compare)

    def childHomework(self,choices):
        choices = self.qs_sort(choices,compare_slen)

        result = []
        if  2*(len(choices[0]) -2) <=(len(choices[1]) - 2) :
            result.append(choices[0][0])

        if (len(choices[3])-2)  >=  2*(len(choices[2]) - 2):
            result.append(choices[3][0])

        if len(result) != 1:
            return 'C'
        else:
            return result[0]


if __name__ == "__main__":
    #print Solution().childHomework(["A.VFleaKing_is_the_author_of_this_problem",
    #"B.Picks_is_the_author_of_this_problem",
    #"C.Picking_is_the_author_of_this_problem",
    #"D.Ftiasch_is_cute"])
    #print Solution().childHomework(["A.ab",
    #"B.abcde",
    #"C.ab",
    #"D.abc",
    #])

    choices = []
    i = 0
    while True:
        line = sys.stdin.readline()
        if line.strip() == "":
            continue
        choices.append(line.strip())
        i += 1
        if i == 4:
            break

    #for choice in choices:
    #print len(choice),choice

    print Solution().childHomework(choices)
