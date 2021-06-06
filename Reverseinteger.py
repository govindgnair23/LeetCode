# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 09:38:26 2021

@author: learningmachine
"""

class Solution:
    def reverse(self, x: int) -> int:
        if x <= -2**31 or x >= (2**31 -1):
            return 0
        sign = 1 if x>0 else -1
        s = str(abs(x))
        ans = sign*int(s[::-1])
        if ans <= -2**31 or ans >= (2**31 -1):
            return 0
        
        return ans
    
    def reverse_(self,x):
        rev = 0
        sign = 1 if x>0 else -1
        x_ = sign*x
        while x_!= 0:
            pop = x_%10
            x_ = x_//10
            
            temp = rev *10 + pop
            rev =  temp
        
        return sign*rev
        


s = Solution()
s.reverse(1534236469)
s.reverse_(-123)
