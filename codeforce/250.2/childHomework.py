#!/bin/python2

'''
A. The Child and Homework
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
Once upon a time a child got a test consisting of multiple-choice questions as homework. A multiple-choice question consists of four choices: A, B, C and D. Each choice has a description, and the child should find out the only one that is correct.

Fortunately the child knows how to solve such complicated test. The child will follow the algorithm:

If there is some choice whose description at least twice shorter than all other descriptions, or at least twice longer than all other descriptions, then the child thinks the choice is great.
If there is exactly one great choice then the child chooses it. Otherwise the child chooses C (the child think it is the luckiest choice).
You are given a multiple-choice questions, can you predict child's choose?

Input
The first line starts with "A." (without quotes), then followed the description of choice A. The next three lines contains the descriptions of the other choices in the same format. They are given in order: B, C, D. Please note, that the description goes after prefix "X.", so the prefix mustn't be counted in description's length.

Each description is non-empty and consists of at most 100 characters. Each character can be either uppercase English letter or lowercase English letter, or "_".

Output
Print a single line with the child's choice: "A", "B", "C" or "D" (without quotes).

Sample test(s)
input
A.VFleaKing_is_the_author_of_this_problem
B.Picks_is_the_author_of_this_problem
C.Picking_is_the_author_of_this_problem
D.Ftiasch_is_cute
output
D
input
A.ab
B.abcde
C.ab
D.abc
output
C
input
A.c
B.cc
C.c
D.c
output
B
Note
In the first sample, the first choice has length 39, the second one has length 35, the third one has length 37, and the last one has length 15. The choice D (length 15) is twice shorter than all other choices', so it is great choice. There is no other great choices so the child will choose D.

In the second sample, no choice is great, so the child will choose the luckiest choice C.

In the third sample, the choice B (length 2) is twice longer than all other choices', so it is great choice. There is no other great choices so the child will choose B.
'''

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
