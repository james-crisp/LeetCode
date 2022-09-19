#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 20:02:29 2022

@author: jamescrisp
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        finalnumber = -1
        
        if target == nums[0]:
            return 0
            
        def binarys(mins,maxs,targets):
            nonlocal finalnumber
            
            if abs(mins-maxs) <= 1:
                return
            
            mids = int((mins+maxs)/2)
            
            if nums[mids] == targets:
                finalnumber = mids
                return
            elif targets > nums[mids]:
                mins = mids
                binarys(mins,maxs,targets)
            elif targets < nums[mids]:
                maxs = mids
                binarys(mins,maxs,targets)
            
            return
        
        binarys(0,len(nums),target)
        
        return finalnumber