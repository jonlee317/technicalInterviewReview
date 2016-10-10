# Question 4
# Find the least common ancestor between two nodes on a binary search tree.
# The least common ancestor is the farthest node from the root that is an ancestor of both nodes.
# For example, the root is a common ancestor of all nodes on the tree,
# but if both nodes are descendents of the root's left child,
# then that left child might be the lowest common ancestor.
# You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties.
# The function definition should look like question4(T, r, n1, n2),
# where T is the tree represented as a matrix,
# where the index of the list is equal to the integer stored in that node and a 1 represents a child node,
# r is a non-negative integer representing the root,
# and n1 and n2 are non-negative integers representing the two nodes in no particular order.
# For example, one test case might be
#
# question4([[0, 1, 0, 0, 0],
#           [0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0],
#           [1, 0, 0, 0, 1],
#           [0, 0, 0, 0, 0]],
#          3,
#          1,
#          4)
# and the answer would be 3.
#

# Here we determine if the BST child is on the left or right
def findChild(T, r):
    right = None
    left = None
    for i in range(len(T[r])):
        if T[r][i] == 1:
            if i > r:
                right = i
            else:
                left = i
    return left, right

# Here is the algorithm to find the least common ancenstor

def leastCommonAncestor(T, r, n1, n2):
    left, right = findChild(T,r)
    # if there is no root then there's nothing
    if r == None:
        return None
    
    # If both numbers lie to the left of the root then we know the 
    # answer has to be in the left tree
    if (r > n1 and r > n2):
        return leastCommonAncestor(T, left, n1, n2)
    
    # If both numbers lie to the right of the root then we know
    # answer has to be in the right tree
    if (r < n1 and r < n2):
        return leastCommonAncestor(T, right, n1, n2)
    
    # in the desired case when one number is left and another is on right
    # we return the root
    return r

def question4(T, r, n1, n2):
    # If there is nothing then return nothing
    if r == None:
        return None
    # if any of the numbers equal the root then simply return the root
    if r == n1 or r == n2:
        return r
    else:
        # Only if the number is within range of the length
        # we will iterate the least Common Ancestor Function
        if n1 >= 0 and n1<len(T) and n2>=0 and n2<len(T):
            return leastCommonAncestor(T,r,n1,n2)
        else:
            return None
        

# Test code
print("---- Test Cases for Question 4 ----")
# Test Case 1
T1 = [[0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [1, 0, 0, 0, 1],
     [0, 0, 0, 0, 0]]
r1 = 3
n1_1 = 1
n2_1 = 4

print question4(T1, r1, n1_1, n2_1)
# 3

print question4(T1, r1, 1, 0)
# 0

# Test Case 3
T3 = [[0, 1, 0, 0, 0, 0, 0, 0],
     [1, 0, 1, 1, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 1, 0, 1, 0, 0],
     [0, 0, 0, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 0, 1, 0, 1],
     [0, 0, 0, 0, 0, 0, 1, 0]]
r3 = 3


# answer should be 2

print question4(T3, r3, 0, 2)
# 1

print question4(T3, r3, 2, 5)
# 3

print question4(T3, r3, 1, 5)
# 3

print question4(T3, r3, 1, 2)
# 1

print question4(T3, r3, 11, 12)
# None

print question4(T3, r3, 7, 8)
# None

print question4(T3, r3, 8, 6)
# None  ""out of bounds""

print question4(T3, r3, 0, 0)
# 0   ""Since we are at the root""

print question4(T3, r3, 0, -1)
# None      ""Out of bounds""

T4 = []
r4 = 0
n1_4 = 7
n2_4 = 6
print question4(T4, r4, n1_4, n2_4)
# None  T4 is empty list
