class Solution(object):
    def sortArray(self, array):
        if len(array) == 1:
            return array

        midPt = (0 + len(array)) // 2
        left = self.sortArray(array[:midPt])
        right = self.sortArray(array[midPt:])

        sorted = [0]*len(array)
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted[k] = left[i]
                i += 1
            else:
                sorted[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            sorted[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            sorted[k] = right[j]
            j += 1
            k += 1

        return sorted

