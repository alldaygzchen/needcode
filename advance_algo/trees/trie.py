# root trienode >> first trienode >> second trienode

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):

        # create a reference
        curr = self.root

        # prevent duplicate child nodes
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word =True

    def search(self,word):

        # create a reference
        curr = self.root

        # prevent duplicate child nodes
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word
    
    def startsWith(self,prefix):

        # create a reference
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


if __name__=="__main__":
    trie = Trie()
    words = ["apple","ape","nope"]
    for word in words:
        trie.insert(word)

    print(trie.startsWith("no")) # True
    print(trie.search("app")) # False
    print(trie.search("ape")) # True
