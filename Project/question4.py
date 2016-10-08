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

def question4(T, r, n1, n2):
    least_common_ancestor = r   # initializing least common ancestor to the root

    child_parent = {}   # creating a dictionary to hold each child's parent
    child_level = {}    # creating a dictionary to hold each child's level

    nextList = [r]  # The list of items which will be iterated through in a queue

    level = 0

    # looping through the tree
    while len(nextList) > 0:
        current = nextList.pop()
        # only check each parent's child if it actually has a child
        if len(T) > 0: # check if there is even anything in the T
            if sum(T[current]) > 0:
                level +=1
                for i in range(len(T[current])):
                    if T[current][i] == 1:
                        child_level[i] = level
                        child_parent[i] = current
                        nextList.append(i)

    # Strategy: if the level of one child is lower than the other move them up
    #   until they are at the same level and check if the parent is the same
    #   if the parent is the same then we are done.  if they are not the same
    #   then we move them both up at the same time and check if the parent is the same
    #   we keep repeating this step until the parent is the same
    if len(T) >0:
        n1_curr = n1
        n2_curr = n2

        while child_parent[n1_curr] != child_parent[n2_curr]:
            if child_level[n1_curr] > child_level[n2_curr]:
                n1_curr = child_parent[n1_curr]
            elif child_level[n2_curr] > child_level[n1_curr]:
                n2_curr = child_parent[n2_curr]
            else:
                n1_curr = child_parent[n1_curr]
                n2_curr = child_parent[n2_curr]

        if child_parent[n1_curr] == child_parent[n2_curr]:
            least_common_ancestor = child_parent[n1_curr]

        return least_common_ancestor
    else:
        return ""

# Test code
# Test Case 1
T1 = [[0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [1, 0, 0, 0, 1],
     [0, 0, 0, 0, 0]]
r1 = 3
n1_1 = 1
n2_1 = 4

# answer should be 3

print question4(T1, r1, n1_1, n2_1)

# Test Case 2
T2 = [[0, 1, 1, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [1, 0, 0, 0, 1],
     [0, 0, 0, 0, 0]]
r2 = 3
n1_2 = 1
n2_2 = 2

# answer should be 0

print question4(T2, r2, n1_2, n2_2)


# Test Case 3
T3 = [[0, 1, 0, 0, 1, 0, 0, 0],
     [0, 0, 1, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0]]
r3 = 0
n1_3 = 7
n2_3 = 6

# answer should be 2

print question4(T3, r3, n1_3, n2_3)

# Test Case 4
T4 = []
r4 = 0
n1_4 = 7
n2_4 = 6
print question4(T4, r4, n1_4, n2_4)
