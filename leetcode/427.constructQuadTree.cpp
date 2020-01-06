/**
 *
 *
427. Construct Quad Tree
Medium

We want to use quad trees to store an N x N boolean grid. Each cell in the grid can only be true or false. The root node represents the whole grid. For each node, it will be subdivided into four children nodes until the values in the region it represents are all the same.

Each node has another two boolean attributes : isLeaf and val. isLeaf is true if and only if the node is a leaf node. The val attribute for a leaf node contains the value of the region it represents.

Your task is to use a quad tree to represent a given grid. The following example may help you understand the problem better:

Given the 8 x 8 grid below, we want to construct the corresponding quad tree:



It can be divided according to the definition above:

(see ./962_grid_divided_1.png)




The corresponding quad tree should be as following, where each node is represented as a (isLeaf, val) pair.

For the non-leaf nodes, val can be arbitrary, so it is represented as *.

(see ./962_quad_tree.png)


Note:

N is less than 1000 and guaranteened to be a power of 2.
If you want to know more about the quad tree, you can refer to its wiki.

 */

/*
// Definition for a QuadTree node.
class Node {
public:
    bool val;
    bool isLeaf;
    Node* topLeft;
    Node* topRight;
    Node* bottomLeft;
    Node* bottomRight;

    Node() {}

    Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node* _bottomLeft, Node* _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
};


SOLUTION
================================================================================

This is a tree structure illustrating recursive property(dfs).
The problem is, how to check leaf efficiently?

1. Prefix sum array!

Yes, we can build a 2D prefix sum array to check where a square region is all 0s
or all 1s.

Complexity: O(n^2).

2. Direct recursive leaf checking
A node is leaf, if and only if its all children are leaf and have same value, if
this node is split as if it isn't a leaf node.

Complexity: O(n^2)

*/

#include <debug.hpp>

class Node {
public:
    bool val;
    bool isLeaf;
    Node* topLeft;
    Node* topRight;
    Node* bottomLeft;
    Node* bottomRight;

    Node() {}

    Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node* _bottomLeft, Node* _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
};

class Solution {
public:
    Node* construct(vector<vector<int>>& grid) {
        int n = grid.size();
        //assert((n & n - 1) == 0); // power of 2

        Node *root = dfs(grid, 0, 0, n - 1, n - 1); // top left, bottom right

        return root;
    }

    // TODO: parameters can be reduced to (x1, y1, width=height)
    Node* dfs(const vector<vector<int>> &grid, int x1, int y1, int x2, int y2) {
        // base case
        Node *pNode;
        if (x1 > x2) return NULL;
        if (x1 == x2 && y1 == y2) {
            pNode = new Node(grid[x1][y1], true, NULL, NULL, NULL, NULL);
            return pNode;
        }
        pNode = new Node(false, false, NULL, NULL, NULL, NULL);
        int x0 = (x1 + x2)/2;
        int y0 = (y1 + y2)/2;
        bool value = grid[x1][y1];
        // recursive
        pNode->topLeft = dfs(grid, x1, y1, x0, y0);
        pNode->topRight = dfs(grid, x1, y0 + 1, x0, y2);
        pNode->bottomLeft = dfs(grid, x0 + 1, y1, x2, y0);
        pNode->bottomRight = dfs(grid, x0 + 1, y0 + 1, x2, y2);
        if (pNode->topLeft->isLeaf && pNode->topRight->isLeaf
                && pNode->bottomLeft->isLeaf && pNode->bottomRight->isLeaf
                && pNode->topLeft->val == value && pNode->topRight->val == value
                && pNode->bottomLeft->val == value && pNode->bottomRight->val == value
                ) {
            pNode->val = value;
            pNode->isLeaf = true;
            delete pNode->topLeft; pNode->topLeft = NULL;
            delete pNode->topRight; pNode->topRight = NULL;
            delete pNode->bottomLeft; pNode->bottomLeft = NULL;
            delete pNode->bottomRight; pNode->bottomRight = NULL;
        }

        return pNode;
    }
};

int main(int argc, char *argv[])
{
    Solution solution;
    vector<vector<int>> input;

    input = {};
    assert(solution.construct(input) == NULL);

    input = {{0}};
    assert(!solution.construct(input)->val);

    input = {{1}};
    assert(solution.construct(input)->isLeaf);

    input = {{1,1}, {1,1}};
    assert(solution.construct(input)->isLeaf);

    input = {{0,1},{1,0}};
    assert(!solution.construct(input)->isLeaf);

    input = {{1,1,1,1,0,0,0,0},{1,1,1,1,0,0,0,0},{1,1,1,1,1,1,1,1},{1,1,1,1,1,1,1,1},{1,1,1,1,0,0,0,0},{1,1,1,1,0,0,0,0},{1,1,1,1,0,0,0,0},{1,1,1,1,0,0,0,0}};
    assert(solution.construct(input)->topLeft->val);

    cout << "self test passed" << endl;

    return 0;
}
