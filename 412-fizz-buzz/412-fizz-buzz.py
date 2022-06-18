class Solution(object):
    def fizzBuzz(self, n):
        index = 1
        res = []
        while index <= n:
            if index % 3 == 0 and index % 5 == 0:
                res.append("FizzBuzz")
            elif index % 3 == 0:
                res.append("Fizz")
            elif index % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(index))
            index +=1
            
        return res
        