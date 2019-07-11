#  Understanding the Problem
#  suffix = the substring of characters FROM the currently inspected character to the END of the string
#  hash table will have unique keys with child properties, in a nested structure to represent suffices

#  PROBLEM:
#     - write a class
#     - be able create a new instance of the class using any value passed into the constructor
#     - also be able to search through trie for a designated string

#  Devising a Plan
#     - use two for loops, one nested to iterate through given input string to create a hash table
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
        self.createTrie(string)
        
    def createTrie(self, string):  # n = length of starting string to create dict(); O(n^2)
        for i in range(len(string)):
            node = self.root
            for j in string[i:]:
                if j not in node:
                    node[j] = dict()
                node = node[j]
            node[self.n] = True
            
    def contains(self, string):  # n = length of string; O(n)
        node = self.root
        for letter in string:
            if letter in node:
                node = node[letter]  #  similar to node.next
            else:
                return False
        else:  # <== specific to Python language (sort of like a closure)
            if self.n in node:
                return True
            else:
                return False
         
myTrie = SuffixTrie("pogo")
print(myTrie.root)         
print(myTrie.contains("ogo"))           