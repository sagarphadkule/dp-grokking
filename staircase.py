# Given a stair with ‘n’ steps, implement a method to count how many possible ways are there to reach the top of the staircase, 
# given that, at every step you can either take 1 step, 2 steps, or 3 steps.

# RECURSIVE:
def count_ways(n):
    if (n < 0): return -1
    memo = [-1 for i in range(n+1)]
    memo[0] = 1
    memo[1] = 1
    memo[2] = 2
    return count_ways_rec(n, memo)

def count_ways_rec(n, memo):
    if (memo[n] != -1):
        return memo[n]

    memo[n] = count_ways_rec(n-1, memo) + count_ways_rec(n-2, memo) + count_ways_rec(n-3, memo)
    return memo[n]


# ITERATIVE:
def count_ways2(n):
    if (n == 2):
        return 2
    if (n == 0 or n == 1):
        return 1
    
    a = 1
    b = 1
    c = 2
    ans = -1
    for i in range(3, n+1):
        ans = a + b + c
        a = b
        b = c
        c = ans
    
    return ans




def main():

    print(count_ways2(3))
    print(count_ways2(4))
    print(count_ways2(5))


main()