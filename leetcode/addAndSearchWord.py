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
    This is calling for a data structure for text retrieval, which implies that
Trie tree might be a good choice. But the `search` procedure requires WILDCARD
matching, which means that, in another word, there are MULTIPLE BRANCHES during the
search process. So this will be a GRAPH SEARCH PROBLEM. A typical solution would
be DEPTH-FIRST SEARCH with BACKTRACKING.
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
        exist = self.trie.search_node_recursive(word)
        # exist = self.trie.search(word)
        print(word, exist)
        return exist

class TrieNode(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.leaf     = False
        self.children = {}


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        pCrawl = self.root
        for ch in word:
            if not ch in pCrawl.children:
                pCrawl.children[ch] = TrieNode()
            pCrawl = pCrawl.children[ch]
        pCrawl.leaf = True

    def search_node_recursive(self, word, node=None):
        if not node:
            node = self.root
        if not word:
            # the recursive call's base case: search word is empty now
            return node.leaf
        ch = word[0]
        if ch in node.children:
            return self.search_node_recursive(word[1:], node.children[ch])
        elif ch == '.':
            # wildcard matching
            for ch in node.children:
                if self.search_node_recursive(word[1:], node.children[ch]):
                    return True

        return False

    # TODO: convert the recursive procedure call into iterative ones

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        pCrawl = self.root
        for ch in word:
            if ch not in pCrawl.children and ch is not '.':
                return False
            else:
                pCrawl = pCrawl.children[ch]
            pass
        return pCrawl.leaf

# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("word")
wordDictionary.search("pattern")
wordDictionary.search("word")

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
