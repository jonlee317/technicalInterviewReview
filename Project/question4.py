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
    least_common_ancestor = r
    nextList = [r]
    traveled =[r]
    parent_child = {}
    level = 0
    while len(nextList) > 0:
        level += 1
        current = nextList.pop()
        #print current
        subTraveled = []
        for i in range(len(T[current])):
            if T[current][i] == 1:
                subTraveled.append((current,i))
                parent_child[i] = current
                nextList.append(i)

        if len(subTraveled) > 0:
            traveled.append(subTraveled)

    # TODO: if the level of one child is lower than the other move them up
    #       until they are at the same level and check if the parent is the same
    #       if the parent is the same then we are done.  if they are not the same
    #       then we move them both up at the same time and check if the parent is the same
    #       we keep repeating this step until the parent is the same

    print traveled
    print parent_child
    n1_path = n1
    n2_path = n2
    #while parent_child[n1] != parent_child[n1]:

    return least_common_ancestor

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

question4(T1, r1, n1_1, n2_1)

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

question4(T2, r2, n1_2, n2_2)
