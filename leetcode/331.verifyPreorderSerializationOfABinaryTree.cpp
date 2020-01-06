/*
 *
 *
331. Verify Preorder Serialization of a Binary Tree

One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #

For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:
"9,3,4,#,#,1,#,#,2,#,6,#,#"
Return true

Example 2:
"1,#"
Return false

Example 3:
"9,#,#,1"
Return false

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.


==============================================================================================
SOLUTION

Preorder traversal is a kind of depth first search. As for dfs, the it can be done with
recursion or stack data structure.

So the underlying algorithm is still stack, with or without constructing the tree.

The preorder serialization is right only if it's subtrees' serialization is right too.

1. Stack

Initialize the stack.

Push the serialized token into the stack one by one. Once we find two successive '#' symbol,
we can construct a complete subtree: merge these two null nodes with their parent node into
one single node that have already been visited, which means it's a valid preorder visited subtree.

Mark the visited node as '*'. Then for any adjacent sequence '*#', we do the merge process again.
Until the stack is left with one '*' or empty. Of course, we can simplify this situation further:
replace a subtree with NULL node children with '#', treating it as a NULL node. This method utilizes
the recurrence relation between tree nodes.

2. count Indegree and outdegree?
How to ensure the preorder property?

Among preorder, inorder, postorder, only preorder has the property of root visited first.

For the other ways of traversing a tree, leaf nodes are always visited first, giving such fact that
the degree difference(outdegree - indegree) could go minus. But for preorder traversal will never
have this difference below zero.

 *
 */

#include <debug.hpp>

class Solution {
public:
    bool isValidSerialization(string preorder) {
        //return _isValidSerializationStack(preorder);
        return _isValidSerializationDegree(preorder);
    }

    bool _isValidSerializationStack(string preorder) {
        stack<string> nodeStack;
        stringstream ss(preorder);
        string token;

        // XXX: getline with stringstream as string split in C++
        while (getline(ss, token, ',')) {
            if (token == "#") {
                while (nodeStack.size() >= 2 && nodeStack.top() == "#") {
                    nodeStack.pop();
                    if (nodeStack.top() == "#") return false; // root node of a subtree cannot be NULL
                    else nodeStack.pop();
                }
            }
            nodeStack.push(token);
        }
        return nodeStack.empty() || (nodeStack.size() == 1 && nodeStack.top() == "#");
    }

    // TODO: count indegree and out degree?
    bool _isValidSerializationDegree(string preorder) {
        if (preorder.length() == 0) { return true; }
        stringstream ss(preorder);
        string token;

        int degreeDifference = 1; // root node has indegree of 0 = +1 - 1, for compensate init with -1

        while (getline(ss, token, ',')) {
            degreeDifference -= 1; // // all nodes have 1 indegree (root compensated), minus indegree
            if (degreeDifference < 0) { return false; } // preorder traverse, degree difference should never exceeds 0
            if (token != "#") { degreeDifference += 2; } // only non-leaf node has 2 outdegree
        }

        return degreeDifference == 0;
    }


};

void test() {

    Solution solution;

    string preorder;

    preorder = "";
    assert(solution.isValidSerialization(preorder));

    preorder = "#";
    assert(solution.isValidSerialization(preorder));

    preorder = "#,#,#";
    assert(solution.isValidSerialization(preorder) == false);

    preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#";
    assert(solution.isValidSerialization(preorder));

    preorder = "#,4,#,3,#,1,#,9,#,2,#,6,#"; // inorder of above tree
    assert(solution.isValidSerialization(preorder) == false);

    preorder = "1,#";
    assert(solution.isValidSerialization(preorder) == false);

    preorder = "1,#,#";
    assert(solution.isValidSerialization(preorder) == true);

    preorder = "9,#,#,1";
    assert(solution.isValidSerialization(preorder) == false);

    cout << "self test passed" << endl;
}

int main(int argc, char* argv[])
{
    test();
    return 0;
}
