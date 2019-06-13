#  Understanding the Problem
#  suffix = the substring of characters FROM the currently inspected character to the END of the string
#  hash table will have unique keys with child properties, in a nested structure to represent suffices

#  PROBLEM:
#     - write a class
#     - be able create a new instance of the class using any value passed into the constructor
#     - also be able to search through trie for a designated string

#  Devising a Plan
#     - use a two for loops, one nested to iterate through given input string to create a hash table
#     - use nested loop to traverse through suffix of current key 
#     - iterate through until no characters left

#     - SEARCH
#     - not concerned with index
#     - use for loop to search root element of trie for the first character in the given string
#     - if a key matches the currently inspected character of the given string, enter into key
#         - repeat process until reach *
#         - if no child property of * found, return False
#     - if no key matches the inspected characater of the given string, return False

#  IMPLEMENT:

class SuffixTrie:
    def __init__(self, string):
        self.string = string
        self.n = "*"
        self.root = dict()
        
    def createTrie(self, string):
        for i in range(len(string)):
            node = self.root
            for j in range(len(string[i:])):
                if j not in node:
                    node[string[j]] = dict()
                node = node[string[j]]
                 