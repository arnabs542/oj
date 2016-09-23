'''
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
'''


class TrieNode(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isLeaf  = False
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
        pCrawl.isLeaf = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        pCrawl = self.root
        for ch in word:
            if ch not in pCrawl.children:
                return False
            else:
                pCrawl = pCrawl.children[ch]
            pass
        return pCrawl.isLeaf

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        pCrawl = self.root
        for ch in prefix:
            if ch not in pCrawl.children:
                return False
            else:
                pCrawl = pCrawl.children[ch]
            pass

        return pCrawl is not None


# Your Trie object will be instantiated and called as such:
def test():
    trie = Trie()
    trie.insert("somestring")
    print ('somestring' +  (' is in trie' if trie.search("somestring") else ' not in trie'))
    print ('key' +  (' is in trie' if trie.search("key") else ' not in trie'))
    trie.search("key")

if __name__ == '__main__':
    test()
