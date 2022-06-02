class Solution(object):
    def letterCombinations(self, digits):
        if digits == "":
            return []
        mnemonics = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6":"mno",
                     "7":"pqrs", "8":"tuv", "9":"wxyz"}
        return self.phoneNumberMnemonicsHelper(0, digits, mnemonics, [], [])


    def phoneNumberMnemonicsHelper(self, i, phoneNumber, mnemonics, base, result):
        if i == len(phoneNumber):
            result.append("".join(base))
            return result

        for char in mnemonics[phoneNumber[i]]:
            base.append(char)
            self.phoneNumberMnemonicsHelper(i+1, phoneNumber, mnemonics, base, result)
            base.pop()

        return result
        