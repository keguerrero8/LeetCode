class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif nums[mid] >= nums[left]:
                if target > nums[mid] or nums[left] > target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
        return -1
                
                
        