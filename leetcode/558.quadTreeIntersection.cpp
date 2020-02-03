/**
 *
558. Quad Tree Intersection
Easy

A quadtree is a tree data in which each internal node has exactly four children: topLeft, topRight, bottomLeft and bottomRight. Quad trees are often used to partition a two-dimensional space by recursively subdividing it into four quadrants or regions.

We want to store True/False information in our quad tree. The quad tree is used to represent a N * N boolean grid. For each node, it will be subdivided into four children nodes until the values in the region it represents are all the same. Each node has another two boolean attributes : isLeaf and val. isLeaf is true if and only if the node is a leaf node. The val attribute for a leaf node contains the value of the region it represents.

For example, below are two quad trees A and B:

A:
+-------+-------+   T: true
|       |       |   F: false
|   T   |   T   |
|       |       |
+-------+-------+
|       |       |
|   F   |   F   |
|       |       |
+-------+-------+
topLeft: T
topRight: T
bottomLeft: F
bottomRight: F

B:
+-------+---+---+
|       | F | F |
|   T   +---+---+
|       | T | T |
+-------+---+---+
|       |       |
|   T   |   F   |
|       |       |
+-------+-------+
topLeft: T
topRight:
     topLeft: F
     topRight: F
     bottomLeft: T
     bottomRight: T
bottomLeft: T
bottomRight: F


Your task is to implement a function that will take two quadtrees and return a quadtree that represents the logical OR (or union) of the two trees.

A:                 B:                 C (A or B):
+-------+-------+  +-------+---+---+  +-------+-------+
|       |       |  |       | F | F |  |       |       |
|   T   |   T   |  |   T   +---+---+  |   T   |   T   |
|       |       |  |       | T | T |  |       |       |
+-------+-------+  +-------+---+---+  +-------+-------+
|       |       |  |       |       |  |       |       |
|   F   |   F   |  |   T   |   F   |  |   T   |   F   |
|       |       |  |       |       |  |       |       |
+-------+-------+  +-------+-------+  +-------+-------+
Note:

Both A and B represent grids of size N * N.
N is guaranteed to be a power of 2.
If you want to know more about the quad tree, you can refer to its wiki.
The logic OR operation is defined as this: "A or B" is true if A is true, or if B is true, or if both A and B are true.

================================================================================
SOLUTION

Return Copy or reference?

Base class is NULL, is leaf node.
But N is guaranteed to be power of 2, so no NULL.

1. Recurrence relation with recursion

Intersect(root1, root2)  {
    if root1 is leaf:
        pass
    elif root2 is leaf:
        pass
    else:
        intersect children
        see where intersection is leaf
}

Complexity: worst O(N²)

 *
 */

#include <debug.hpp>


//Definition for a QuadTree node.
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
    Node* intersect(Node* quadTree1, Node* quadTree2) {

    }

    Node *intersectDfs(Node *root1, Node *root2) {
        //Node* root1 = quadTree1, *root2 = quadTree2;
        auto newNode = []() {
            Node *pNode = new Node();
            pNode->isLeaf = pNode->val = false;
            pNode->topLeft = pNode->topRight = pNode->bottomLeft = pNode->bottomRight = NULL;
            return pNode;
        };
        Node *root = NULL;
        //root = new Node();
        if (!root1) {
            if (!root2) return NULL;
            root = newNode();
            *root = *root2; // XXX: default copy constructor?
            if (!root->isLeaf) {
                root->topLeft = intersect(NULL, root2->topLeft);
                root->topRight = intersect(NULL, root2->topRight);
                root->bottomLeft = intersect(NULL, root2->bottomLeft);
                root->bottomRight = intersect(NULL, root2->bottomRight);
            }
            //{
                //root->isLeaf = root2->isLeaf; // XXX: ?
                //root->val = root2->val;
            //}
            return root;
        } else if (!root2) {
            swap(root1, root2);
            return intersect(root1, root2);
        }

        if (root1->isLeaf) {
            root = newNode();
            if (root1->val) {
                root->isLeaf = true;
                root->val = true;
            } else {
                // copy root2
                root->val = root2->val;
                root->isLeaf = root2->isLeaf;
                root->topLeft = intersect(root1, root2->topLeft);
                root->topRight = intersect(root1, root2->topRight);
                root->bottomLeft = intersect(root1, root2->bottomLeft);
                root->bottomRight = intersect(root1, root2->bottomRight);
            }
        } else if (root2->isLeaf) {
            swap(root1, root2);
            root = intersect(root1, root2);
        } else {
            // recursive case
            root = newNode();
            root->topLeft = intersect(root1->topLeft, root2->topLeft);
            root->topRight = intersect(root1->topRight, root2->topRight);
            root->bottomLeft = intersect(root1->bottomLeft, root2->bottomLeft);
            root->bottomRight = intersect(root1->bottomRight, root2->bottomRight);
            if (root->topLeft->isLeaf & root->topRight->isLeaf && root->bottomLeft->isLeaf && root->bottomLeft->isLeaf) {
                if (root->topLeft->val ==  root->topRight->val && root->bottomLeft->val == root->bottomRight->val
                        &&root->topLeft->val == root->bottomLeft->val) {
                    root->isLeaf = true;
                    root->val = root->topLeft->val;
                    root->topLeft = root->topRight = root->bottomLeft = root->bottomRight = NULL;
                }
            }
        }

        return root;
    }
};

int test() {

    cout << "test passed" << endl;
    return 0;
}

int main(int argc, char **argv) {
    test();
    return 0;
}
