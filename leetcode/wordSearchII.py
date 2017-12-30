#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Word Search II
Total Accepted: 28167
Total Submissions: 132837
Difficulty: Hard


Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
Note:
You may assume that all inputs are consist of lowercase letters a-z
Hint:

You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?

If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.

================================================================================
SOLUTION

1. Brute force
For each word in the dictionary, perform graph search to verify whether it exists in the board.

Complexity
O(M²N²l), where board is of size MxN, and l is the length of words list.

2. Trie - prefix tree -  dictionary problem
Perform graph search on the board, and compare the prefix against the prefix tree(trie).

Complexity
O(M²N²), where board is of size MxN, and l is the length of words list.

'''

class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        result = self._findWordsTrie(board, words)

        result.sort()

        print(board, words, 'result: ', result)

        return result

    def _findWordsTrie(self, board, words):
        class TrieNode:
            def __init__(self):
                self.children = [None for _ in range(26)]
                self.isLeaf = False
        # TODO: trie implementation can be optimized by using just dict

        # build trie
        _id = lambda c: ord(c) - ord('a')
        trie = TrieNode()
        for word in words:
            p = trie
            for c in word:
                i = _id(c)
                if p.children[i] is None:
                    p.children[i] = TrieNode()
                p = p.children[i]
            p.isLeaf = True

        result = set()
        m, n = len(board), len(board[0]) if board else 0
        if not (m*n) and "" in words: return [""] # empty board, empty string in dictionary

        # search
        visited = [[False for _ in range(n)] for _ in range(m)]
        def dfs(i, j, node, prefix):
            if node.isLeaf: # stop criteria: found a word in dictionary
                result.add(prefix)
                if len(result) == len(words): return True # found all words
            if not (0 <= i < m and 0 <= j < n): return False # out of range

            if visited[i][j]: return False # already visited
            c = board[i][j]
            p = node.children[_id(c)] if c else node # cell is empty string ""
            if p is None: return False # no match

            # recursion
            visited[i][j] = True
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if dfs(x, y, p, prefix + c): return True
            visited[i][j] = False
            return False # not all words have been found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, trie, ''): return list(result)
        return list(result) # filter duplcates

def test():
    solution = Solution()

    board = []
    words = []
    output = []

    # edge case: both empty
    assert solution.findWords([], []) == []

    # empty board, empty string
    assert solution.findWords([], [""]) == [""]
    # board of empty rows, empty string
    assert solution.findWords([[]], [""]) == [""]

    # edge case: board containing empty string?
    assert solution.findWords([[""]], [""]) == [""]
    assert solution.findWords([["a", "" , "b"]], ["", "a", "ab"]) == ["", "a", "ab"]


    # case: board size 1x1
    board = [["a"]]
    words = [""]
    output = [""]
    assert solution.findWords(board, words) == output

    board = [["a"]]
    words = ["", "a"]
    output = ["", "a"]
    assert solution.findWords(board, words) == output

    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    words = ["oath", "pea", "eat", "rain"]
    output = ["eat", "oath"]
    assert solution.findWords(board, words) == sorted(output)

    board = [
        ['a', 'b', 'c', 'e'],
        ['s', 'f', 'c', 's'],
        ['a', 'd', 'e', 'e'],
    ]
    assert solution.findWords(board, ["", 'abcced', 'see']) == ["", 'abcced', 'see']

    print("self test passed")


if __name__ == '__main__':
    test()
