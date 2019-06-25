# Understanding the Problem
# 1) Expected Input: array of names
# 2) Expected Output: single name with most votes

# Devise a Plan
# 1) Create a set() to hold unique names and votes per name
# 2) Use a FOR loop to iterate through the array.
# 3) Check to see if the name is in the votes set():
#     a) If it is not, add it and set value to 1.
#     b) If it is, increment value by 1.
# 3) Traverse through set() to find max value of all keys.
#     a) If there is a tie between multiple keys of the set
# 
# 4) Return key of max value.

# Implement the Plan
def winner(array):
    votes = dict()
    
    for i in range(0, len(array)):
        # Checks to see if value is already in set()
        if array[i] not in votes:
            # Adds the value into the set()
            votes[array[i]] = 0
        votes[array[i]] += 1
    
    return votes
  
print(winner(['veronica', 'mary', 'alex', 'james', 'mary', 'michael', 'alex', 'michael']))

# Reflect/Iterate Solution
