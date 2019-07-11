#  Understanding the Problem
#  stack = data structure; FIFO

#  -Create a 'MaxStack' class
#  -Create a 'getMax()' method
    #  -Returns max value in the stack
    #  -Doesn't remove item from stack
    #  -Should be O(1)
    
#  Devising a Plan
#  -Utilize current 'Stack' class to control first stack
#  -Create a 'MaxStack' class to control a second stack that
#   only has items pushed into it if it is greater than the
#   current item in.
#  -Use 'peek' method to see what the value of the current
#   item is in the 'MaxStack'

#  Implementing the Plan

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return None

    def peek(self):
        if len(self.items) > 0:
            return self.items[len(self.items) - 1]
        else:
            return None
  
class MaxStack:
    def __init__(self):
        self.stack = Stack()
        self.max = Stack()
        
    def push(self, current_item):
        #  Check value of item in self.max
        #  If no item in self.max, add item to both stacks
        #  If there is an item in self.max, and current_item > item,
            #  then add item to both stacks
        #  If there is an item in self.max, and current_time < item,
            #  only add item to self.stack
        pass
    def pop(self):
        #  Check value of item in self.max
        #  If there are more than one item in self.max, remove all but last item
        #  Pop item from self.max
        #  Set equal to variable 
        #  Peek to see if variable = top item in self.max
        pass
        
    def getMax(self):
        #  Return top item in self.max
        pass



#  Reflecting/Iterating