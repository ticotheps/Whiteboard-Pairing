def search_sorted_matrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1  #  => 5

    while row < len(matrix) and col >= 0:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return (row, col)

    return (-1, -1)

# Tests
matrix = [ 
    [1, 4, 7, 12, 15, 999], 
    [2, 5, 19, 32, 35, 1001], 
    [4, 8, 24, 34, 36, 1002], 
    [40, 41, 42, 44, 45, 1003], 
    [98, 99, 101, 104, 190, 1009], 
]

print(search_sorted_matrix(matrix, 1))    #  should print (0, 0)
#  1st pass: matrix[0][5] = 999 > 1; so col -= 1 => 4, loop thru same row again
#  2nd pass: matrix[0][4] = 15 > 1; so col -= 1 => 3, loop thru same row again
#  3rd pass: matrix[0][3] = 12 > 1; so col -= 1 => 2, loop thru same row again
#  4th pass: matrix[0][2] = 7 > 1; so col -= 1 => 1, loop thru same row again
#  5th pass: matrix[0][1] = 4 > 1; so col -= 1 => 0, loop thru same row again
#  6th pass: matrix[0][0] = 1; so return (row, col) => return (0, 0)

print(search_sorted_matrix(matrix, 7))    # should print (0, 2)
#  1st pass: matrix[0][5] = 999 > 7; so col -= 1 => 4, loop thru same row again
#  2nd pass: matrix[0][4] = 15 > 7; so col -= 1 => 3, loop thru same row again
#  3rd pass: matrix[0][3] = 12 > 7; so col -= 1 => 2, loop thru same row again
#  4th pass: matrix[0][2] = 7; so return (row, col) => return (0, 2)

print(search_sorted_matrix(matrix, 999))  # should print (0, 5)
#  1st pass: matrix[0][5] = 999; so return (row, col) => return (0, 5)

print(search_sorted_matrix(matrix, 1001)) # should print (1, 5)
#  1st pass: matrix[0][5] = 999 < 1001; so row += 1 => 1, loop thru the next row
#  2nd pass: matrix[1][5] = 1001; so return (row, col) => return (1, 5)

print(search_sorted_matrix(matrix, 104))  # should print (4, 3)
#  1st pass: matrix[0][5] = 999 > 104; so col -= 1 => 4, loop thru same row again
#  2nd pass: matrix[1][4] = 35 < 104; so row += 1 => 1, loop thru the next row
#  3rd pass: matrix[2][4] = 36 < 104; so row += 1 => 2, loop thru the next row
#  4th pass: matrix[3][4] = 45 < 104; so row += 1 => 3, loop thru the next row
#  5th pass: matrix[4][4] = 190 > 104; so col -= 1 => 3, loop thru same row again
#  6th pass: matrix[4][3] = 104; so return (row, col) => return (4, 3)

print(search_sorted_matrix(matrix, 1010)) # should print (-1, -1)

