Input:
n = 4
arr[] = {1,2,3,4}
x = 3
Output: 2
Explanation: There is one test case 
with array as {1, 2, 3 4} and element 
to be searched as 3.  Since 3 is 
present at index 2, output is 2.

#solution

import math
class Solution:
    #Complete the below function
    def search(self,arr, N, X):
        for a in arr:
            if a==X:
               return arr.index(a)
        else:
            return -1
