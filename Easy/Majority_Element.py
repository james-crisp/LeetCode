#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 20:22:59 2022

@author: jamescrisp
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        #not time optimal solution
        
        for number in nums:
            
            if nums.count(number) > (len(nums)/2):
                return number
            
        return False