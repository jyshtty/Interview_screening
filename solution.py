
stairs = 5
steps = [1,2,3]

def unique_ways(stairs, steps):
        dp = [0] * (stairs + 1)
        dp[0] = 1
        for step in steps:
            for stair in range(stairs+1):
                if stair >= step:
                    dp[stair] = dp[stair] + dp[stair - step]
        return dp[stairs]


print(unique_ways(stairs, steps))
