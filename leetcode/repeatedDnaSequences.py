#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
187. Repeated DNA Sequences
Medium

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].

================================================================================
SOLUTION

1. Brute force
There are O(n²) substrings in total. But, since the required substring has
fixed length of 10, so all eligible substrings will be only O(n).

We can check for repeating for every possible substring.

For each subarray, of length 10, check existence in the rest of the string.

Complexity: O(n²), O(1)

2. HASH TABLE FOR DUPLICATE CHECK.
Use a hash table to trade time for space.

There are at most O(N) subarray with fixed length. Then we can exhaust them
and add them into a hash table, if same substring has already been added,
then we check whether the indices are overlapping. If there is no overlapping,
then we found one. If overlapping, we can make greedy decision to keep the
one with smaller starting index.

Complexity: O(N), O(N)

3. Bit optimization?
No need to store count, only three states:
substring never seen before, seen once, seen more than once.

Then 2 bits will do: 2² = 4 > 3.

"""

class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = self._findRepeatedDnaSequencesHash(s)

        print(s, " => ", result)

        return result

    def _findRepeatedDnaSequencesHash(self, s):
        result = []
        count = {}
        for i in range(len(s) - 9):
            j = i + 9
            sequence = s[i:j + 1]
            if sequence not in count:
                count[sequence] = 1
            # elif count[sequence] + 9 < i:
            else:
            # XXX: doesn't have to non-overlapping?
                if count[sequence] == 1:
                    result.append(sequence)
                count[sequence] += 1

        return result

    # TODO: bit optimization

def test():
    solution = Solution()

    assert solution.findRepeatedDnaSequences("") == []
    assert solution.findRepeatedDnaSequences("AAAAAAAAAA") == []
    assert solution.findRepeatedDnaSequences("AAAAAAAAAAA") == ["AAAAAAAAAA"]
    assert solution.findRepeatedDnaSequences("AAAAAAAAAAAAAAAAAAAA") == ["AAAAAAAAAA"]
    assert solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT") == ["AAAAACCCCC", "CCCCCAAAAA"]

    print("self test passed")

if __name__ == "__main__":
    test()
