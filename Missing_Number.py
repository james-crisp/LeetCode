#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 19:59:16 2022

@author: jamescrisp
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        
        rangen = list(range(len(nums)+1))
        
        for number in rangen:
            if number not in nums:
                return number
        
        return len(nums)+1