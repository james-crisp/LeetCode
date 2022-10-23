#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 21:13:27 2022

@author: jamescrisp
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        
        count = 1
        
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[count] = nums[i+1]
                count += 1
            
        return count
            
        
            
        
        
            
        