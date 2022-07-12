class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        base = []
        
        def findSumCombinations(num, start, target):
            if num == 2:
                self.twoSum(start, res, base, nums, target)
                return
            
            end = len(nums) - num + 1
            for i in range(start, end):
                if i > start and nums[i] == nums[i-1]:
                    continue
                newSum = target - nums[i]
                base.append(nums[i])
                findSumCombinations(num - 1, i + 1, newSum)
                base.pop()
            return res
        
        return findSumCombinations(4, 0, target)
    
    def twoSum(self, start, res, base, nums, target):
        l, r = start, len(nums) - 1
        
        while l < r:
            total = nums[l] + nums[r]
            if total == target:
                res.append(base + [nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
            elif total < target:
                l += 1
            else:
                r -= 1
    
        