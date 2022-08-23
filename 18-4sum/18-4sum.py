class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        possibleQuad = []
        self.kSum(0, 4, nums, res, target, possibleQuad)
        return res
        
    def kSum(self, start, k, nums, res, target, possibleQuad):
        if k == 2:
            self.twoSum(start, nums, res, target, possibleQuad)
        else:
            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i-1]:
                    continue
                newTarget = target - nums[i]
                possibleQuad.append(nums[i])
                self.kSum(i + 1, k-1, nums, res, newTarget, possibleQuad)
                possibleQuad.pop()
                
    def twoSum(self, start, nums, res, target, possibleQuad):
        l, r = start, len(nums) - 1
        
        while l < r:
            currentSum = nums[l] + nums[r]
            if currentSum == target:
                res.append(possibleQuad + [nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
            elif currentSum < target:
                l += 1
            else:
                r -= 1
                

            
        