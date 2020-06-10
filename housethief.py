# There are ‘n’ houses built in a line. A thief wants to steal maximum possible money from these houses. 
# The only restriction the thief has is that he can’t steal from two consecutive houses, as that 
# would alert the security system. How should the thief maximize his stealing?

# Input: {2, 5, 1, 3, 6, 2, 4}
# Output: 15
# Explanation: The thief should steal from houses 5 + 6 + 4

# RECURSIVE 1:
def find_max_steal(wealth):
    memo = [-1] * len(wealth)
    return find_max_steal_rec(wealth, 0, memo)

def find_max_steal_rec(wealth, currentIndex, memo):
    n = len(wealth)
    if (currentIndex >= n): return 0

    if memo[currentIndex] == -1:
        stealThis = wealth[currentIndex] + find_max_steal_rec(wealth, currentIndex+2, memo)
        skipThis = find_max_steal_rec(wealth, currentIndex+1, memo)

        memo[currentIndex] = max(stealThis, skipThis)
    
    return memo[currentIndex]


# RECURSIVE 2:
# We go from right to left in the wealth array this time.
# This implies, either side could be considered as the top in this top-down recursive approach
def find_max_steal2(wealth):
    n = len(wealth)
    memo = [-1] * n
    return find_max_steal_rec2(wealth, n-1, memo)

def find_max_steal_rec2(wealth, currentIndex, memo):
    n = len(wealth)
    if (currentIndex < 0): return 0

    if memo[currentIndex] == -1:
        stealThis = wealth[currentIndex] + find_max_steal_rec2(wealth, currentIndex-2, memo)
        skipThis = find_max_steal_rec2(wealth, currentIndex-1, memo)

        memo[currentIndex] = max(stealThis, skipThis)
    
    return memo[currentIndex]


# ITERATIVE 1:
def find_max_steal3(wealth):
    n = len(wealth)
    if (n == 1): return wealth[0]
    if (n < 1): return 0

    dp = [0] * n

    # dp[i] represents the max-wealth that can be stolen for [0...i] houses.
    # dp[i] shall be max(wealth[i]+dp[i-2], dp[i-1])

    dp[0] = wealth[0]
    dp[1] = max(wealth[0], wealth[1])
    for i in range(2,n):
        dp[i] = max(wealth[i] + dp[i-2], dp[i-1])
    
    return dp[n-1]




def main():
    # print(find_max_steal([2, 5, 1, 3, 6, 2, 4]))
    # print(find_max_steal([2, 10, 14, 8, 1]))

    # print(find_max_steal2([2, 5, 1, 3, 6, 2, 4]))
    # print(find_max_steal2([2, 10, 14, 8, 1]))

    print(find_max_steal3([2, 5, 1, 3, 6, 2, 4]))
    print(find_max_steal3([2, 10, 14, 8, 1]))


main()