#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 14:07:00 2022

@author: jamescrisp
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        
        #Start from the end
        
        while m > 0 and n > 0:
            if nums2[m-1] >= nums1[n-1]:
                nums1[m+n-1] = nums2[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums1[n-1]
                n -= 1
                
        if n > 0:
            nums1[:n] = nums2[:n]
        
        return nums1
        
        