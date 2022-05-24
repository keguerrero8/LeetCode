class Solution(object):
    def longestMountain(self, arr):
            
        if len(arr) < 3:
            return 0
        
        longestPeak = 0
        i = 1
        while i < len(arr) - 1:
            currentPeak = 0
            if arr[i-1] < arr[i] and arr[i+1] < arr[i]:
                currentPeak = 3
                j = i-1
                while j-1 >= 0 and arr[j-1] < arr[j]:
                    currentPeak += 1
                    j -= 1
                    
                j = i+1
                while j+1 < len(arr) and arr[j+1] < arr[j]:
                    currentPeak += 1
                    j += 1   
                longestPeak = max(longestPeak, currentPeak)
                i = j
            i += 1
                
        return longestPeak
                
            
        