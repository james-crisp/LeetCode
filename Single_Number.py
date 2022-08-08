#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 10:51:40 2022

@author: jamescrisp
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        onenum = nums[0]
        
        listnums = []
        
        for i in range(len(nums)):
            if nums[i] == onenum:
                onenum = nums[i+1]
            else