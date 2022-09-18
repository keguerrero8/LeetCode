class Solution(object):
    def invalidTransactions(self, transactions):
        trans = [transactions[i].split(",") for i in range(len(transactions))]
        res = []
        
        for i in range(len(trans)):
            name, t1, amount, cityName = trans[i]
            if int(amount) > 1000:
                res.append(transactions[i])
                continue
            
            for j in range(len(trans)):
                name2, t2, amount2, cityName2 = trans[j]
                
                if j != i and name == name2 and abs(int(t1)-int(t2)) <= 60 and cityName != cityName2:
                    res.append(transactions[i])
                    break
                    
        return res
                
        