#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 17:06:37 2022

@author: jamescrisp
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        def flip(x):
            
            if nums[x] == 0:
                flip(x+1)
            else:
                nums[x-1] = nums[x]
                nums[x] = 0
                
        for x in range(len(nums)-1):
            
            flip(x)
            print(nums)
            
        
        return
        