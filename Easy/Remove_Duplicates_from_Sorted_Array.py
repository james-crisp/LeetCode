#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 21:13:27 2022

@author: jamescrisp
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        #modify the array 
        
        
        for i in range(len(nums)-2):
            k = 1
            while nums[i] == nums[i+k]:
                if k+i == len(nums) - 1:
                    break
                nums[i+k] = nums[i] + 1
                k += 1
                
            
            nums[i+1] = nums[i] + 1
        
        count = 0
        for i in range(len(nums)):
            if
        
        return
            
        