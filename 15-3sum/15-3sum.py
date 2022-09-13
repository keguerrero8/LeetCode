class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue    
            l, r = i + 1, len(nums) - 1
            target = 0 - nums[i]
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                elif target > nums[l] + nums[r]:
                    l += 1
                else:
                    r -= 1
                while l > i + 1 and nums[l] == nums[l-1]:
                    l += 1
                    if l == len(nums):
                        break
                    
        return res
            
        