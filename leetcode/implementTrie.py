'''
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
'''

# @optimization: TrieNode inheriting dictionary class will boost the speed


class TrieNode(dict):

    LEAF_SYMBOL = '#'

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
        node[node.LEAF_SYMBOL] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            else:
                node = node[ch]
            pass
        return node.LEAF_SYMBOL in node

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            else:
                node = node[ch]
            pass

        return node is not None


# Your Trie object will be instantiated and called as such:
def test():
    trie = Trie()
    trie.insert("somestring")
    print ('somestring' +  (' is in trie' if trie.search("somestring") else ' not in trie'))
    print ('key' +  (' is in trie' if trie.search("key") else ' not in trie'))
    trie.search("key")

if __name__ == '__main__':
    test()
