class Solution(object):
    def change(self, amount, coins):
        ways = [0]*(amount+1)
        ways[0] = 1
        for denom in coins:
            for target in range(1, len(ways)):
                if denom <= target:
                    ways[target] += ways[target-denom]
        return ways[-1]
        