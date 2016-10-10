# ------------------------------------ Question 1 -------------------------------------------
#
# Given two strings s and t, determine whether some anagram of t is a substring of s.
# For example: if s = "udacity" and t = "ad", then the function returns True.
# Your function definition should look like: question1(s, t) and return a boolean True or False.
#

def question1(s, t):
	# defining the lengths of the substring and strings
	substringLength = len(t)
	stringLength = len(s)
	# Defining the start and end index substring length relative to the string
	beginIndex = 0
	endIndex = beginIndex + substringLength
	# Create a clean tally to count matches
	matchedNum = []
	# Create a checklist for each index of the substring characters
	checkList = [0 for i in range(substringLength)]

	# Until the last character of the string is reached we check each partition the string
	# to see if all the characters match with the substring
	while endIndex <= stringLength:
		# the segment of the string which will be compared with the input substring
		testSubstring = list(s[beginIndex:endIndex])
		# converting the substring into a list of characters to use python list methods
		mySubstring = list(t)
		mySubstringLength = len(mySubstring)

		# Search through each character of the testsubstring
		while len(testSubstring) >0:
			testChar = testSubstring.pop()
			for i in range(mySubstringLength):
				if mySubstring[i] == testChar and checkList[i] ==0:
					matchedNum.append(1)
					checkList[i] += 1
		if matchedNum.count(1) == substringLength:
			break # If we found all the characters can exit
		else:
			matchedNum = []
			checkList = [0 for i in range(substringLength)]
		# Increment the begin and end index to check the next partition of the string
		beginIndex += 1
		endIndex += 1

	if matchedNum.count(1) == substringLength:
		return True
	else:
		return False

# Testcases
print("---- Test Cases for question 1 ----")
print(question1("udacity", "yit"))	#True
print(question1("jumanji", "naj"))	#True
print(question1("jumanji", "muj"))	#True
print(question1("udacity", "udc"))	#False
print(question1("superman", "rem"))	#True
print(question1("superman", "nar"))	#False
print(question1("", "nar"))			#False
print(question1("nar", ""))			#True

# ------------------------------------ Question 2 -------------------------------------------
#
# Given a string a, find the longest palindromic substring contained in a.
# Your function definition should look like question2(a), and return a string.

# TODO: clean up the code and comment what each code does
# TODO: see if there is any other more efficient method to implement

def findMatch(inputString, begin, end, output):
	# to take into account the letter corresponding to 'a' in the dcbabcd pattern
	if end-begin == 2:
		output += inputString[begin+1]
	if begin >=0 and end < len(inputString):
		if inputString[begin] == inputString[end]:
			output = inputString[begin]+output+inputString[end]
			output = findMatch(inputString, begin-1, end+1, output)
		else:
			output = output
	return output

def question2(a):
	outputStringList = []
	outputString_type1 = ""
	outputString_type2 = ""
	initialIndex = 0
	finalIndex = initialIndex + 1

	while finalIndex < len(a):
		# Implements the dcbaabcd pattern
		outputString_type1 = findMatch(a, initialIndex, finalIndex, outputString_type1)
		# Implements the dcbabcd pattern
		outputString_type2 = findMatch(a, initialIndex, finalIndex+1, outputString_type2)

		initialIndex += 1
		finalIndex += 1

		# if there is nothing in the list simply append
		if len(outputStringList) == 0:
			outputStringList.append(outputString_type1)
			outputStringList.append(outputString_type2)
		# If there is something in the list place longer string in front else append
		elif len(outputStringList) > 0:
			if len(outputStringList[0]) > len(outputString_type1):
				outputStringList.append(outputString_type1)
			else:
				outputStringList.insert(0,outputString_type1)
			if len(outputStringList[0]) > len(outputString_type2):
				outputStringList.append(outputString_type2)
			else:
				outputStringList.insert(0,outputString_type2)

		outputString_type1 = ""
		outputString_type2 = ""

	if len(outputStringList) > 0:
		# Since palindrome will never be one character
		if len(outputStringList[0]) > 1:
			return outputStringList[0]
		else:
			return ""
	else:
		return ""

# Test Cases
print("---- Test Cases for question 2 ----")
print(question2('zeabxbaezcc'))
# zeabxbaez
print(question2("bloblobbor"))
# obbo
print(question2("racecar"))
# racecar
print(question2("bloblobbbor"))
# obbbo
print(question2("feffzracecarefz"))
# racecar
print(question2(""))
# ""
print(question2("feffzrasdfdasflijdasfldfjshagwoghioiwehofhasdfljacecarefz"))
# aceaca
print(question2("abcdefghijk"))
# ""    <-- nothing since there is no palinrome
print(question2("abcdeffghijk"))
# ff

# ------------------------------------ Question 3 -------------------------------------------
#
# Given an undirected graph G, find the minimum spanning tree within G.
# A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges.
# Your function should take in and return an adjacency list structured like this:
#
# {'A': [('B', 2)],
#  'B': [('A', 2), ('C', 5)],
#  'C': [('B', 5)]}
# Vertices are represented as unique strings. The function definition should be question3(G)

