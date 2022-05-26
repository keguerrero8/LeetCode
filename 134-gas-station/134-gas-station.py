class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        
        leastGas = float("inf")
        validCity = None
        currentGas = 0

        for i in range(len(cost)):
            if currentGas < leastGas:
                leastGas = currentGas
                validCity = i
            currentGas += gas[i] - cost[i]
        return validCity
        