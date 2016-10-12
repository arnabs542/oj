'''
126. Word Ladder II

Total Accepted: 53418
Total Submissions: 390397
Difficulty: Hard

Given two words (beginWord and endWord), and a dictionary's word list, find all
shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
All words have the same length.
All words contain only lowercase alphabetic characters.

SOLUTION:
    For SHORTEST PATH, we may consider BFS(breadth-first search).
    Use hash table to store the graph implicitly, instead of explicitly
constructing the graph with in O(V*V) time complexity.

Python tips:
  Us chr, ord to convert character and unicode integer back and forth.
'''

class Solution(object):

    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """

def test():
    pass

if __name__ == '__main__':
    test()
