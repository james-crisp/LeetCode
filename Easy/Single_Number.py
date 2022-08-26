#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 14:04:02 2022

@author: jamescrisp
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        for number in nums:
            if nums.count(number) == 1:
                return number
        
        return
            
                
        
        
        
        
        
        