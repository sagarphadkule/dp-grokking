# Given a staircase with ‘n’ steps and an array of ‘n’ numbers representing the fee 
# that you have to pay if you take the step. Implement a method to calculate the 
# minimum fee required to reach the top of the staircase (beyond the top-most step).
# At every step, you have an option to take either 1 step, 2 steps, or 3 steps. 
# You should assume that you are standing at the first step.

#       [1, 3, 5, 2, 1, 2, 3, 2, 4, 5, 1]

# RECURSIVE:
def find_min_fee(fees):
    memo = [-1] * len(fees)
    return find_min_fee_rec(fees, 0, memo)

def find_min_fee_rec(fees, currentIndex, memo):
    if (currentIndex >= len(fees)):
        return 0

    if memo[currentIndex] == -1:
        feeIfOneStep = fees[currentIndex] + find_min_fee_rec(fees, currentIndex+1, memo)
        feeIfTwoSteps = fees[currentIndex] + find_min_fee_rec(fees, currentIndex+2, memo)
        feeIfThreeSteps = fees[currentIndex] + find_min_fee_rec(fees, currentIndex+3, memo)
        memo[currentIndex] =  min(feeIfOneStep, feeIfTwoSteps, feeIfThreeSteps)
    
    return memo[currentIndex]


# ITERATIVE Mine:
# Like a reverse fibonacci pattern
# 
def find_min_fee2(fees):
    n = len(fees)
    dp = [-1] * (n+3)
    # dp[i] represents the min total fee required from i'th step to reach top of the stairs (just as in the recursive implementation above)

    dp[n], dp[n+1], dp[n+2] = 0, 0, 0     # Top of the stairs (beyond last step)
    
    for i in range(n-1, -1, -1):
        dp[i] = fees[i] + min(dp[i+1], dp[i+2], dp[i+3])

    return dp[0]

def main():
    print(find_min_fee2([1, 2, 5, 2, 1, 2]))
    print(find_min_fee2([2, 3, 4, 5]))


main()