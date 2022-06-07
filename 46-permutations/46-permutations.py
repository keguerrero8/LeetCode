class Solution(object):
    def permute(self, nums):
        result = []
        return self.getPermutationsHelper(nums, 0, result)


    def getPermutationsHelper(self, array, idx, result):
        if idx == len(array) - 1:
            result.append(array[:])
            return result

        for i in range(idx, len(array)):
            array[idx], array[i] = array[i], array[idx]
            self.getPermutationsHelper(array, idx + 1, result)
            array[idx], array[i] = array[i], array[idx]

        return result
        