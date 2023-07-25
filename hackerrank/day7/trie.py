class TrieNode:
        # Initialize your data structure here.
        def __init__(self):
            self.word=False
            self.children={}
    
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node=self.root
        for i in word:
            if i not in node.children:
                node.children[i]=TrieNode()
            node=node.children[i]
        node.word=True

    def search(self, word):
        node=self.root
        for i in word:
            if i not in node.children:
                return False
            node=node.children[i]
        return node.word

    def startsWith(self, prefix):
        node=self.root
        for i in prefix:
            if i not in node.children:
                return False
            node=node.children[i]
        return True
    
    def hasOtherPrefix(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            if node.word:
                return True
            node = node.children[i]
        return False
    
    def isPrefixOfOthers(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        return True
            
keys = ['aa', 'a']
def noPrefix(words):
    trie = Trie()
    wordMap = {}
    for k in words:
        if trie.search(k) or trie.isPrefixOfOthers(k):
            print("BAD SET")
            print(k)
            return 
        trie.insert(k)
    
    for k in words:
        if trie.hasOtherPrefix(k):
            print("BAD SET")
            print(k)
            return
    print("GOOD SET")

noPrefix(keys)
