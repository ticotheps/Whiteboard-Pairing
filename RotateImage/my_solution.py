# Understanding the Problem

# image = N x N
# pixel = integer, 0-9

# Objective: Rotate the image, counter-clockwise

# Expected Input: An array of arrays
# Expected Output: A modified array of arrays

# Number of Rows = length of ONE array (inside larger array)
# Number of Cols = Number of total arrays (insdie larger array)

# Devising a Plan

def rotateImage(matrix):
    # Create an empty array to make a modified copy of the original.
    copied_matrix = []
    # Loop through and create a copy of the given matrix, but with all
    #     all values set to "None".
    for _ in range(len(matrix)):
        template_array = []
        for _ in range(len(matrix)):
            template_array.append(None)
        copied_matrix.append(template_array)
        
    # print(template_array)
    # print(copied_matrix)
    
    # Loop through each item within the given matrix...
    for x in range(0, len(matrix), 1):
        # print(x)
        # ...Create a variable to keep track of which index of matrix you're on
        matrix_item_index = 0
    #   ...Loop through each index of each ITEM (from given matrix) 
    #        beginning from the LAST item...
        for y in range(len(matrix)-1, -1, -1):
            # print(y)
            copied_matrix[matrix_item_index][x] = matrix[x][y]
            matrix_item_index += 1
            
    return copied_matrix


# Implementing the Plan
# Reflect/Reiterate

print(rotateImage([
  [1, 1, 5, 9, 9],
  [2, 2, 6, 0, 0],
  [3, 3, 7, 1, 1],
  [4, 4, 8, 2, 2],
  [5, 5, 9, 3, 3]
]))