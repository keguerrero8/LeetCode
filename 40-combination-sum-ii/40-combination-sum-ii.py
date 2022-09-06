class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()
        self.combinationSumHelper(candidates, target, res, [], 0, 0)
        return res
    
    
    def combinationSumHelper(self, candidates, target, res, candidate, idx, currentSum):
        if target == currentSum:
            res.append([] + candidate)
        elif currentSum > target:
            return
        else:
            prev = -1
            for i in range(idx, len(candidates)):
                if candidates[i] == prev:
                    continue
                newCand = candidate + [candidates[i]]
                self.combinationSumHelper(candidates, target, res, newCand, i + 1, currentSum + candidates[i])
                newCand.pop()
                prev = candidates[i]
        