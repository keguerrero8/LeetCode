class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False

class WordDictionary(object):
    def __init__(self):
        self.base = TrieNode()

    def addWord(self, word):
        current = self.base
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.endWord = True
            
        

    def search(self, word):
        def dfs(i, base):
            if i == len(word):
                return base.endWord #change this if we need to check end of word

            char = word[i]
            if char != ".":
                if char in base.children:
                    return dfs(i + 1, base.children[char])
                else:
                    return False
                
            for node in base.children.values():
                if dfs(i+1, node):
                    return True
                
            return False

        return dfs(0, self.base)
    
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)