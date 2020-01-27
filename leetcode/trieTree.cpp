#include <debug.hpp>
#include "tree.hpp"

/**
 * Trie - prefix tree implementation
 *
 * Complexity:
 * Trie could use less space compared to Hash Table when inserting/storing many keys with the same prefix.
 * Searching for a key in a balanced tree costs O(m \log n) time complexity.
 * In this case using trie has only O(m) time complexity, where m is the key length.
 *
 * A dummy root indicates start of a string.
 * Each node contains symbol, indicated by the mapping from its parent node.
 * Any path from root node corresponds to a prefix.
 *
 * Space complexity:
 * Best case: O(max(word lengths))
 * Worst case: O(sum(word lengths))
 *
 * TODO: optimization
 *
 * 1. Use vector as pointers to children, ASCII value of characters as indices.
 * 2. Use language specific performance techniques: register variables, etc
 */

Trie::Trie() {
    m_root = make_shared<TrieNode>(false);
}

Trie::Trie(vector<string>& words): Trie(){
    for (string& word: words) {
        insert(word);
    }
}

void Trie::insert(string word) {
    shared_ptr<TrieNode> p = m_root;
    shared_ptr<TrieNode> node = NULL;
    for (char c: word) {
        if (p->m_children.find(c) == p->m_children.end()) {
            node = make_shared<TrieNode>();
            p->m_children.insert(make_pair(c, node));
        }
        p = p->m_children.find(c)->second;
    }
    p->m_is_leaf = true;
}

bool Trie::search(string word) {
    shared_ptr<TrieNode> p = m_root;
    for (char c: word) {
        unordered_map<char, shared_ptr<TrieNode>>::iterator it = p->m_children.find(c);
        if (it == p->m_children.end()) {
            return false;
        }
        p = it->second;
    }
    return p->m_is_leaf;
}

bool Trie::startsWith(string prefix) {
    shared_ptr<TrieNode> p = m_root;
    for (char c: prefix) {
        unordered_map<char, shared_ptr<TrieNode>>::iterator it = p->m_children.find(c);
        if (it == p->m_children.end()) {
            return false;
        }
        p = it->second;
    }
    return true;
}

void Trie::remove(string word) {
    throw runtime_error("NOT IMPLEMENTED");
}

string Trie::shortestPrefix(string word) {
    //if (word == "") {
        //return NULL;
    //}

    shared_ptr<TrieNode> p = m_root;
    for (unsigned int i = 0; i < word.length(); ++i) {
        if (p->m_is_leaf) { return word.substr(0, i); }
        auto it = p->m_children.find(word[i]);
        if (it == p->m_children.end()) { return ""; }
        p = p->m_children.find(word[i])->second;
    }

    return p->m_is_leaf ? word: "";
}
