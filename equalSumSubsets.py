# https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/3jEPRo5PDvx
# Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both the subsets is equal.

def can_partition(nums):
	S = sum(nums)
	if (S%2 == 1):
		return False

	halfSum = int(S/2)
	n = len(nums)
	# Find out if nums upto element at index i can sum up to s:
	dp = [[False for i in range(halfSum + 1)] for j in range(2)]
	
	for i in range(2):
		dp[i][0] = True
	
	for s in range(halfSum+1):
		dp[0][s] = True if nums[0] == s else False


#				0 1 2 3 4 5
#	1			T T F F F F
#	1,2			T T T T F F 
#	1,2,3		T 
#	1,2,3,4		T

	for i in range(1,n):
		for s in range(1, halfSum+1):
			# If we (can) include nums[i]:
			possibility1 = False
			if (nums[i] <= s):
				possibility1 = dp[(i-1)%2][s-nums[i]]
			
			possibility2 = dp[(i-1)%2][s]
			
			dp[i%2][s] = possibility1 or possibility2
	
	return dp[(n-1)%2][halfSum]

def main():
	print("Can partition: " + str(can_partition([1, 2, 3, 4])))
	print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
	print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()