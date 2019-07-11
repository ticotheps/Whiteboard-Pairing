# Largest Contiguous Sum

# Given an array of positive and negative integers, write a function to
# find the contiguous sequence (in other words, a non-empty subarray of
# adjacent elements) with the largest sum. Return the sum.

# Sample input: [2, 3, -8, -1, 2, 4, -2, 3] </br>
# Expected output: 7, from summing up the sequence 2, 4, -2, 3

# Sample input: [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4] </br>
# Expected output: 19, from summing up the sequence 1, 3, -2, 3, 4, 7, 2,
# -9, 6, 3, 1

# Analyze the time and space complexity of your solution.

#  input: array
#  output: sum

#  1) Create an empty array to hold list of sums
#  2) Create an empty array to hold values to add together to get a "sum"
#  3) Loop through each index until every index has been added to the tempArr, beginning with currentIndex
#  4) Use Max() to find largest sum from 'sumsArr'
#  5) Return largest sum from 'sumsArr'
#

#  arr = [3, 5, 7, -9, 5]

sumsArr = []

def contig_sum(arr):

    for i in range(len(arr)-1):
        addNumsArr = []
        addNumsArr.append(arr[i])
        sumsArr.append(sum(addNumsArr))
    return max(sumsArr)
        
print(contig_sum([3, 5, 7, -9, 5]))
    
    
    

