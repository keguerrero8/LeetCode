class Solution(object):
    def networkDelayTime(self, times, n, k):
        graphHash = {i+1:[] for i in range(n)}
        for time in times:
            graphHash[time[0]].append([time[1], time[2]])
            
        h = [[0, k]]
        visited = set()
        t = float("-inf")
        heapq.heapify(h)
                    
        while h:
            time, nodeToVisit = heapq.heappop(h)
            if nodeToVisit in visited:
                continue
            t = max(t, time)
            for n2, w1 in graphHash[nodeToVisit]:
                if n2 not in visited:
                    distance = time + w1
                    heapq.heappush(h, [distance, n2])
                    
            visited.add(nodeToVisit)
            
        return t if len(visited) == n else -1

#         graphHash = {i+1:[] for i in range(n)}
#         for time in times:
#             graphHash[time[0]].append([time[1], time[2]])
            
#         visited = set()
#         distances = [float("inf") for i in range(n)]
#         distances[k-1] = 0
        
#         def getNextNode():
#             minTime = float("inf")
#             nodeToVisit = None
#             for i in range(len(distances)):
#                 if i+1 not in visited and minTime >= distances[i]:
#                     minTime = distances[i]
#                     nodeToVisit = i + 1
#             return nodeToVisit
                
        
#         while len(visited) < n:
#             nodeToVisit = getNextNode() 
            
#             for neighbor in graphHash[nodeToVisit]:
#                 distance = distances[nodeToVisit-1] + neighbor[1]
#                 distances[neighbor[0]-1] = min(distances[neighbor[0]-1], distance)
                
#             visited.add(nodeToVisit)
        
#         minTime = float("-inf")
#         for i in range(len(distances)):
#             if distances[i] == float("inf"):
#                 return -1
#             minTime = max(minTime, distances[i])
            
#         return minTime
            
            
            
            
        
        