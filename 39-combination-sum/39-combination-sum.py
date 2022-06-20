class Solution(object):
    def combinationSum(self, candidates, target):                    
        combinations = []
        self.combinationSumHelper(0, 0, [], combinations, candidates, target)
        return combinations
    
    
    def combinationSumHelper(self, total, idx, candidate, combos, candidates, target):
        if total == target:
            combos.append(candidate + [])
        elif total > target:
            return
        else:
            for i in range(idx, len(candidates)):
                newCandidate = candidate + [candidates[i]] #[2], combos(0+2, 0, [2]) -> [2, 2], combos(4, 0, [2,2])
                self.combinationSumHelper(total + candidates[i], i, newCandidate, combos, candidates, target)
                newCandidate.pop()
        