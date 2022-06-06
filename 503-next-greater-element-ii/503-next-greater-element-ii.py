class Solution(object):
    def nextGreaterElements(self, nums):
        result = [-1] * len(nums)
        stack = []
        self.getNextGreaterHelper(nums, stack, result)
        self.getNextGreaterHelper(nums, stack, result)
        return result


    def getNextGreaterHelper(self, array, stack, result):
        for i in reversed(range(len(array))):
            while len(stack) and array[i] >= stack[-1]:
                stack.pop()

            if len(stack) == 0:
                stack.append(array[i])
            else:
                result[i] = stack[-1]
                stack.append(array[i])
        