class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        combos = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs",
        "8":"tuv", "9":"wxyz"}
        res = []
        self.comboHelper(digits, combos, [], res, 0)
        return res
    
    def comboHelper(self, digits, combos, combo, res, idx):
        if idx == len(digits):
            res.append("".join([] + combo))
            return
        
        for letter in combos[digits[idx]]:
            combo.append(letter)
            self.comboHelper(digits, combos, combo, res, idx + 1)
            combo.pop()