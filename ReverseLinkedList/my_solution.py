# Understanding the Problem
    # list node = a single value in a linked list
    # Must reverse the list
    # Cannot use any extra 
# Devising a Plan
    # make list node aware of previous node vs only next node
# Implementing the Plan
# Reflect/Iterate

class ListNode:
  def __init__ (self, value):
    self.value = value
    self.next = None

# a -> b -> c -> d -> e

def reverseLinkedList(node):
    # Set the value of 'node' equal to a variable
    # Traverse to node.next
    # Set the value of 'node.next' to another variable
    # Continue ^ this process until 'node.next' = none, which means I'm at the tail
        # Set the value of the tail to another variable
    # Set the 'next' value of the tail to previous node's value
    # Traverse backwards, setting each node's 'next' value to the previous node value until you reach head
    
    # Swap before traversing forward
    
    # current node
    # previous node
    # next node
    pass




a = ListNode('a')
b = ListNode('b')
c = ListNode('c')
d = ListNode('d')
e = ListNode('e')

a.next = b
b.next = c
c.next = d
d.next = e

def printList(node):
  current = node
  
  while current:
    print(current.value)
    current = current.next
  


print(reverseLinkedList(a));  # should print 'e'
printList(e);   # should print 'e', 'd', 'c', 'b', 'a'