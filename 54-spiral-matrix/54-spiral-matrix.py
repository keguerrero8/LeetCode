class Solution(object):
    def spiralOrder(self, array):
        startRow = 0
        startColumn = 0
        endRow = len(array)-1
        endColumn = len(array[0])-1
        oneDArray = []
        while startRow <= endRow and startColumn <= endColumn:
            for i in range(startColumn, endColumn + 1):
                oneDArray.append(array[startRow][i])

            for i in range(startRow + 1, endRow + 1):
                oneDArray.append(array[i][endColumn])

            for i in range(endColumn-1, startColumn, -1):
                if startRow == endRow:
                    break
                oneDArray.append(array[endRow][i])

            for i in range(endRow, startRow, -1):
                if startColumn == endColumn:
                    break
                oneDArray.append(array[i][startColumn])

            startRow += 1
            startColumn += 1
            endRow -= 1
            endColumn -= 1

        return oneDArray