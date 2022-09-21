class Solution(object):
    def unhappyFriends(self, n, preferences, pairs):
        d = {}
        
        for x, y in pairs:
            d[x] = set(preferences[x][:preferences[x].index(y)])
            d[y] = set(preferences[y][:preferences[y].index(x)])
        
        res = 0
        
        for x in d:
            for y in d[x]:
                if x in d[y]:
                    res += 1
                    break
        return res
            
        
        