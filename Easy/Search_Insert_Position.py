#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 16:42:08 2022

@author: jamescrisp
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        #Binary search
        lowerbound = 0
        midpoint = 0
        upperbound = len(nums)
        
        if len(nums) % 2 == 0:
            midpoint = int(len(nums)/2)
            
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] > target:
                lowerbound = 0
            else:
                lowerbound = midpoint
        
        return
                
            
            