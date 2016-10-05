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
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        count = 1
        if self.head:
            while count < position:
                count += 1
                current = current.next
        return current

def question5(ll, m):
    pass

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

print ll.get_position(0).data

# TODO:  figure out what is the rule of this question.  are we supposed to create
# our own linked list and add items to it and test it?

# Test case
#ll1
#print question5()
