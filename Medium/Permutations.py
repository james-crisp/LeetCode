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
            
        def repeat(nums1):
            set_nums = []
            for i in range(len(nums)):
                set_nums.append(nums[i])
            set_of_numbers.append(set_nums)
            return
        
        for j in range(2**len(nums)-2):
            repeat(nums[-j])
        
        return set_of_numbers