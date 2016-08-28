'''
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

===================================================
1. Dynamic Programming solution
    STATE TRANSITION: breakable[j] = 1(exists such i that s[i-1:j] is in dictionary) * breakable[i],
        where i, j indicates the ith, jth character in string s.
'''
class Solution(object):

    def wordBreakDPNaive(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]

        FIXEME: This is a naive dynamic programming solution:
            Storing partial solutions during the recursive state transition process
        Parts that can be optimized:
            1. PRUNE: First check whether a sentence is possible to break. If not, then just return []
            2. Don't store partial solutions at all, use backtracking!
        """
        n = len(s)
        # index to list of string composed of words separated by space
        tokens = [[] for i in range(n)]
        # sentence end index
        for j in range(1, n + 1):
            # last break word point
            for i in range(j, 0, -1):
                if s[i - 1:j] in wordDict:
                    # no breaking previously
                    if i == 1:
                        # store partial solution
                        tokens[j - 1].append(s[i - 1: j])
                    # sentence end with (i - 1)th character is breakable
                    elif tokens[i - 2]:
                        for sentence in tokens[i - 2]:
                            tokens[j - 1].append(
                                '{} {}'.format(sentence, s[i - 1:j]))
        return tokens[-1]

    def _canBreak(self, s, wordDict):
        """
        Returns whether the sentence s can be broken with dictionary wordDict. (Problem in Word Break).

        Algorithm: DYNAMIC PROGRAMMING
            A sentence s[:j] is able to break if and only if there exists a such index i(0<=i<=j) that
            the word s[i - 1: j] is in the dictionary and the sentence s[:i - 1] is able to break.
        """
        n = len(s)
        # transition[i] indicates whether string s ending with ith element
        # can be broken into the dictionary
        transition = [False for i in range(n + 1)]
        # padding, so that in the case when index is 0 the RECURSION FORMULA still stands
        transition[0] = True
        for j in range(1, n + 1, 1):
            for i in range(1, j + 1):
                if transition[i -1] and s[i - 1:j] in wordDict:
                    transition[j] = True
                    break

        return transition[n]

    def wordBreakDPPrune(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]

        This is a naive dynamic programming solution:
            Storing partial solutions during the recursive state transition process
        Parts that can be optimized:
            1. First check whether a sentence is possible to break. If not, then just return []
            2. Don't store partial solutions at all, use backtracking!
        """
        if not self._canBreak(s, wordDict):
            return []
        n = len(s)
        # index to list of string composed of words separated by space
        tokens = [[] for i in range(n)]
        # sentence end index
        for j in range(1, n + 1):
            # last word break index
            # i.e. the last breakable sub-string's ending index, starting with 0
            for i in range(j, 0, -1):
                if s[i - 1:j] in wordDict:
                    # no breaking previously
                    if i == 1:
                        # store partial solution
                        tokens[j - 1].append(s[i - 1: j])
                    # sentence end with (i - 1)th character is breakable
                    elif tokens[i - 2]:
                        for sentence in tokens[i - 2]:
                            tokens[j - 1].append(
                                '{} {}'.format(sentence, s[i - 1:j]))
        return tokens[-1]

    def wordBreakDPBacktrack(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]

        This is a dynamic programming with backtracking solution:
            Instead of storing partial solutions during the recursive state transition process, but
            store only maintain a transition table during the transition process, and backtrack to generate
            the solutions.
        """
        n = len(s)
        # XXX: boundary condition 1 - empty wordDict
        if not wordDict:
            solutions = []
            print(solutions)
            return solutions
        # the maximum word length in the dictionary
        # m = n
        # XXX: boundary condition 2 - sentence shorter than word's maximum length
        m = min(n, max(map(lambda word: len(word), wordDict)))
        # the last breakable sub-string's ending index, starting with 0
        dp = [[] for i in range(n)]
        # sentence's end index, starting with 1
        for j in range(0, n):
            # last word's begin index, starting with 1, in the sentence
            for i in range(j, j - m, -1):
                if s[i:j + 1] in wordDict and (i == 0 or dp[i - 1]):
                    dp[j].append(i - 1)

        # TODO: backtrack to generate solutions. DONE
        # TODO: do it iteratively
        def generate(dp, solutions, end, curr=[]):
            for last_index in dp[end]:
                curr_new = list(curr)
                curr_new.insert(0, s[last_index + 1:end + 1])
                if last_index >= 0:
                    generate(dp, solutions, last_index, curr_new)
                else:
                    breaked_sentence = ' '.join(curr_new)
                    # print('generated a solution: ', breaked_sentence)
                    solutions.append(breaked_sentence)
                # print(s[last_index + 1:end + 1], '     ')
            pass
        # print(dp)
        solutions = []
        generate(dp, solutions, len(s) - 1, [])
        return solutions

    def wordBreakDFS(self, b, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]

        This is a depth-first searching solution:
        """
        # TODO: DFS
        pass

    def wordBreakDFS(self, b, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]

        This is a depth-first searching solution:
        """
        # TODO: DFS
        pass

    def wordBreakBFS(self, b, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]

        This is a breadth-first searching solution:
        """
        # TODO: BFS
        pass

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        # solutions =  self.wordBreakDPNaive(s, wordDict)
        solutions = self.wordBreakDPPrune(s, wordDict)
        # solutions = self.wordBreakDPBacktrack(s, wordDict)
        print(solutions)
        return solutions

def test():
    Solution().wordBreak("leetcode", {"leet", "code", "oj"})  # True
    Solution().wordBreak("hellohalloworld",
                         {"hello", "worl", "world"})  # False
    Solution().wordBreak("catsanddog",
                         {"cat", "cats", "and", 'sand', 'dog'})  # True
    Solution().wordBreak("南京市长江大桥",
                         {"南京", '市', "南京市", "市长", "长江", "大桥", "江大桥", '长江大桥'})  # True
    Solution().wordBreak(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"])  # False
    Solution().wordBreak('a', [])
    Solution().wordBreak('bb', ["a","b","bbb","bbbb"])
    # NOTE: this case's solutions size is astronomical!
    # (6,
    # Solution().wordBreak(
    # "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    # ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", 'b', 'ab', 'aab', 'ba', 'baa']))  # True

    # Solution().wordBreak(
        # "aaaaabaaaaaaaaaaaaaaaa",
        # ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", 'b', 'ab', 'aab', 'ba', 'baa'])  # True

if __name__ == "__main__":
    test()
