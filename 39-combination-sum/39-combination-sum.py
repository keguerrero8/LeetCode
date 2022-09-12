class Solution(object):
    def combinationSum(self, candidates, target):
        total = 0
        res = []
        candidate = []
        self.combinationSumHelper(candidates, target, total, res, candidate, 0)
        return res
        
    def combinationSumHelper(self, candidates, target, total, res, candidate, idx):
        if total == target:
            res.append(candidate + [])
            return
        elif total > target:
            return
        else:
            for i in range(idx, len(candidates)):
                candidate.append(candidates[i])
                self.combinationSumHelper(candidates, target, total + candidates[i], res, candidate, i)
                candidate.pop()