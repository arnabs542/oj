# -*- encoding:utf-8 -*-
'''
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a
substring, "pwke" is a subsequence and not a substring.

==============================================================================================
Solution:
1. Dynamic Programming
    Use length[n] to store the length of longest substring without repeating characters of
string[0...i].
length[i] = length[i-1] + 1,if string[i] not in string[i-length[i-1]...i-1]
            j,for largest j < length[i-1] such that string[i] not in string[i-j...i-1]
O(n^2).

2. dynamic programming and hash table.
Define the state more wisely: the maximum length of eligible string so far(ending with current
element). And use hash table to store character's most recent occurrence position to check
eligibility.
O(n)

'''


class Solution:
    # @return an integer

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.lengthOfLongestSubstringDPOpt(s)

    def lengthOfLongestSubstringDP(self, s):
        '''
        Time Complexity: O(n^2)
        '''
        n = len(s)
        length = [1 for i in range(n)]
        max_so_far = 1
        end = 0
        if n == 0:
            return 0
        for i in range(1, n):
            for j in range(1, length[i - 1] + 1, 1):
                if s[i - j] == s[i]:
                    length[i] = j
                    break
            if j == length[i - 1] and s[i - j] != s[i]:
                length[i] = j + 1
                if max_so_far < length[i]:
                    max_so_far = length[i]
                    end = i

        # print s[end - max_so_far + 1:end + 1]
        return max_so_far

    def lengthOfLongestSubstringDPOpt(self, s):
        '''
        Keep a hash table to store the most recent position of characters in s, and maintain
        a variable `max_ending_here` to denote the maximum longest eligible substring length so far
        (ENDING WITH CURRENT ELEMENT).

        Scan the string from left to right, if we found the current character's previous position j
        in range of max_ending_here, then the new eligible string start with j + 1, ends with current
        position.

        time complexity: O(n)
        '''
        max_so_far, max_ending_here = 0, 0
        ch2idx = {}
        for i, _ in enumerate(s):
            if i - ch2idx.get(s[i], -1) <= max_ending_here:
                max_ending_here = i - ch2idx[s[i]]
            else:
                max_ending_here += 1
                max_so_far = max(max_so_far, max_ending_here)
            ch2idx[s[i]] = i

        return max_so_far

def test():
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring('bbbbb') == 1
    print('self test passed')

if __name__ == "__main__":
    test()
