class Solution(object):
    def leastInterval(self, tasks, n):
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        q = []
        
        while maxHeap or q:
            time += 1
            
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
                    
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.pop(0)[0])      
        
        return time