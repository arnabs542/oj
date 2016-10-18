#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

===================================================================================================
SOLUTION:
    For SHORTEST PATH, we may consider BFS(breadth-first search).
    Use hash table to store the graph implicitly, instead of explicitly
constructing the graph with in O(V*V) time complexity.

Python tips:
  Us chr, ord to convert character and unicode integer back and forth.
'''

class Solution(object):

    def __init__(self):
        self.max_distanceFront = None
        self.max_distanceBack = None
        self.max_distanceFull = None
        self.paths = []

    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        if not isinstance(wordlist, set):
            print('converting wordlist as a set, size', len(wordlist))
            wordlist = set(wordlist)
        # length = self.ladderLengthBiBFS(beginWord, endWord, wordlist)

        # paths =  self.findLaddersDFS(beginWord, endWord, wordlist, length)
        # paths = self.findLaddersStorePaths(beginWord, endWord, wordlist)
        paths = self.findLaddersBFS(beginWord, endWord, wordlist)
        # paths = self.findLaddersBFSStorePaths(beginWord, endWord, wordlist)
        return list(paths)

    def neighbors(self, word, wordList):
        l = len(word)
        for i in range(l):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                neighbor = word[:i] + c + word[i + 1:]
                if neighbor != word and neighbor in wordList:
                    yield neighbor

    def findLaddersBFS(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: set[str]?
        :rtype: int

        """
        # TODO(done): breadth first search with predecessors list
        wordList.add(endWord)

        distance = {}
        predecessors = {}
        queue = list()

        queue.append(beginWord)
        distance[beginWord] = 1
        length = 0

        while queue:
            # POP
            word = queue.pop(0)
            if word == endWord:
                # new solution found
                if not length:
                    length = distance[word]
                    print('Shortest distance is: ', length)
                continue
            # search depth limit exceeded
            if length and distance[word] >= length:
                # continue
                break
            # explore neighbors
            for neighbor in self.neighbors(word, wordList):
                # unexplored or only explored by siblings
                if neighbor not in distance or distance[
                        neighbor] > distance[word]:
                    if neighbor not in distance:
                        # XXX(done): only PUSH into the Queue when not explored
                        queue.append(neighbor)
                        predecessors.setdefault(neighbor, [])
                        distance[neighbor] = distance[word] + 1

                    # update predecessors list and distance
                    if distance[word] + 1 < distance[neighbor]:
                        # not used for this graph
                        print('A general graph BFS case, not supposed to occur here')
                        predecessors[neighbor] = [word]
                        distance[neighbor] = distance[word] + 1
                    else:
                        # XXX(done): keep predecessors list to track all paths
                        predecessors[neighbor].append(word)

        # generate paths
        def generate(word, predecessors, path, paths):
            path.insert(0, word)
            if not predecessors.get(word):
                if path:
                    paths.append(path)
            else:
                for p in predecessors[word]:
                    path_new = list(path)
                    generate(p, predecessors, path_new, paths)

        paths = []
        if length:
            generate(endWord, predecessors, [], paths)
        print(len(paths), 'paths')

        yield from paths

    def ladderLengthBiBFS(self, beginWord: str,
                          endWord: str, wordList: set) -> int:
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: set[str] or list[str]?
        :rtype: int

        Bidirectional breadth-first search.
        Assume branching factor is b, then bidirectional search
        reduces time complexity from O(b^d) to O(b^(d/2)) by reducing the SEARCH DEPTH.

        """
        # TODO: bidirectional breadth-first search

    def findLaddersDFS(self, beginWord, endWord, wordlist, max_steps):
        # TODO: time limit exceeded without pruning
        stack = [beginWord]
        color = {beginWord: 'grey'}
        wordlist.add(endWord)
        predecessors = []

        while stack:
            # LIFO from STACK
            word = stack[-1]
            print(len(predecessors), word, len(stack), color[word])
            if word == endWord:
                yield list(predecessors) + [word]
                stack.pop()
                del color[word]
                continue
            if color.get(word) != 'black' and \
               len(predecessors) + 1 < min(max_steps, 10):
                for neighbor in self.neighbors(word, wordlist):
                    # print('neighbor ', neighbor)
                    if neighbor not in color:
                        stack.append(neighbor)
                        # explored itself but not its neighbors yet
                        color[neighbor] = 'grey'
                color[word] = 'black'  # explored itself and its neighbors
                predecessors.append(word)
            else:
                stack.pop()
                if color.get(word) == 'black':
                    predecessors.pop()
                del color[word]

    def findLaddersStorePaths(self, start, end, wordList):
        res = []
        path = []
        if start == end:
            path.append(end)
            res.append(path)
            return res
        wordList.add(start)
        wordList.add(end)
        edge = {}
        for word in wordList:
            edge[word] = []
        for word in wordList:
            for i in range(len(word)):
                for c in range(ord(word[i]) + 1, 123):
                    nw = word[:i] + chr(c) + word[i + 1:]
                    if nw in wordList:
                        edge[word].append(nw)
                        edge[nw].append(word)
        queue = [[start]]
        flag = 0
        delete = set([start])
        size = 1
        add = []
        while len(queue):
            words = queue.pop(0)
            if flag and len(words) >= flag:
                break
            if len(words) > size:
                size = len(words)
                delete |= set(add)
                add = []
            word = words[-1]
            for nw in edge[word]:
                if nw == end:
                    flag = len(words) + 1
                    res.append(words + [nw])
                if nw not in delete:
                    queue.append(words + [nw])
                    add.append(nw)
        return res

    def findLaddersBFSStorePaths(self, beginWord, endWord, wordList):
        # TODO: breadth first search with paths stored
        wordList.add(endWord)

        distance = {}
        queue = list()

        # store paths instead of nodes in the queue
        queue.append([beginWord])
        distance[beginWord] = 1
        length = 0
        paths = []

        while queue:
            words = queue.pop(0)
            word = words[-1]
            if word == endWord:
                # new solution found
                if not length:
                    length = len(words)
                    print('Shortest distance is: ', length)
                paths.append(words)
                continue
            # search depth limit exceeded
            if length and distance[word] >= length:
                print('depth limit exceeded')
                # break
                continue
            # explore neighbors
            for neighbor in self.neighbors(word, wordList):
                if neighbor not in distance or distance[
                        neighbor] > distance[word]:
                    # PUSH into the Queue
                    queue.append(words + [neighbor])
                    distance[neighbor] = distance[word] + 1
                pass
        pass

        return paths

def test():
    import json
    with open('./wordLadder.json', 'r') as f:
        params = json.load(f)
    solution = Solution()
    for param in params[:]:
        print(solution.findLadders(
            param['beginWord'], param['endWord'], set(param['wordList'])
        ))
    pass

if __name__ == '__main__':
    test()
