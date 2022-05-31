# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        return self.sortedArrayToBSTHelper(nums, 0, len(nums)-1)
        
    def sortedArrayToBSTHelper(self, nums, start, end):
        if start > end:
            return None

        mid = (start + end) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBSTHelper(nums, start, mid - 1) 
        root.right = self.sortedArrayToBSTHelper(nums, mid + 1, end) 

        return root
        