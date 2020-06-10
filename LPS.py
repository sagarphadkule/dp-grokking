callCount = 0

# # NO MEMO:
# def find_LPS_length(st):
#   global callCount
#   callCount = 0
#   answer = find_LPS_length_recursive(st, 0, len(st) - 1)
#   print(f"Call Count: {callCount}")
#   return answer


# def find_LPS_length_recursive(st, startIndex, endIndex):
#   global callCount
#   callCount += 1
#   if startIndex > endIndex:
#     return 0

#   # every sequence with one element is a palindrome of length 1
#   if startIndex == endIndex:
#     return 1

#   # case 1: elements at the beginning and the end are the same
#   if st[startIndex] == st[endIndex]:
#     return 2 + find_LPS_length_recursive(st, startIndex + 1, endIndex - 1)

#   # case 2: skip one element either from the beginning or the end
#   c1 = find_LPS_length_recursive(st, startIndex + 1, endIndex)
#   c2 = find_LPS_length_recursive(st, startIndex, endIndex - 1)
#   return max(c1, c2)


# WITH MEMO:
def find_LPS_length(st):
  global callCount
  callCount = 0
  n = len(st)
  dp = [[-1 for _ in range(n)] for _ in range(n)]
  answer = find_LPS_length_recursive(dp, st, 0, n - 1)
  print(f"Call Count: {callCount}")
  return answer


def find_LPS_length_recursive(dp, st, startIndex, endIndex):
  global callCount
  callCount += 1
  if startIndex > endIndex:
    return 0

  # every sequence with one element is a palindrome of length 1
  if startIndex == endIndex:
    return 1

  if (dp[startIndex][endIndex] == -1):
    # case 1: elements at the beginning and the end are the same
    if st[startIndex] == st[endIndex]:
      dp[startIndex][endIndex] = 2 + find_LPS_length_recursive(dp, st, startIndex + 1, endIndex - 1)
    else:
      # case 2: skip one element either from the beginning or the end
      c1 = find_LPS_length_recursive(dp, st, startIndex + 1, endIndex)
      c2 = find_LPS_length_recursive(dp, st, startIndex, endIndex - 1)
      dp[startIndex][endIndex] = max(c1, c2)

  return dp[startIndex][endIndex]


def main():
  # print(find_LPS_length("abdbca"))
  # print(find_LPS_length("cddpd"))
  # print(find_LPS_length("pqr"))
  print(find_LPS_length("tommarvolloriddle"))


main()