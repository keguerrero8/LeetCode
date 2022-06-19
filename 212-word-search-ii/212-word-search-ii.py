class Solution(object):
    def findWords(self, board, words):
        trie = TrieNode()
        for word in words:
            trie.insert(word)

        res, visiting = [], set()
        
        def dfs(row, col, node, word):
            if row < 0 or col < 0 or row == len(board) or col == len(board[0]) or board[row][col] not in node.children or (row, col) in visiting:
                return
            
            visiting.add((row, col))
            node = node.children[board[row][col]]
            word += board[row][col]
            
            if node.isWord:
                res.append(word)
                node.isWord = False
                trie.pruneWord(word)
                
            dfs(row, col - 1, node, word)
            dfs(row, col + 1, node, word)
            dfs(row - 1, col, node, word)
            dfs(row + 1, col, node, word)
                
            visiting.remove((row, col))

        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(row, col, trie, "")
        return list(res)


#     def getNeighbors(self, row, col, trie, visiting, board):
#         neighbors = []

#         if col - 1 >= 0 and board[row][col-1] in trie.root and (row, col-1) not in visiting:
#             neighbors.append([row, col-1])

#         if col + 1 < len(board[0]) and board[row][col+1] in trie.root and (row, col+1) not in visiting:
#             neighbors.append([row, col+1])

#         if row - 1 >= 0 and board[row-1][col] in trie.root and (row-1, col) not in visiting:
#             neighbors.append([row-1, col])

#         if row + 1 < len(board) and board[row+1][col] in trie.root and (row+1, col) not in visiting:
#             neighbors.append([row+1, col])

#         return neighbors



class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def insert(self, word):
        current = self
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.isWord = True
        
    def pruneWord(self, word):
        cur = self
        nodeAndChildKey = []
        for char in word:
            nodeAndChildKey.append((cur, char))
            cur = cur.children[char]

        for parentNode, childKey in reversed(nodeAndChildKey):
            targetNode = parentNode.children[childKey]
            if len(targetNode.children) == 0:
                del parentNode.children[childKey]
            else:
                return
        