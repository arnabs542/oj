'''
127. Word Ladder

Total Accepted: 93607
Total Submissions: 481100
Difficulty: Medium

Given two words (beginWord and endWord), and a dictionary's word list, find the
length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.


===================================================================================================
SOLUTION:
    This is a SHORTEST PATH problem in Graph theory. If the Edit Distance
between two words is the distance between two vertices representing them.
    For SHORTEST PATH problem, we have BREADTH-FIRST SEARCH problem.
    Naively, we can build the graph with time complexity of O(|V|*|V|),
and do a BFS in O(|V|+|E|).This implementation will fail the big data test. To
optimize the code,we can get around the graph building process:
    We IMPLICITLY REPRESENT the graph by storing vertices in a HASH TABLE(set), thus
retrieving them in constant time. Initially,we push the start word into the queue.
While BREADTH-FIRST searching, do change one character each time with a word, and
check if it's in the dictionary.If it's in,then we push it into a queue, updating
its search depth. Then we can find the shortest path in O(|V| * L * 26). L is the
words' length.

    Optimization:
        1) preprocess word to use 'h_t' to match 'hot', 'hit' and so on, reducing the
neighbors finding time complexity from O(26) to O(1).
        2) Bidirectional BFS. Assume branching factor is b, then bidirectional search
reduces time complexity from O(b^d) to O(b^(d/2)) by reducing the SEARCH DEPTH.

'''

class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: set[str] or list[str]?
        :rtype: int
        """
        # return self.ladderLengthBFS(beginWord, endWord, wordList)
        return self.ladderLengthBiBFS(beginWord, endWord, wordList)

    def neighbors(self, word, wordList):
        l = len(word)
        for i in range(l):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                # for j in range(26):
                # neighbor = ''.join(map(
                    # lambda t: chr(ord('a') + j) if t[0] == i else t[1],
                    # enumerate(word)))
                neighbor = word[:i] + c + word[i + 1:]
                if neighbor != word and neighbor in wordList:
                    yield neighbor

    def ladderLengthBFS(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: set[str]?
        :rtype: int

        662ms,
        """
        depth = {}
        queue = list()
        queue.append(beginWord)
        depth[beginWord] = 1
        # XXX(done): to reduce the neighbor query time complexity to O(26)*O(1)
        if not isinstance(wordList, set):
            print('converting wordList as a set, size', len(wordList))
            wordList = set(wordList)
        wordList.add(endWord)

        while queue:
            word = queue.pop(0)
            # print('depth {}, depth: {}'.format(word, depth[word]))
            if word == endWord:
                return depth[word]
            for neighbor in self.neighbors(word, wordList):
                if neighbor in wordList and neighbor not in depth:
                    # print('visiting {}'.format(neighbor))
                    queue.append(neighbor)
                    depth[neighbor] = depth[word] + 1

        return 0

    def ladderLengthBiBFS(self, beginWord: str, endWord: str, wordList: set) -> int:
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: set[str] or list[str]?
        :rtype: int

        For this BFS on this problem, we don't need to track the path, so we don't have to
        track the PREDECESSORS or the COLOR while traversing the graph. Keeping track of
        the DISTANCE will do.

        Bidirectional breadth-first search.
        Assume branching factor is b, then bidirectional search
        reduces time complexity from O(b^d) to O(b^(d/2)) by reducing the SEARCH DEPTH.

        159ms, 83.67%
        """
        # TODO: bidirectional breadth-first search
        if beginWord == endWord:
            return 1
        length = 0

        front, back = [beginWord], [endWord]
        frontDistance, backDistance = dict(), dict()

        frontDistance[beginWord] = 1
        backDistance[endWord] = 1

        def explore(queue, visited, visited2):
            word = queue.pop(0)
            for neighbor in self.neighbors(word, wordList):
                if neighbor in wordList and neighbor not in visited:
                    if neighbor in visited2:
                        return visited[word] + visited2[neighbor]
                    else:
                        queue.append(neighbor)
                        visited[neighbor] = visited[word] + 1
            return 0

        while front and back:
            length = explore(front, frontDistance, backDistance)
            if not length:
                length = explore(back, backDistance, frontDistance)
            if length:
                break

        print('length ', length)
        return length

    def ladderLengthBiBFSPreprocess(self, beginWord: str, endWord: str, wordList: set) -> int:
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: set[str] or list[str]?
        :rtype: int

        Bidirectional breadth-first search, with preprocessing the input wordList

        """
        # TODO: preprocess to use 'h_t' like words to represent words with a ladder


def test():
    import json
    with open('./wordLadder.json', 'r') as f:
        params = json.load(f)
    solution = Solution()
    assert solution.ladderLength(
        '', '', set([])) == 1
    assert solution.ladderLength(
        'a', 'c', set(['a', 'b', 'c'])) == 2
    assert solution.ladderLength(
        'hit', 'cog',
        set(["hot", "dot", "dog", "lot", "log"])) == 5
    for param in params:
        length = solution.ladderLength(
            param['beginWord'], param['endWord'], set(param['wordList']))
        print('testing result: ', param.keys(), length)
        assert length == int(param['length'])

    print('self test passed!')

if __name__ == '__main__':
    test()
