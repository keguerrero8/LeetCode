class Solution(object):
    def maxSlidingWindow(self, nums, k):
        dq = []
        output = []
        
        for i in range(k):
            while dq and nums[i] > dq[-1]:
                dq.pop()
            dq.append(nums[i])
            
        output.append(dq[0])
        
        i = 0
        for j in range(k, len(nums)):
            i += 1
            if nums[i-1] == dq[0]:
                dq.pop(0)
            while dq and nums[j] > dq[-1]:
                dq.pop()
                
            dq.append(nums[j])
            output.append(dq[0])
            
        return output