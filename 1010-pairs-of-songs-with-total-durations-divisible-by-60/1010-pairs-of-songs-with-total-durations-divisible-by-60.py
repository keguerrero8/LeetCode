class Solution(object):
    def numPairsDivisibleBy60(self, time):
        hashRems = {}
        songPairs = 0
        for i in range(len(time)):
            remainder = time[i] % 60
            pairToMatch = 60 - remainder
            if remainder == 0 and 0 in hashRems:
                songPairs += hashRems[0]
            elif pairToMatch in hashRems:
                songPairs += hashRems[pairToMatch]
                
            hashRems[remainder] = 1 + hashRems.get(remainder, 0)
                
        return songPairs
            
        