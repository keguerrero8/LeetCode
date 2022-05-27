class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        
        for i in range(len(nums)-2):
            if i-1 >= 0 and nums[i-1] == nums[i]:
                continue
            start = i+1
            end = len(nums)-1
            twoSum = 0-nums[i]
            
            while start < end:
                if start-1 > i and nums[start-1] == nums[start]:
                    start += 1
                    continue
                if end+1 < len(nums) and nums[end+1] == nums[end]:
                    end -= 1
                    continue
                currentSum = nums[start] + nums[end]
                if currentSum == twoSum:
                    result.append([nums[i], nums[start], nums[end]])
                    start += 1
                elif currentSum > twoSum:
                    end -= 1
                else:
                    start += 1
                    
                    
        return result
        