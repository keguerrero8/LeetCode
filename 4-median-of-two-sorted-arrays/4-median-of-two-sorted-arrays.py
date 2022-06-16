class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        
        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        
        while True:
            midA = (l + r) // 2 #0 -> 0
            midB = half - midA - 2 #2-0-2 = 0
            
            Aleft = A[midA] if midA >= 0 else float("-inf") #1
            Aright = A[midA+1] if (midA + 1) < len(A) else float("inf") #2
            Bleft = B[midB] if midB >= 0 else float("-inf") #3
            Bright = B[midB+1] if (midB + 1) < len(B) else float("inf") #4
            
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    return (float(max(Aleft, Bleft)) + float(min(Aright, Bright))) / 2
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                r = midA - 1
            else:
                l = midA + 1 #0+1 = 1
            