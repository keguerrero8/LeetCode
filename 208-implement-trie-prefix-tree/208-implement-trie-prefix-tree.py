class Trie(object):
    #"apple" {"a": Trie("a")}, {"p": Trie{"p"}}
    #a -> p -> p -> l -> e (mark this node as end)
    #b -> u -> s (mark this node as end)
    def __init__(self, char = None):
        self.children = {}
        self.end = False
        self.char = char

    def insert(self, word):
        current = self
        for char in word:
            if char not in current.children:  
                current.children[char] = Trie(char)
            current = current.children[char]
        current.end = True
        

    def search(self, word):
        current = self
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.end

    def startsWith(self, prefix):
        current = self
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True 
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)