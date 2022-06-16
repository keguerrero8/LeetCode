class Solution(object):
    def change(self, amount, coins):
        ways = [0]*(amount+1)
        ways[0] = 1

        for denom in coins:
            for i in range(1, len(ways)):
                if denom <= i:
                    ways[i] += ways[i-denom]

        return ways[-1]
        