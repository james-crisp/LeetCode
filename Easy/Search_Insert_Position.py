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
        upperbound = len(nums) - 1
        
        if target > nums[upperbound]:
            return upperbound+1
        if target < nums[lowerbound]:
            return 0
        if target == nums[0]:
            return 0
        
        while lowerbound != upperbound:
            midpoint = int((upperbound+lowerbound)/2)
            if lowerbound == midpoint:
                return lowerbound+1
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] < target:
                lowerbound = midpoint
            else:
                upperbound = midpoint
        
        return lowerbound+1
                
            
            
                
            
            
            
            
                
            
            