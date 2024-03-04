        def dfs(curAmount, i, memo):
            if curAmount < 0: return float('inf')

            if curAmount == 0: 
                return 0

            for j in coins: 
                minCoins = min(minCoins, 1 + dfs(curAmount - j, i + 1, memo))



            if memo[curAmount] != -1:
                return memo[curAmount]

            minCoins = float('inf')
            memo[curAmount] = minCoins

            return minCoins
        memo = [-1] * (amount + 1)
        result = dfs(amount, 0, memo)
        return result if result != float('inf') else -1
        
        if amount == 0: return 0


[
