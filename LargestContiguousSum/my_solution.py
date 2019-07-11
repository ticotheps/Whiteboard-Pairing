#  1) Create an empty array to hold list of sums
#  2) Create an empty array to hold values to add together to get a "sum"
#  3) Loop through each index until every index has been added to the tempArr, beginning with currentIndex
#  4) Use Max() to find largest sum from 'sumsArr'
#  5) Return largest sum from 'sumsArr'
#

#  arr = [3, 5, 7, -9, 5]
sumsArr = []

def contig_sum(arr):
    global sumsArr
    addNumsArr = []
    for i in range(len(arr)):
        addNumsArr.append(arr[i])
        if sum(addNumsArr) < 0:
            addNumsArr = [2, 3, -8]
        sumsArr.append(sum(addNumsArr))
            
    return max(sumsArr)
        
print(contig_sum([2, 3, -8, -1, 2, 4, -2, 3]))
print(sumsArr)