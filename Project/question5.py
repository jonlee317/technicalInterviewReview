# Question 5
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
    # This loop will find the desired position
    if ll:
        while current.next:
            count += 1
            current = current.next
    # Checking that the number m chosen is within the bounds of the linked list
    if m < (count+1) and m >= 0:
        desired_position = count+1-m
    else:
        desired_position = None

    # This loop will find and return the value at the desired position
    current = ll
    count = 1
    if ll and desired_position != None:
        while current.next and count < desired_position:
            count += 1
            current = current.next
        return current.data
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
print (question5(ll1.get_position(0), ""))
# None
