class Solution(object):
    def findMin(self, nums):
        l, r = 0, len(nums)-1
        minVal = float("inf")
        
        while l <= r:
            mid = (l+r) // 2
            minVal = min(minVal, nums[mid])
            
            if nums[mid] >= nums[l]:
                if nums[l] > nums[r]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                if nums[l] > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
                    
        return minVal
        