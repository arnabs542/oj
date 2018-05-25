#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
467. Unique Substrings in Wraparound String

Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.

Note: p consists of only lowercase English letters and the size of p might be over 10000.

Example 1:
Input: "a"
Output: 1

Explanation: Only the substring "a" of string "a" is in the string s.

Example 2:
Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.

Example 3:
Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.


================================================================================
SOLUTION

1. Brute force
Exhaust all substrings in p, and verify existence of unique ones.

Complexity
----------
Given string p of length n, there are (n + 1 - i) substrings of length i, 1<=i<=n.
For a substring with length i, the complexity to compare is: O(i).

So overall complexity is:
O(\sum_{i=1}^{n} (n+1-i)*i) = O(n^3) = O(n³).

2. Find locally longest substring, and count? - won't handle duplicate substrings
Above solution involves many duplicate calculations.

If we find a locally longest substring t that's substring of s, then unique substrings
of this substring t can be counted.

But how about duplicate substrings?
To filter duplicate substrings, we can use a HASH TABLE.

Complexity
----------
O(mp³), where there are amortized m locally longest substring of length p in s.
Approximately mp=n. Then O(mp³) = O(np²) <= O(n³), equal when p = n.

Well the worst case complexity is still high.
Can we do better?
When we find a locally longest substring t, in s, can unique substrings be
counted directly?

Math analysis - counting
------------------------
Observe that the infinite wraparound string is periodic.
If a string of length l is substring of s, then we can count unique substrings
of it, grouping by substring length:
  1: min(26, l)
  2: min(26, l + 1 - 2)
  3: min(26, l + 1 - 3)
  ...
  i: min(26, l + 1 - i)
  ...
  l: min(26, l + 1 - l)

Total number is \sum_{i=1}^{l} min(26, l + 1 - i), which can be calculated in O(l).

--------------------------------------------------------------------------------
Now the problem is to find all locally longest substring of p that's in s.

1) A naive method would be iterating all substrings. O(n³)...
2) How about state transition, like KMP state machine algorithm?

However, there is another problem: there are many non-overlapping substrings of p
in s, and they may cause duplicates!

So this method is just not better.

3. Efficient tuple REPRESENTATION of string: (starting character, length)

Representation
--------------
The periodic string can be represented with string, which takes O(l) to process,
where l is the length.

It can also be represented with a tuple: (start character, string length)
In this way, processing the string will just take O(1).

Complexity
----------
And a brute force exhaustive search will take O(n²).
O(n²), O(n²)

--------------------------------------------------------------------------------
Track only maximum length, instead of all tuples.

Complexity: O(n²), O(26)=O(1)

4. Partition and calculate - find locally longest substring

Apparently, there are overlapping problems involved in the above methods.

Partition by finding locally longest substring with sliding window and calculate, in O(n).

And eliminate redundant calculations by make greedy choice of the longest.

For any locally longest substring (x, l) that's eligible, we're processing
it with O(l²) with complexity, where x = 'a', 'b', ..., 'z', and l is the length.

And since we can only keep track of the maximum length, so
given substring y = (x, l), we have f(x) = max(f(x), l), where f is the function
storing maximum length of string starting with x.
What is more, we can also infer that:
    f(x + i) = max(f(x + i), l - i), i = 0, 1, ..., 25
where we are only processing the longest substring we can find.

With such state transition relation, the string (x, l) only needs to be scanned once.

Complexity: O(n), O(1)

5. Dynamic programming - track state of maximum length ending here

In the above method, the state update is done with two passes.

The core idea to implicitly represent a string with tuple,
 string: (starting character, length).

To eliminate redundant calculations, track the state (starting character, max length)
will suffice.

Then it's possible to update such state in one pass.

Define state:
(maximum length of string starting here, string occurrence hash table)

################################################################################
FOLLOW UP
1. For the state transition method to find locally longest substring in s, there
must be no duplicate characters in the minimal repeating sequence "ab...z".
What if s is wraparound of string "abcdacde"? There are duplicate characters now.

TODO:

