#without built-in func

Input:
x = 5
Output: 2
Explanation: Since, 5 is not a perfect 
square, floor of square_root of 5 is 2.

Input:
x = 4
Output: 2
Explanation: Since, 4 is a perfect 
square, so its square root is 2.

Solution:

import math as mp
#Complete this function
class Solution:
    def floorSqrt(self, x):
        
        return mp.floor(x**0.5)
