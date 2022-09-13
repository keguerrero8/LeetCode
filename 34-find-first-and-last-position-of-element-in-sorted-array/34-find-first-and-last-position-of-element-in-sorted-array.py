class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:                
        def bSearch(leftBias):
            i = -1
            l, r = 0, len(nums) - 1
            
            while l <= r:
                mid = (l+r) // 2
                if target > nums[mid]:
                    l = mid + 1
                elif target < nums[mid]:
                    r = mid - 1
                else:
                    i = mid
                    if leftBias:
                        r = mid - 1
                    else:
                        l = mid + 1
            return i
        left = bSearch(True)
        right = bSearch(False)
        return [left, right]