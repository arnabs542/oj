'''
Word Break

Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

=================================================================

Method 1:
    Dynamic Programming
    Algorithm: DYNAMIC PROGRAMMING
        A sentence s[:j] is able to break if and only if there exists a such index i(0<=i<=j) that
        the word s[i - 1: j] is in the dictionary and the sentence s[:i - 1] is able to break.
    State transition: breakable[j] = 1(exists such i that s[i-1:j] is in dictionary) * breakable[i],
        where i, j indicates the ith, jth character in string s.
'''


class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean

    def wordBreak(self, s, dic):
        n = len(s)
        # transition[i] indicates whether string s ending with ith element
        # can be broken into the dictionary
        transition = [False for i in range(n + 1)]
        # padding, so that in the case when index is 0 the RECURSION FORMULA still stands
        transition[0] = True
        for j in range(1, n + 1, 1):
            for i in range(1, j + 1):
                if transition[i -1] and s[i - 1:j] in dic:
                    transition[j] = True
                    break

        return transition[n]

def test():
    assert Solution().wordBreak("leetcode", {"leet", "code", "oj"}) # True
    assert not Solution().wordBreak("hellohalloworld", {"hello", "worl", "world"}) # False
    assert not Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                              ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]) # False
    assert Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                              ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa", 'b', 'ab', 'aab', 'ba', 'baa'])

if __name__ == "__main__":
    test()
    print('Accepted')
