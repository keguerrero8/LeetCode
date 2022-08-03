class Solution(object):
    def findKthLargest(self, nums, k):
        return self.quickSelectHelper(nums, k, 0, len(nums) - 1)

    def quickSelectHelper(self, array, k, start, end):
        partitionIdx = self.partition(array, start, end)

        if partitionIdx + 1 == k:
            return array[partitionIdx]
        elif partitionIdx + 1 > k:
            return self.quickSelectHelper(array, k, start, partitionIdx - 1)
        else:
            return self.quickSelectHelper(array, k, partitionIdx + 1, end)

    def partition(self, array, start, end):
        pivot = array[end]

        i = start - 1
        j = start

        while j < end:
            if array[j] >= pivot:
                i += 1
                array[j], array[i] = array[i], array[j]
            j += 1

        array[end], array[i+1] = array[i+1], array[end]
        return i + 1
        