'''
Word Break

Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
'''


class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean

    def wordBreak(self, s, dic):
        n = len(s)
        # transition[i] indicates whether string s ending with ith element
        # can be broken into the dictionary
        transition = [False for i in xrange(n + 1)]
        transition[0] = True
        for j in xrange(1, n + 1, 1):
            for i in xrange(1, j + 1):
                if transition[i - 1] and s[i - 1:j] in dic:
                    transition[j] = True
                    break

        return transition[n]

if __name__ == "__main__":
    print Solution().wordBreak("leetcode", {"leet", "code", "oj"})
    print Solution().wordBreak("hellohalloworld", {"hello", "worl", "world"})
