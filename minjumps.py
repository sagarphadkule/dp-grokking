import math

# Given an array of positive numbers, where each element represents the max number of jumps 
# that can be made forward from that element, write a program to find the minimum number of 
# jumps needed to reach the end of the array (starting from the first element). 
# If an element is 0, then we cannot move through that element.

# Input = {2,1,1,1,4}
# Output = 3
# Explanation: Starting from index '0', we can reach the last index through: 0->2->3->4

# DP ITERATIVE 1
# Time: O(n2)
# Space: O(n)
def count_min_jumps(jumps):
    n = len(jumps)
    
    # dp[i] represents min jumps to get to i'th element from 0'th element    
    dp = [math.inf for i in range(n)]
    dp[0] = 0

    for i in range(1, n):
        for k in range(0, i):
            if (jumps[k] >= (i-k)):
                dp[i] = min(dp[i], 1 + dp[k])
    
    return dp[n-1]


# DP ITERATIVE 2
# Time: O(n2) but less than approach 1 if element values are small compared to len(jumps)
# Space: O(n)
def count_min_jumps2(jumps):
    n = len(jumps)
    
    # dp[i] represents min jumps FROM the i'th element TO THE LAST element:
    dp = [math.inf for i in range(n)]
    dp[n-1] = 0

    for i in range(n-2, -1, -1):
        for k in range(1, jumps[i]+1):
            if (i+k) >= n:
                break
            dp[i] = min(dp[i], 1 + dp[i+k])
    
    return dp[0]

    # [2, 1, 1, 1, 4]
    #  0, 1, 2, 3, 4
    #
    # [2, 1, 1, 1, 4]
    #  0, 1, 2, 3, 4
    # [I, I, I, I, 0]
    #
    # [2, 1, 1, 1, 4]
    #  0, 1, 2, 3, 4
    # [I, I, I, 1, 0]
    #
    # [2, 1, 1, 1, 4]
    #  0, 1, 2, 3, 4
    # [3, 3, 2, 1, 0]


# DP ITERATIVE 3
# Time: O(n2)
# Space: O(n)
def count_min_jumps3(jumps):
    n = len(jumps)

    # dp[i] represents min jumps to get to i'th element from 0th element
    dp = [math.inf for i in range(n)]
    dp[0] = 0

    for i in range(n):
        for k in range(1, jumps[i]+1):
            to = i + k
            if to >= n:
                break
            dp[to] = min(dp[to], dp[i] + 1)

    return dp[n-1]          


    # [2, 1, 1, 1, 4]
    #  0, 1, 2, 3, 4
    # [0, I, I, I, I]
    # 
    # [2, 1, 1, 1, 4]
    #  0, 1, 2, 3, 4
    # [0, I, I, I, I]
    # 





def main():

    print(count_min_jumps3([2, 1, 1, 1, 4]))
    print(count_min_jumps3([1, 1, 3, 6, 9, 3, 0, 1, 3]))



main()