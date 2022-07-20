class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        A, B = nums1, nums2
        
        if len(B) < len(A):
            A, B = B, A
            
        l, r = 0, len(A) - 1
        
        while True:
            midA = (l + r) // 2
            midB = half - midA - 2
            
            Aleft = A[midA] if midA >= 0 else float("-inf")
            Aright = A[midA + 1] if midA + 1 < len(A) else float("inf")
            Bleft = B[midB] if midB >= 0 else float("-inf")
            Bright = B[midB + 1] if midB + 1 < len(B) else float("inf")
            
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2: 
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                    
            elif Bleft > Aright:
                l = midA + 1
            else:
                r = midA - 1