class SparseVector:
    def __init__(self, nums):
        self.array = []
        for i in range(len(nums)):
            if nums[i]:
                self.array.append([i, nums[i]])
                
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        p, q = 0, 0
        total = 0
        
        while p < len(self.array) and q < len(vec.array):
            if self.array[p][0] == vec.array[q][0]:
                total += self.array[p][1] * vec.array[q][1]
                p += 1
                q += 1
            elif self.array[p][0] > vec.array[q][0]:
                q += 1
            else:
                p += 1
        
        return total
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)