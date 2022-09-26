# class Trie:
#     def __init__(self):
#         self.children = {}
#         self.count = 0
        
#     def insert(self, char, children):
#         for trie in children.values():
#             self.insert(char, trie.children)
            
#         if char not in children:
#             self.count += 1
#             children[char] = Trie()
#         return
        

# class Solution(object):
#     def countDistinct(self, s):
#         trie = Trie()
        
#         for char in s:
#             trie.insert(char, trie.children)
            
#         return trie.count

class Solution(object):
    def countDistinct(self, s):
        visited = set()
        res = 0
        
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if s[i:j] not in visited:
                    visited.add(s[i:j])
                    res += 1
        return res
        