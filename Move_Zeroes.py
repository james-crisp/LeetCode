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
        counter = 0
        
        def flip(x):
            nonlocal counter
            print(x)
            if nums[x] == 0:
                counter += 1
                flip(x+1)
            else:
                for i in range(counter):
                    nums[x-(i+1)] = nums[x-i]
                    nums[x-i] = 0
                counter = 0
                
        #Exceeds range for end 0's        
        for x in range(len(nums)-1):
            print(nums)
            flip(x)
            
            
        
        return
        