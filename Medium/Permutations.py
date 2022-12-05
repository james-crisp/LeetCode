#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 20:32:45 2022

@author: jamescrisp
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        #recurison
        set_of_numbers = []
        #2^n-2
        count1 = 0
        print(set_of_numbers)
        if len(nums) == 0:
            return []
        
        if len(nums) == 1:
            return [nums]
        
        for i in range(len(nums)):
            m = nums[i]
            remLst = nums[:i] + nums[i+1:]
            
            for p in self.permute(nums):
                set_of_numbers([m] + p)
            
        
        return set_of_numbers