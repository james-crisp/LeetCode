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
        
        for i in nums2:
            for j in nums1:
                if i <= j:
                    temp = j
                    nums1[nums1.find(j)] = i 
            
        return
        