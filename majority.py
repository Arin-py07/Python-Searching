Input:
N = 3 
A[] = {1,2,3} 
Output:
-1
Explanation:
Since, each element in 
{1,2,3} appears only once so there 
is no majority element.


class Solution:
    def majorityElement(self, A, N):
        d={}
        for i in A:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        ma=max(d,key=d.get)
        
        if d[ma]>(N//2):
            return ma
        else:
            return -1