def question3(G):
    if len(G) > 0:
        nodeList = [[0,G.keys()[0]]]
    else:
        nodeList = []

    # naively iterating through all items
    traveled = {item: 0 for item in G}
    minTree = {item: [] for item in G}
    while len(nodeList) > 0:
        val = nodeList.pop(0)
        traveled[val[1]] = 1
        for item in G[val[1]]:
            if traveled[item[0]] == 0 or traveled[val[1]]==0:
                nodeList.append([item[1],item[0],val[1]])
        nodeList = sorted(nodeList)

        if len(nodeList) >0 and (traveled[nodeList[0][2]] == 0 or traveled[nodeList[0][1]]==0):
            minTree[nodeList[0][2]].append([nodeList[0][1],nodeList[0][0]])
            minTree[nodeList[0][1]].append([nodeList[0][2],nodeList[0][0]])

    return minTree

# test cases
myGraph1 = {'A': [('B',4), ('C',2)],
            'B': [('A',4), ('D',3)],
            'C': [('A',2), ('D',5)],
            'D': [('B',3),('C',5)]
}

myGraph2 = {'A': [('B',4), ('C',2)],
            'B': [('A',4), ('C',1), ('D',3)],
            'C': [('A',2), ('B',1), ('D',5)],
            'D': [('B',3),('C',5)]
}

myGraph3 = {'A': [('B',4), ('C',3), ('D',1)],
            'B': [('A',4), ('F',1)],
            'C': [('A',3), ('D',5)],
            'D': [('E',2),('C',5)],
            'E': [('D',2),('F',1)],
            'F': [('B',1),('E',1)],
}

myGraph4 = {}
myGraph5 = {'A': [],
            'B': [],
            'C': [],
            'D': []
}

print("---- Test Cases for question 3 ----")
print(question3(myGraph1))
# {'A': [['C', 2], ['B', 4]], 'C': [['A', 2]], 'B': [['A', 4], ['D', 3]], 'D': [['B', 3]]}

print(question3(myGraph2))
# {'A': [['C', 2]], 'C': [['A', 2], ['B', 1]], 'B': [['C', 1], ['D', 3]], 'D': [['B', 3]]}

print(question3(myGraph3))
# {'A': [['D', 1], ['C', 3]], 'C': [['A', 3]], 'B': [['F', 1]], 'E': [['D', 2], ['F', 1]], 'D': [['A', 1], ['E', 2]], 'F': [['E', 1], ['B', 1]]}

print(question3(myGraph4))
# {}

print(question3(myGraph5))
# {'A': [], 'C': [], 'B': [], 'D': []}

# ------------------------------------ Question 4 -------------------------------------------
# 
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

# ------------------------------------ Question 5 -------------------------------------------
# 
# Find the element in a singly linked list that's m elements from the end.
# For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element.
# The function definition should look like question5(ll, m),
# where ll is the first node of a linked list and m is the "mth number from the end".
# You should copy/paste the Node class below to use as a representation of a node in the linked list.
# Return the value of the node at that position.

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def get_position(self, position):
        current = self.head
        count = 1
        if self.head:
            while count < position:
                count += 1
                current = current.next
        else:
            current = None
        return current

def question5(ll, m):
    count = 1
    current = ll
    current_lead = ll
    # This loop will find the desired position
    if ll:
        # leading node starts first
        while current_lead.next and count < m:
            count += 1
            current_lead = current_lead.next
        # Now move both
        while current_lead.next:
            current = current.next
            current_lead = current_lead.next
        if m <= (count) and m >= 0:
            return current.data
        else:
            return None
    else:
        return None

# define a few nodes
n1 = Node(13)
n2 = Node(21)
n3 = Node(35)
n4 = Node(49)

# Create linked list
ll = LinkedList(n1)
ll.append(n2)
ll.append(n3)
ll.append(n4)

print("---- Test Cases for Question 5 ----")
# Test Case 1
print (question5(ll.get_position(0), 2))
# 35

# define a few more nodes
n1 = Node(311)
n2 = Node(21)
n3 = Node(3)
n4 = Node(49)
n5 = Node(9)
n6 = Node(36)
n7 = Node(4)

# Create linked list
ll1 = LinkedList(n1)
ll1.append(n2)
ll1.append(n3)
ll1.append(n4)
ll1.append(n5)
ll1.append(n6)
ll1.append(n7)

# Test Cases Continued
print (question5(ll1.get_position(0), 6))
# 21
print (question5(ll1.get_position(0), 7))
# 311
print (question5(ll1.get_position(0), 8))
# None
print (question5(ll1.get_position(0), 9))
# None
print (question5(ll1.get_position(0), 3))
# 9
print (question5(ll1.get_position(0), 0))
# 4
print (question5(ll1.get_position(0), -1))
# None
print (question5("",3))
# None

