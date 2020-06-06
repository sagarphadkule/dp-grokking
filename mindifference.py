# https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/xVVNRPPXQGr
# Given a set of positive numbers, partition the set into two subsets with a minimum difference between their subset sums.

def can_partition(nums):
#               0 1 2 3 4 5 6
#   1           0 1 1 1 1 1 1
#   1,2         0 1 2 3 3 3 3
#   1,2,3       0 
#   1,2,3,4     0 . . . 
    S = sum(nums)
    halfSum = int(sum(nums) / 2)
    n = len(nums)

    dp = [[0 for i in range(halfSum+1)] for j in range(n)]

    for i in range(n):
        dp[i][0] = 0
    
    for s in range(halfSum+1):
        dp[0][s] = nums[0] if nums[0] <= s else 0

    for i in range(1,n):
        for s in range(1, halfSum+1):            
            sum1 = 0
            # If we (can) include nums[i]:
            if nums[i] <= s:
                sum1 = nums[i] + dp[i-1][s-nums[i]]

            # If we exclude nums[i]:
            sum2 = dp[i-1][s]
            dp[i][s] = max(sum1, sum2)


    diff1 = abs((S - dp[n-1][halfSum]) - dp[n-1][halfSum])
    # diff2 = abs((S - dp[n-1][halfSum+1]) - dp[n-1][halfSum+1])
    # return min(diff1, diff2)

    # ^ We don't need to check till halfSum+1 or more because the difference is gonna be symmetric across the halfSum. Think.

    return diff1




def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
#               0 1 2 3 4 5 6 7 8
#   1           0 1 1 1 1 1 1 1 1
#   1,2         0 1 2 3 3 3 3 3 3
#   1,2,3       0 1 2 3 4 5 6 6 6
#   1,2,3,9     0 1 2 3 4 5 6 6 6

    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))
    print("Can partition: " + str(can_partition([16, 5, 10,9])))

main()