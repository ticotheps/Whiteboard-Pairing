# Understanding the Problem

# -We have robot.
# -Goal: robot to move from 'S' => 'E' in
#  an n x n grid.

# -Expected Input: n (length of a side of the grid)
# -Expected Output: an integer (represents total # of possible paths from 
#  'S' to 'E').

# -Constraints:
#     -Can only move up, down, left, or right.
#     -Can't visit the same square twice.

# Devising a Plan
# -BFS => shortest path
# -DFS => think of a maze, gets from start to end

# Implementing the Plan

# Create a stack (LIFO) to store list of scheduled paths to try
# Create a variable called 'possible_paths'
# Append the starting square to a path; add path to the stack

# Create a graph that stores paths you've already attempted

# Create a DFS function that takes in: graph, starting square, end square
    # Pop off the first path in the stack
    # Set the last item in that path equal to a variable
    # Check to see if path is empty
    #    If it's not, check to see if it's equal to the end square
    #         If it is, add the whole path to a 'possible_paths'
    # 
# Reflecting/Iterating