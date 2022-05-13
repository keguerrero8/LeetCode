class Solution(object):
    def groupAnagrams(self, strs):
        # sortedAnagrams = map(lambda x: x.sort(), strs)
        sortedAnagrams = []
        
        for string in strs:
            sortedAnagrams.append("".join(sorted(string)))
        
        anagramsHash = {}
        
        for i in range(len(strs)):
            if sortedAnagrams[i] not in anagramsHash:
                anagramsHash[sortedAnagrams[i]] = [strs[i]]
            else:
                anagramsHash[sortedAnagrams[i]].append(strs[i])
        
        anagrams = []
        
        for value in anagramsHash.values():
            anagrams.append(value)
            
        return anagrams
        