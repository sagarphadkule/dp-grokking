# https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/7nAOY4oy64A
# Given a set of positive numbers (non zero) and a target sum ‘S’.
# Each number should be assigned either a ‘+’ or ‘-’ sign.
# We need to find out total ways to assign symbols to make the sum of numbers equal to target ‘S’.

# Input: {1, 1, 2, 3}, S=1
# Output: 3
# Explanation: The given set has '3' ways to make a sum of '1': {+1-1-2+3} & {-1+1-2+3} & {+1+1+2-3}

"""
DP Table: dp[i][s] represents number of ways to make sum s by using elements upto i'th element

            - - -
            3 2 1 0 1 2 3
{1}         0 0 1 0 1 0 0
{1,1}             2 0 1
{1,1,2}             
{1,1,2,3}    

"""
from collections import defaultdict

def find_target_subsets(nums, targetSum):
    n = len(nums)
    S = sum(nums)

    dp = [defaultdict(lambda: 0) for i in range(n)]
    
    for s in range(-S, S+1):
        dp[0][s] = 1 if (nums[0] == s or s == -nums[0]) else 0
    
    for i in range(1,n):
        for s in range(-S, S+1):
            # If +ve sign for nums[i]:
            numWays1 = dp[i-1][s-nums[i]]

            # If -ve sign for nums[i]:
            numWays2 = dp[i-1][s+nums[i]]

            dp[i][s] = numWays1 + numWays2

    return dp[n-1][targetSum]

def main():
    print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
    print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()

# Their solution:
# https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/7nAOY4oy64A
# See explanation there. They essentially transformed / reduced this problem to the count_subsets of sum S problem.
def find_target_subsets2(num, s):
  totalSum = sum(num)

  # if 's + totalSum' is odd, we can't find a subset with sum equal to '(s + totalSum) / 2'
  if totalSum < s or (s + totalSum) % 2 == 1:
    return 0

  return count_subsets(num, int((s + totalSum) / 2))


# this function is exactly similar to what we have in 'Count of Subset Sum' problem.
def count_subsets(num, s):
  n = len(num)
  dp = [[0 for x in range(s+1)] for y in range(n)]

  # populate the sum = 0 columns, as we will always have an empty set for zero sum
  for i in range(0, n):
    dp[i][0] = 1

  # with only one number, we can form a subset only when the required sum is
  # equal to the number
  for s in range(1, s+1):
    dp[0][s] = 1 if num[0] == s else 0

  # process all subsets for all sums
  for i in range(1, n):
    for s in range(1, s+1):
      dp[i][s] = dp[i - 1][s]
      if s >= num[i]:
        dp[i][s] += dp[i - 1][s - num[i]]

  # the bottom-right corner will have our answer.
  return dp[n - 1][s]


def main():
  print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
  print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()