# -*- coding:utf-8 -*-
'''
Problem Statement
    
You are given a string S. You can modify this string by repeating the following process:
Find the leftmost occurrence of two consecutive letters in S that are the same.
If you found a pair of identical letters in the first step, delete those two letters from S.
For example, if S="aabccb", you can proceed as follows:
Find and erase "aa", producing the string "bccb".
Find and erase "cc", producing the string "bb".
Find and erase "bb", producing the empty string.
For S="axxyybac" you can do at most two steps, erasing "xx" first and "yy" next. Once you obtain the string "abac", you are done. Note that you cannot erase the two "a"s because they are not consecutive. You want to change S into an empty string by repeating the operation described above. Return "Possible" if you can do that, and "Impossible" otherwise.
Definition
    
Class:
DoubleLetter
Method:
ableToSolve
Parameters:
string
Returns:
string
Method signature:
def ableToSolve(self, S):

Limits
    
Time limit (s):
2.000
Memory limit (MB):
256
Constraints
-
S will contain between 1 and 50 characters.
-
Each character in S will be a lowercase English letter ('a'-'z').
Examples
0)

    
"aabccb"
Returns: "Possible"

1)

    
"aabccbb"
Returns: "Impossible"
The process will terminate with a single 'b'.
2)

    
"abcddcba"
Returns: "Possible"
"abcddcba" -> "abccba" -> "abba" -> "aa" -> "".
3)

    
"abab"
Returns: "Impossible"
No two successive letters are the same, so we can't do any operation.
4)

    
"aaaaaaaaaa"
Returns: "Possible"

5)

    
"aababbabbaba"
Returns: "Impossible"

6)

    
"zzxzxxzxxzzx"
Returns: "Possible"

This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.
'''


class DoubleLetter:

    def ableToSolve(self, S):
        sl = list(S)
        c = 1
        while c > 0:
            n = len(sl)
            new_sl = []
            i = 0
            while i < n - 1:
                if sl[i] == sl[i + 1]:
                    i = i + 2
                    pass
                else:
                    new_sl.append(sl[i])
                    i = i + 1
            if i == n - 1:
                new_sl.append(sl[i])
            sl = new_sl
            if n == len(sl):
                break

        if len(sl) == 0:
            return "Possible"
        else:
            return "Impossible"

if __name__ == "__main__":
    print DoubleLetter().ableToSolve("aabccb")
    print DoubleLetter().ableToSolve("abcddcba")
    print DoubleLetter().ableToSolve("aababbabbaba")
