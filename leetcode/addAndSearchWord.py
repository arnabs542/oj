'''
Add and Search Word - Data structure design

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

Note:
You may assume that all words are consist of lowercase letters a-z.

SOLUTION:
    1. This is calling for a data structure for text retrieval, which implies that
TRIE tree might be a good choice. But the `search` procedure requires WILDCARD
matching, which means that, in another word, there are MULTIPLE BRANCHES during the
search process. So this will be a GRAPH SEARCH PROBLEM. A typical solution would
be DEPTH-FIRST SEARCH with BACKTRACKING.
    2. Hash Table from word length to word.
'''

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.trie = Trie()


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.trie.insert(word)


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        exist = self.trie.searchFromRecursive(word)
        # exist = self.trie.search(word)
        print('SEARCH', word, exist)
        return exist

LEAF_SYMBOL = '#'
class TrieNode(dict,):

    # LEAF_SYMBOL = '#'

    def __init__(self):
        """
        Initialize your data structure here.
        """
        super(dict, self).__init__()


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for ch in word:
            if not ch in node:
                node[ch] = TrieNode()
            node = node[ch]
        node[LEAF_SYMBOL] = True

    def searchFromRecursive(self, word, node=None):
        if not node:
            node = self.root
        if not word:
            # the recursive call's base case: search word is empty now
            return LEAF_SYMBOL in node
        ch = word[0]
        if ch in node:
            return self.searchFromRecursive(word[1:], node[ch])
        elif ch == '.':
            # wildcard matching
            for ch in node:
                if ch == LEAF_SYMBOL:
                    continue
                if self.searchFromRecursive(word[1:], node[ch]):
                    return True

        return False

    # TODO: convert the recursive procedure call into iterative ones

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for ch in word:
            if ch not in node and ch is not '.':
                return False
            else:
                node = node[ch]
            pass
        return LEAF_SYMBOL in node

# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("word")
wordDictionary.search("pattern")
wordDictionary.search("word")
print()

wordDictionary = WordDictionary()
wordDictionary.addWord('a')
wordDictionary.search(".")
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
wordDictionary.search("pad")
wordDictionary.search("bad")
wordDictionary.search(".ad")
wordDictionary.search("b..")

print()
wordDictionary = WordDictionary()
wordDictionary.addWord("at")
wordDictionary.addWord("and")
wordDictionary.addWord("an")
wordDictionary.addWord("add")
wordDictionary.search("a")
wordDictionary.search(".at")
wordDictionary.addWord("bat")
wordDictionary.search(".at")
wordDictionary.search("an.")
wordDictionary.search("a.d.")
wordDictionary.search("b.")
wordDictionary.search("a.d")
wordDictionary.search(".")
print()
