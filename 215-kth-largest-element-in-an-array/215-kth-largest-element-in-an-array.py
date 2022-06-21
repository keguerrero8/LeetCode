class Solution(object):
    def findKthLargest(self, nums, k):
        for i in range(len(nums)):
            nums[i] *= -1
        heapify(nums)
        
        for i in range(k):
            kthLargest = heapq.heappop(nums)
            
        return kthLargest*-1
        