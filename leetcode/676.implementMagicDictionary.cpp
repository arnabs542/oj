/**
 *
676. Implement Magic Dictionary

Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.

Example 1:
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False
Note:
    - You may assume that all the inputs are consist of lowercase letters a-z.
    - For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
    - Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details.

==============================================================================================
SOLUTION

1. Brute force

For each word in the dictionary, compare it against every word in the dictionary
to check whether they are different by only 1 character.

Complexity
For each word to search, it takes O(w) to compare.
O(lw), where l is the dictionary length and m is the average word length.

2. Hash table storing transformation of word(generalized neighbour)

Preprocess each word in dictionary to possible words obtained by replacing one character to '*'.
hello -> {*ello, h*llo, ..., hell*}
And store the transformation with a hash table.

To search a word, enumerate all words obtained by replacing one character to '*'.

Time Complexity
Build dictionary: O(lw²) where l is the dictionary size, w is the average word length in dictionary.
Search: O(w²), where w is the average word length.

Space complexity
build: O(lw²), search: O(w²)

3. Trie - prefix tree
Build a trie tree, and search, allowing mismatching characters maximum number of 1.

Search with replacement, or fuzzy search.
At each node, we have two scenarios: replace current character or not.
If replacing current character, then we have at most 25 branches to go.

Apparently, this is a recursive situation.

Time Complexity
After building the trie tree, search complexity is: O(m), where m is the target word length.
Average case: O(w).
Worst case complexity: O(26w)=O(w)?

Space complexity
Build: O(w) ~ O(lw), search: O(w), where w is the average word length.

Corner case:
dict = {"hello", "hallo"};
search("hello"), true or false?

 *
 */

#include <debug.hpp>
//#include "_tree.hpp"

struct TrieNode {
    TrieNode *m_children[26] = {NULL};
    bool m_is_leaf=false;
};

class MagicDictionary {
    TrieNode *m_root;
public:
    /** Initialize your data structure here. */
    MagicDictionary() {
        m_root = new TrieNode();
    }

    /** Build a dictionary through a list of words */
    void buildDict(vector<string> dict) {
        TrieNode *p = NULL;
        for (string word: dict) {
            // insert
            p = m_root;
            for (char c: word) {
                if (!(p->m_children[c - 'a'])) {
                    p->m_children[c - 'a'] = new TrieNode();
                }
                p = p->m_children[c - 'a'];
            }
            p->m_is_leaf = true;
        }
    }

    /** Returns if there is any word in the trie that equals to the given word after modifying exactly one character */
    bool search(string word) {
        return _dfs(word, m_root, 1);
    }

    bool _dfs(string word, TrieNode *p, int nModify) {
        if (!word.length()) {
            return p->m_is_leaf && nModify == 0; // word ends
        } else {
            for (int j = 0; j < 26; ++j) {
                //cout << "child: " << "subsearch: " << word.substr(i + 1) << ", nModify: " << nModify << endl;
                auto child = p->m_children[j];
                if(child && _dfs(word.substr(1), child, nModify - (word[0] - 'a' != j)))
                    return true;
            }
        }
        return false;
    }
};

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary obj = new MagicDictionary();
 * obj.buildDict(dict);
 * bool param_2 = obj.search(word);
 */

void test() {
    MagicDictionary dict;

    assert(dict.search("") == false);
    assert(dict.search("hello") == false);

    dict.buildDict({"hello", "leetcode", "hallo", "hi", "he"});

    assert(dict.search("hello") == true);
    assert(dict.search("xello") == true);
    assert(dict.search("hellx") == true);
    assert(dict.search("xellx") == false);
    assert(dict.search("hhllo") == true);
    assert(dict.search("hell") == false);
    assert(dict.search("leetcoded") == false);

    dict = MagicDictionary();

    dict.buildDict({"hello","hallo","leetcode"});
    assert(dict.search("hello"));
    assert(dict.search("hhllo"));
    assert(dict.search("hell") == false);
    assert(dict.search("leetcoded") == false);

    cout << "self test passed" << endl;
}


int main(int argc, char *argv[])
{
    test();
    return 0;
}
