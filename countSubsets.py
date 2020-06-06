# Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.


"""
Ways to make Sum:
            0 1 2 3 4
{1}         1 1 0 0 0
{1,1}       1 2 1 0 0
{1,1,2}     1 2 2 2 1
{1,1,2,3}   1 2 2 4 3
"""
def count_subsets(nums, targetSum):
    S = sum(nums) 
    if S < targetSum:
        return 0
    
    n = len(nums)

    # dp[i][s] represents number of ways the sum s can be formed by using elements upto i'th element.
    dp = [[0 for s in range(targetSum+1)] for i in range(n)]

    for i in range(n):
        dp[i][0] = 1
    
    for s in range(targetSum+1):
        dp[0][s] = 1 if nums[0] == s else 0
    
    for i in range(1,n):
        for s in range(1,targetSum+1):
            # If we (can) include nums[i], then:
            numWays1 = 0
            if nums[i] <= s:
                numWays1 = dp[i-1][s-nums[i]]
            
            # If we exclude nums[i], then:
            numWays2 = dp[i-1][s]

            dp[i][s] = numWays1 + numWays2

    return dp[n-1][targetSum]

def main():
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()

# With O(S) space:
def count_subsets(num, sum):
  n = len(num)
  dp = [0 for x in range(sum+1)]
  dp[0] = 1

  # with only one number, we can form a subset only when the required sum is equal to the number
  for s in range(1, sum+1):
    dp[s] = 1 if num[0] == s else 0

  # process all subsets for all sums
  for i in range(1, n):
    for s in range(sum, -1, -1):
      if s >= num[i]:
        dp[s] += dp[s - num[i]]

  return dp[sum]