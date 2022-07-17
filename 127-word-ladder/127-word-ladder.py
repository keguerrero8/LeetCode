class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        
        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)
                
        visit = set([beginWord])
        q = [beginWord]
        res = 1
        
        while q:
            for i in range(len(q)):
                word = q.pop(0)
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neighbor in nei[pattern]:
                        if neighbor not in visit:
                            visit.add(neighbor)
                            q.append(neighbor)
                
            res += 1
        
        return 0