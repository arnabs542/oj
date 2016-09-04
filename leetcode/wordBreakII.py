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

2. Search: depth-first search with backtracking and breadth-first search
'''
class Solution(object):

    def __init__(self):
        self.memory = {}

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
        # padding, so that in the case when index is 0 the RECURSION FORMULA
        # still stands
        transition[0] = True
        for j in range(1, n + 1, 1):
            for i in range(1, j + 1):
                if transition[i - 1] and s[i - 1:j] in wordDict:
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
        else:
            return self.wordBreakDPNaive(s, wordDict)

    def wordBreakDPBacktrack(self, s, wordDict, tailRecursion=False):
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
        # XXX: boundary condition 2 - sentence shorter than word's maximum
        # length
        m = min(n, max([len(word) for word in wordDict]))
        # the last breakable sub-string's ending index, starting with 0
        dp = [[] for i in range(n)]
        # sentence's end index, starting with 1
        for j in range(0, n):
            # last word's begin index, starting with 1, in the sentence
            for i in range(j, j - m, -1):
                if s[i:j + 1] in wordDict and (i == 0 or dp[i - 1]):
                    dp[j].append(i - 1)

        # TODO: backtrack to generate solutions. DONE. This is actually a DFS search routine
        # This is tail recursion, constructing solution at the end of the recursion by
        # passing intermediate solution along down recursive calls as function arguments
        # TODO: do it iteratively
        def generate(dp, solutions, end, curr=[]):
            for last_index in dp[end]:
                # if not instantiate a new list, we need to pop from it after
                # insert into it for DFS backtracking
                curr_new = list(curr)
                curr_new.insert(0, s[last_index + 1:end + 1])
                if last_index >= 0:
                    generate(dp, solutions, last_index, curr_new)
                else:
                    broken_sentence = ' '.join(curr_new)
                    # print('generated a solution: ', broken_sentence)
                    solutions.append(broken_sentence)
                # print(s[last_index + 1:end + 1], '     ')
            pass

        def generateNonTail(dp, solutions, end, curr=[]):
            """
                DFS backtracking generating solutions with non-tail recursion
            """
            for last_index in dp[end]:
                # if not instantiate a new list, we need to pop from it after
                # insert into it for DFS backtracking
                curr.append(s[last_index + 1:end + 1])
                if last_index >= 0:
                    generate(dp, solutions, last_index, curr)
                else:
                    broken_sentence = ' '.join(curr[::-1])
                    print('generated a solution: ', broken_sentence)
                    solutions.append(broken_sentence)
                # non tail recursion, we need to RESTORE variable STATE or construct the solution
                # at the top level call
                curr.pop()
            pass

        # print(dp)
        solutions = []
        tailRecursion and generateNonTail(dp, solutions, len(s) - 1, []) or \
                generate(dp, solutions, len(s) - 1, [])
        return solutions

    def wordBreakDFS(self, s, wordDict, start=0, cat=False, memoization=False):
        """
        :type s: str
        :type wordDict: Set[str]
        :type cat: bool, whether to concatenate list into string
        :rtype: List[str]

        This is a depth-first searching solution:
        """
        # TODO: DFS
        if not self._canBreak(s, wordDict):
            return []
        n = len(s)
        m = min(n, max([len(word) for word in wordDict]))
        # recursive DFS with memoization
        if memoization and start in self.memory:
            solutions = self.memory[start]
        else:
            solutions = []
            if s[start:] in wordDict:
                solutions.append([n - 1])
            # for i in range(start, n):
            for i in range(start, start + m):
                if s[start:i + 1] in wordDict:
                    subsolutions = self.wordBreakDFS(s, wordDict, start=i + 1)
                    solutions.extend(map(lambda sub: [i] + sub, subsolutions))

            if memoization:
                self.memory[start] = solutions

        # return integer lists or string lists
        if cat:
            def combine(solution):
                segments = map(lambda item:
                               s[solution[item[0] - 1] + 1 if item[0] else 0:
                                 solution[item[0]] + 1],
                               enumerate(solution))
                return ' '.join(segments)
            return list(map(combine, solutions))
        else:
            return solutions

    def wordBreakDFSIteration(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]

        This is a depth-first searching solution.
        Iterative depth-first search algorithm.
        """
        # TODO: DFS iteratively
        n = len(s)
        m = min(n, max([len(word) for word in wordDict]))
        pass

    def wordBreakBFS(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]

        This is a breadth-first searching solution:
        """
        # TODO: BFS
        n = len(s)
        m = min(n, max([len(word) for word in wordDict]))
        pass

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        # solutions =  self.wordBreakDPNaive(s, wordDict)
        # solutions = self.wordBreakDPPrune(s, wordDict)
        # solutions = self.wordBreakDPBacktrack(s, wordDict)
        # solutions = self.wordBreakDFS(s, wordDict, cat=True)
        solutions = self.wordBreakDFS(s, wordDict, cat=True, memoization=True)
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
    Solution().wordBreak('bb', ["a", "b", "bbb", "bbbb"])
    # NOTE: this case's solutions size is astronomical!
    # (6,
    # Solution().wordBreak(
    # "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    # ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", 'b', 'ab', 'aab', 'ba', 'baa']))  # True

    Solution().wordBreak(
        "aaaaabaaa",
        ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", 'b', 'ab', 'aab', 'ba', 'baa'])  # True

if __name__ == "__main__":
    test()
