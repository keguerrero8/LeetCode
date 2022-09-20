class Freq:
    def __init__(self, frequency, word):
        self.frequency = frequency
        self.word = word
        
    def __lt__(self, other):
        if self.frequency == other.frequency:
            return self.word > other.word 
        return self.frequency < other.frequency

class Solution(object):
    def topKFrequent(self, words, k):
        counter = {}
        for word in words:
            counter[word] = counter.get(word, 0) + 1
        h = []
        for word in counter:
            heapq.heappush(h, Freq(counter[word], word))
            if len(h) > k:
                heapq.heappop(h)
        res = []
        while h:
            res.append(heappop(h).word)
            
        return res[::-1]