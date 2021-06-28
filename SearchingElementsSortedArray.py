#Test case 1:

Input:
N = 5, K = 6
arr[] = {1,2,3,4,6}
Output: 1
Exlpanation: Since, 6 is present in 
the array at index 4 (0-based indexing),
output is 1.

#Test Case2:

Input:
N = 5, K = 2
arr[] = {1,3,4,5,6}
Output: -1
Exlpanation: Since, 2 is not present 
in the array, output is -1.

#Solution:

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == K:
                return 1
                
            elif arr[mid] < K:
                low = mid + 1
                

            else:
                high = mid - 1
                

        return -1
