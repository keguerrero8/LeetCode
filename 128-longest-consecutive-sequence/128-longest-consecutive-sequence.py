class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        
        graph = {}
        longestLength = 1
        
        def traverse(graph, value, increment):
            length = 1
            currentVal = value
            while currentVal in graph:
                length += 1
                graph[currentVal] = True
                currentVal += increment
                
            return length
        
        for value in nums:
            if value not in graph:
                graph[value] = False
        
        for value in nums:
            length = 1
            
            if graph[value] == False:
                graph[value] = True
                
                if value - 1 in graph:
                    length = traverse(graph, value - 1, -1)
                elif value + 1 in graph:
                    length = traverse(graph, value + 1, 1)
                    
            longestLength = max(longestLength, length)
            
        return longestLength
                    