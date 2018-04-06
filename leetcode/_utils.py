#!/usr/bin/env python
# -*- coding: utf-8 -*-

from _type import ListNode

def linkedList(l):
    if not l:
        return None
    head = ListNode(l[0])
    p = head
    for i in range(1, len(l)):
        node = ListNode(l[i])
        p.next = node
        p = node

    return head

def tolist(head, until=None):
    p = head
    result = []
    while p not in (None, until):
        result.append(p.val)
        p = p.next
    return result

def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    result, frontier, frontier_new = [], [root] if root else [], []
    while frontier:
        result.append([])
        while frontier:
            node = frontier.pop(0)
            print(node)
            result[-1].append(node.val)
            for child in (node.left, node.right):
                if child: frontier_new.append(child)
        frontier_new, frontier = frontier, frontier_new
    # print(result)
    return result

def deepcopy(x, cache=None):
    """
    deep copy must consider the graph connection references, which means
    cycle in graph must be resolved to avoid infinite loop.

    Then dfs(depth first search) with memoization will do the magic.
    """
    if cache is None: cache = {}
    if id(x) in cache:
        y = cache[id(x)]
    elif isinstance(x, (int, float, str)):
        y = x
    elif isinstance(x, list):
        y = cache[id(x)] = []

        for v in x:
            y.append(deepcopy(v, cache)) # dfs
    elif isinstance(x, dict):
        y = cache[id(x)] = {}

        for k, v in x.items():
            y[k] = deepcopy(v, cache) # dfs

    print("copy", x, " to: ", y)
    return y

def test():

    # shallow copy
    a = {1: 2, 2: {3: 4}}
    b = a[2]
    b[3] = 5

    assert a[2][3] == b[3] == 5

    # deep copy
    a = {1: 2, 2: {3: 4}}
    b = deepcopy(a)[2]
    b[3] = 5
    assert a[2][3] == 4
    assert b[3] == 5

    # graph: deep copy of self referencing dictionary
    # c = {'a': c, 'b': 'b'}
    a = {}
    a['a'] = a
    # b['a'] = a
    c = deepcopy(a)
    a[1] = 2
    c[1] = 3
    assert a[1] == 2
    # assert b['a'][1] == 2
    assert c[1] == 3
    # assert b['b'] == 'B'

    # graph: deep copy of self referencing dictionary
    # c = {'a': c, 'b': 'b'}
    a = {}
    b = {}
    a['b'] = b
    b['a'] = a
    c = deepcopy(a)
    a[1] = 2
    c[1] = 3
    assert a[1] == 2
    assert b['a'][1] == 2
    assert c[1] == 3
    # assert b['b'] == 'B'

    # graph: deep copy of self referencing list
    a = []
    a.append(a)
    b = deepcopy(a)
    print(a, b)

    print("self test passed!")

if __name__ == "__main__":
    test()
