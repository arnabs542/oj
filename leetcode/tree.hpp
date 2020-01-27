#pragma once

#include <vector>
#include <unordered_map>

using namespace std;

// binary tree node data structure
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x)
        : val(x)
          , left(NULL)
          , right(NULL)
    {
    }

    void print();
    vector<int> preorderTraversal(bool iterative=true);
    vector<int> inorderTraversal(bool iterative=true);
    vector<int> postorderTraversal(bool iterative=true);
};

class SegmentTree {
    public:
};

class TrieNode {
public:
    unordered_map<char, shared_ptr<TrieNode>> m_children;
    bool m_is_leaf;

    TrieNode(bool is_leaf=false): m_is_leaf(is_leaf) {}
};

class Trie {
private:
    shared_ptr<TrieNode> m_root;

public:
    /** Initialize your data structure here. */
    Trie();
    Trie(vector<string>& words);

    /** Inserts a word into the trie. */
    void insert(string word);

    /** Returns if the word is in the trie. */
    bool search(string word);

    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix);

    /** remove a word from the trie.*/
    void remove(string word);

    /** Returns the shortest word in the trie that is prefix of given word */
    string shortestPrefix(string word);

    /** Returns a vector of string that starts with given prefix */
    vector<string> wordsStartingWith(string prefix);
};


class BitTree {
public:
    BitTree(int n): mSize(n) {
        mData.resize(n+1);
    }

    inline int update(int i, int value) {
        while (i <= mSize) {
            mData[i] += value;
            i += i & (-i);
        }
        return 0;
    }

    inline int query(int i) {
        int rangeSum = 0;
        while (i > 0) {
            rangeSum += mData[i];
            i &= (i-1); //i -= i & (-i);
        }

        return rangeSum;
    }

    vector<int> mData; // [0, 1, ..., n];
    int mSize; // n
};


/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * bool param_2 = obj.search(word);
 * bool param_3 = obj.startsWith(prefix);
 */
