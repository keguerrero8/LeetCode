class Leaderboard(object):

    def __init__(self):
        self.scoreHash = {}

    def addScore(self, playerId, score):
        if playerId not in self.scoreHash:
            self.scoreHash[playerId] = score
        else:
            self.scoreHash[playerId] += score

    def top(self, K):
        heap = []
        
        for playerId in self.scoreHash.keys():
            heap.append([-1*self.scoreHash[playerId], playerId])
            
        heapq.heapify(heap)
        n, total = 0, 0
        
        while n < K:
            score, playerId = heapq.heappop(heap)
            total += score
            n += 1
            
        return abs(total)
        

    def reset(self, playerId):
        del self.scoreHash[playerId]
        

#13, 93, 84, 6, 89, 31, 7, 1, 98, 42
# reset 13, 93
#add 76, 68
#top 1

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)