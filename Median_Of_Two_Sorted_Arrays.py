#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 11:02:45 2022

@author: jamescrisp
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        import numpy as np
        
        nums3 = np.concatenate((nums1,nums2))
        median = np.median(nums3)
        
        return median