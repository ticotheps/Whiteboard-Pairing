# Understanding the Problem

# Create a TempTracker class
#   -max (highest)
#   -min (lowest)
#   -mean (average of all temps seen)
#   -mode (the middle element in a list of ordered temps)

# Priorities
#   -GET methods > INSERT methods
#   -Goal: get GET methods to O(1) runtime

# Constraints
#   -getMean() => output = float (integer with decimals)
#   -all other methods => output = integers
#   -units => Farenheit
#   -if more than 1 mode => output = any mode

# Devising a Plan

#   -Hash table as data structure 
#       -runtime complexity for insert/get/delete = O(1)

# Implementing the Plan

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.elements = [None] * self.capacity

class TempTracker:
    def __init__(self, temp):
        self.temp = temp
        
    def hash(self, string, max):
        hash = 5381
        for x in string:
            hash = (hash * 33) + ord(x)
        return hash % max
        
    # records a new temperature
    def insert(self, hash_table, key, temp):
        hash_key = hash(key, hash_table.capacity) 
        
        key_value = [key, temp]
      
    # returns the highest temperature we've seen so far 
    def getMax():
        pass
    
    # returns the lowest temperature we've seen so far
    def getMin():
        pass
      
    # returns the mean of all temperatures we've seen so far
    def getMean():
        pass
      
    # return a mode of all temperatures we've seen so far
    def getMode():
        pass
    
# Reflect/Iterate