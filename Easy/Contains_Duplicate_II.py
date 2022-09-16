#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 19:39:54 2022

@author: jamescrisp
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        for i in range(len(nums)):
            num_in_num = nums.count(nums[i])
            if num_in_num > 1:
                for x in range(num_in_num - 1):
                    if 
                