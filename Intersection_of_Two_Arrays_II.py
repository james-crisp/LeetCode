#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 17:09:21 2022

@author: jamescrisp
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums3 = []
        
        if len(nums1) > len(nums2):
            for number in nums2:
                if number in nums1:
                    nums3.append(number)
        else:
            for number in nums1:
                if number in nums2:
                    nums3.append(number)
                    
        return nums3