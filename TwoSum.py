# -*- coding: utf-8 -*-
"""
Created on Sat May 29 16:58:08 2021

@author: learningmachine
"""

class Solution:
    def twoSum(self, nums, target):
        ans = [(i,j) for i,s1 in enumerate(nums) for j,s2 in enumerate(nums) if i != j and s1+s2 == target]
        return ans[0]
    
    def twoSum_(self, nums, target):
        #Create a hash table to map from value to index
        h = {num: index for index,num in enumerate(nums)}
        ans = [(i,h[target-num]) for i,num  in enumerate(nums) if target-num in h and i !=  h[target-num]]
        return ans[0]
    
    def twoSum__(self,nums,target):
        h = {}
        for i,num in enumerate(nums):
            n = target-num
            if n not in h:
                h[num] = i
            else:
                return[h[n],i]
    


s = Solution()
s.twoSum__([3,2,2,3],6)

 
