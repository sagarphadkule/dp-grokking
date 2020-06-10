from Tree import TreeNode

# Given two strings ‘s1’ and ‘s2’, find the length of the longest substring which is common in both the strings.


# # RECURSIVE 1: TOP DOWN
# def find_LCS_length(s1, s2):
#     maxCount = [0]
#     find_LCS_length_rec(s1, s2, 0, 0, 0, 0, maxCount)
#     return maxCount[0]


# def find_LCS_length_rec(s1, s2, i, j, count, currentMaxCount, maxCount):
#     # if beyond bounds, base case:
#     n1 = len(s1)
#     n2 = len(s2)
#     if (i >= n1 or j >= n2):
#         maxCount[0] = max(maxCount[0], currentMaxCount)
#         return

#     # if within bounds, check condition
#     if s1[i] == s2[j]:
#         currentMaxCount = max(count+1, currentMaxCount)
#         find_LCS_length_rec(s1, s2, i+1, j+1, count+1, currentMaxCount, maxCount)
#     else:  
#         find_LCS_length_rec(s1, s2, i+1, j, 0, currentMaxCount, maxCount)
#         find_LCS_length_rec(s1, s2, i, j+1, 0, currentMaxCount, maxCount)
#         x = 1
    

# # RECURSIVE 2: Bottom-Up. (more precisely: Top-Down-Top)
# def find_LCS_length(s1, s2):
#     return find_LCS_length_rec(s1, s2, 0, 0, 0)


# def find_LCS_length_rec(s1, s2, i, j):
#     # if beyond bounds, base case:
#     n1 = len(s1)
#     n2 = len(s2)
#     if (i >= n1 or j >= n2):
#         return 0

#     # if within bounds, check condition
#     if s1[i] == s2[j]:
#         count = 1 + find_LCS_length_rec(s1, s2, i+1, j+1)       # THIS IS WRONG. This results in longest common SUBSEQUENCE.
#         # For longest common SUBSTRING, the manager (this function) shouldn't be adding 1. The child should be adding 1 conditionally.
#         # and so, we need to pass in a count variable to child which may be reset to 0 down the line.
#         # SEE NEXT IMPLEMENTATION.
#     else:
#         c1 = find_LCS_length_rec(s1, s2, i+1, j)
#         c2 = find_LCS_length_rec(s1, s2, i, j+1)
#         count = max(c1, c2)
    
#     return count
# abcd
# azcd 


# # RECURSIVE 2: Bottom-Up. (more precisely: Top-Down-Top)
# def find_LCS_length(s1, s2):
#     return find_LCS_length_rec(s1, s2, 0, 0, 0)


# def find_LCS_length_rec(s1, s2, i, j, count):
#     # if beyond bounds, base case:
#     n1 = len(s1)
#     n2 = len(s2)
#     if (i >= n1 or j >= n2):
#         return count

#     # if within bounds, check condition
#     if s1[i] == s2[j]:
#         count = find_LCS_length_rec(s1, s2, i+1, j+1, count+1)
#         return count
#     else:
#         c1 = find_LCS_length_rec(s1, s2, i+1, j, 0)
#         c2 = find_LCS_length_rec(s1, s2, i, j+1, 0)
#         return max(count, c1, c2)
# # abcdx
# # azcdy 

# RECURSIVE 2-memo: Memoization with Bottom-Up. (more precisely: Top-Down-Top)
def find_LCS_length(s1, s2):
    treeRoot = TreeNode("start")
    answer = find_LCS_length_rec(s1, s2, 0, 0, 0, treeRoot)
    treeRoot.generateDot("LCSubstring")
    return answer


def find_LCS_length_rec(s1, s2, i, j, count, treeParentNode):
    currTreeNode = TreeNode((i,j, s1[i:], s2[j:]))
    treeParentNode.children.append(currTreeNode)
    # if beyond bounds, base case:
    n1 = len(s1)
    n2 = len(s2)
    if (i >= n1 or j >= n2):
        return count

    # if within bounds, check condition
    if s1[i] == s2[j]:
        count = find_LCS_length_rec(s1, s2, i+1, j+1, count+1, currTreeNode)
        return count
    else:
        c1 = find_LCS_length_rec(s1, s2, i+1, j, 0, currTreeNode)
        c2 = find_LCS_length_rec(s1, s2, i, j+1, 0, currTreeNode)
        return max(count, c1, c2)
# abcdx
# azcdy 


# abdca
# cbda

def main():
    print(find_LCS_length("ab", "cd"))
    # print(find_LCS_length("abc", "bca"))
    # print(find_LCS_length("abdca", "cbda"))
    # print(find_LCS_length("passport", "ppsspt"))


main()