class Solution(object):
    def coinChange(self, coins, amount):
        #for ex if target is 11, array would be
        #[0,1,1,2,2,1,2,2,3,3,2,3]
        #[0,0,0,0]
        #set 0th position to 1
        amounts = [float("inf")]*(amount+1)
        amounts[0] = 0
        for coin in coins:
            for targetAmount in range(1, len(amounts)):
                if coin <= targetAmount:
                    minCoins = 1 + amounts[targetAmount-coin]
                    amounts[targetAmount] = min(minCoins, amounts[targetAmount])
                # if coin <= targetAmount:
                #     currentCoinChange = targetAmount // coin
                #     remainder = targetAmount - currentCoinChange*coin 
                #     remainderWays = amounts[remainder]
                #     currentWays = remainderWays + currentCoinChange
                #     if amounts[targetAmount] == 0:
                #         amounts[targetAmount] = currentWays
                #     else:
                #         amounts[targetAmount] = min(currentWays, amounts[targetAmount])
                    
        return amounts[-1] if amounts[-1] != float("inf") else -1
        