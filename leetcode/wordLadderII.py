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

        # paths =  self.findLaddersDFS(beginWord, endWord, wordlist, length)
        # paths = self.findLaddersStorePaths(beginWord, endWord, wordlist)
        # paths = self.findLaddersBFS(beginWord, endWord, wordlist)
        # paths = self.findLaddersBFSStorePaths(beginWord, endWord, wordlist)
        paths = self.findLaddersBiBFS(beginWord, endWord, wordlist)
        return list(paths)

    def _neighbors(self, word, wordList):
        l = len(word)
        for i in range(l):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                neighbor = word[:i] + c + word[i + 1:]
                if neighbor != word and neighbor in wordList:
                    yield neighbor

    def _constructPaths(self, endWord, predecessors, path, paths, beginWord=None, depth=0):
        # generate paths in DFS approach
        path.insert(0, endWord)
        if not predecessors.get(endWord) and path:
            if (depth and len(path) > depth) or (beginWord and beginWord != path[0]):
                return
            paths.append(path)
        else:
            for p in predecessors[endWord]:
                path_new = list(path)
                self._constructPaths(p, predecessors, path_new, paths, beginWord, depth)

    def findLaddersBFS(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: set[str]?
        :rtype: int

        618ms
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
            for neighbor in self._neighbors(word, wordList):
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

        paths = []
        if length:
            self._constructPaths(endWord, predecessors, [], paths)
        print(len(paths), 'paths')

        yield from paths

    def findLaddersBiBFS(self, beginWord: str,
                          endWord: str, wordList: set) -> int:
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: set[str] or list[str]?
        :rtype: int

            Bidirectional(two-end) breadth-first search.
        Assume branching factor is b, then bidirectional search reduces time complexity from
        O(b^d) to O(b^(d/2)) by reducing the SEARCH DEPTH.

            For bidirectional search, we have to maintain two FRONTIERS. In this scenario, we
        have to find the shortest paths, which means the depths of nodes in each frontier must
        keep in consistency. In another word, ndoes in each frontier must be from the same level
        of the graph.
            A simple way to tackle this would be to explore all nodes in one frontier at each time
        and do the same to the other frontier next time. Given that, a trick with set data structure
        comes in handy. We can use a empty set to contain nodes with new depths and discard those
        with old depths.

        242ms: Two-end BFS
        178ms: use logic or instead of set union operation when checking element in sets.
        162ms: assign object pointers instead of copying objects
        """
        # TODO(done): bidirectional breadth-first search
        # FIXME(fixed): why would this approach give paths besides the shortest ones. And the
        # solutions are nondeterministic.
        # The nondeterminacy of solutions results in the `set` data structure's UNORDERED nature

        frontiers = [{beginWord}, {endWord}] # forward, backward frontiers
        frontier_new = set()
        predecessors = dict()
        visited = set()
        join = False
        step = 0

        while frontiers[0] and frontiers[1]:
            # choose a FRONTIER, whether forward or backward
            backward = True if len(frontiers[1]) < len(frontiers[0]) else False
            i = 1 if backward else 0
            frontier, frontier2 = frontiers[i], frontiers[1 - i]

            step += 1
            frontier_new.clear()
            # explore one frontier
            while frontier:
                # XXX: POP from FRONTIER and EXPLORE
                node = frontier.pop()
                if node in frontier2:
                    print('found solution at step', step, node)
                    join = True
                elif not join:
                    for neighbor in self._neighbors(node, wordList):
                        # XXX: explore only FORWARD edges not BACK/CROSS edges
                        if neighbor in visited or neighbor in frontier: continue
                        frontier_new.add(neighbor)
                        predecessor_key    = neighbor if not backward else node
                        predecessors_value = node if not backward else neighbor
                        predecessors.setdefault(predecessor_key, [])
                        # XXX: append predecessors list
                        predecessors[predecessor_key].append(predecessors_value)
                        pass
                # XXX: mark state EXPLORED
                visited.add(node)

            frontiers[i], frontier_new = frontier_new, frontiers[i]
            if join: break
            pass

        paths = []
        if join: self._constructPaths(endWord, predecessors, [], paths,
                                      beginWord=beginWord, depth=step)
        return paths

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
                for neighbor in self._neighbors(word, wordlist):
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
            for neighbor in self._neighbors(word, wordList):
                if neighbor not in distance or distance[
                        neighbor] > distance[word]:
                    # PUSH into the Queue
                    queue.append(words + [neighbor])
                    distance[neighbor] = distance[word] + 1
                pass

        return paths

def test():
    import json
    with open('./wordLadder.json', 'r') as f:
        params = json.load(f)
    solution = Solution()
    for param in params[:]:
        paths = solution.findLadders(
            param['beginWord'], param['endWord'], set(param['wordList']))
        print(paths, '\n')
        # assert len(paths) == param['length']
    pass

if __name__ == '__main__':
    test()
