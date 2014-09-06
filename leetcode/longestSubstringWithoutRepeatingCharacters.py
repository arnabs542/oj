# -*- encoding:utf-8 -*-
'''
Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

'''


class Solution:
    # @return an integer

    def lengthOfLongestSubstring(self, s):
        n = len(s)
        length = [1 for i in xrange(n)]
        max_len = 1
        end = 0
        for i in xrange(1, n):
            for j in range(1, length[i - 1] + 1, 1):
                if s[i - j] == s[i]:
                    length[i] = j
                    break
            if j == length[i - 1] and s[i - j] != s[i]:
                length[i] = j + 1
                if max_len < length[i]:
                    max_len = length[i]
                    end = i

        # print s[end - max_len + 1:end + 1]
        return max_len

if __name__ == "__main__":
    print Solution().lengthOfLongestSubstring("abcabcbb")