"""

from collections import defaultdict

class Solution:
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        # result = self._findSubstringInWraproundStringTupleRepresentation(p)
        # result = self._findSubstringInWraproundStringTupleRepresentationTrackingMaxLength(p)
        # result = self._findSubstringInWraproundStringTupleRepresentationStateTransition(p)
        result = self._findSubstringInWraproundStringTupleRepresentationDynamicProgramming(p)

        print(p, " => ", result)

        return result

    def _findSubstringInWraproundStringTupleRepresentation(self, p):
        # FIXME: Time limit exceeded
        def nextChar(c):
            return chr(ord('a') + (ord(c) - ord('a') + 1) % 26)

        result = 0
        visited = defaultdict(set)
        i, j = 0, 1
        for i in range(len(p)):
            j = i + 1
            while j < len(p) and p[j] == nextChar(p[j - 1]):
                visited[p[i]].add(j - i) # add current length
                j += 1 # update end pointer
            visited[p[i]].add(j - i) # update length

        # print(visited)
        for c in visited:
            result += len(visited[c])

        return result

    def _findSubstringInWraproundStringTupleRepresentationTrackingMaxLength(self, p):
        """
        Instead of tracking actual tuples, just track the maximum length
        of substring beginning with each character.
        """
        # FIXME: Time limit exceeded
        def nextChar(c):
            return chr(ord('a') + (ord(c) - ord('a') + 1) % 26)

        result = 0
        visited = defaultdict(lambda : 0)
        # visited = {}
        i, j = 0, 1
        for i in range(len(p)):
            j = i + 1
            while j < len(p) and p[j] == nextChar(p[j - 1]):
                j += 1 # update end pointer
            visited[p[i]] = max(visited[p[i]], j - i)

        # print(visited)
        for c in visited:
            result += visited[c]

        return result

    def _findSubstringInWraproundStringTupleRepresentationStateTransition(self, p):
        """
        The above methods actually exhaust all possible substrings, of O(n²).

        Duplicate calculations can be eliminated making use state transition
        between characters.

        When a locally longest substring (x, l) is found, it means
        (x + 1, l - 1) is also found too!

        """
        # FIXED: Time limit exceeded
        def nextChar(c):
            return chr(ord('a') + (ord(c) - ord('a') + 1) % 26)

        result = 0
        visited = defaultdict(lambda: 0) # character to maximum length of substring starting with it
        i, j = 0, 0

        while j < len(p): # linear two pointers scan
            i = j
            j = i + 1
            while j < len(p) and p[j] == nextChar(p[j - 1]): # eligible substring so far
                j += 1 # update end pointer

            l = j - i
            for k in range(min(l, 26)):
                visited[p[i + k]] = max(visited[p[i + k]], l - k) # update maximum length

        for c in visited:
            result += visited[c]

        return result

    # TODO: follow up, element repeating sequence has duplicate characters

    # DONE: dynamic programming solution
    def _findSubstringInWraproundStringTupleRepresentationDynamicProgramming(self, p):
        visited = defaultdict(lambda: 0) # character to maximum length of string starting with it
        result = 0

        l = 0 # track state: maximum string length starting here.
        for i in range(len(p) - 1, -1, -1):
            if i == len(p) - 1 or (ord(p[i + 1]) - ord(p[i]))  % 26 == 1:
                l += 1
            else:
                l = 1
            visited[p[i]] = max(visited[p[i]], l)
        for c, in visited:
            result += visited[c]

        return result

def test():
    solution = Solution()

    assert solution.findSubstringInWraproundString("") == 0
    assert solution.findSubstringInWraproundString("a") == 1
    assert solution.findSubstringInWraproundString("z") == 1
    assert solution.findSubstringInWraproundString("cac") == 2
    assert solution.findSubstringInWraproundString("zab") == 6
    assert solution.findSubstringInWraproundString("zabc") == 10
    assert solution.findSubstringInWraproundString("zabcdcdefg") == 27
    assert solution.findSubstringInWraproundString("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 36179

    print("self test passed")

if __name__ == '__main__':
    test()
