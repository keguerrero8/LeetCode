class Solution(object):
    def minDistance(self, word1, word2):
        edits = [[x for x in range(len(word1)+1)] for y in range(len(word2)+1)]
        for i in range(1, len(word2) + 1):
            edits[i][0] = edits[i-1][0] + 1
        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):
                if word2[i-1] == word1[j-1]:
                    edits[i][j] = edits[i-1][j-1]
                else:
                    edits[i][j] = 1 + min(edits[i-1][j-1], edits[i-1][j], edits[i][j-1])
        return edits[-1][-1]
        