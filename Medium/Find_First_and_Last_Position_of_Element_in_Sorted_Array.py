#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 21:11:38 2022

@author: jamescrisp
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        #binary search
        #separate left and right?
        
        def bnsleft(nums1,target1):
            low = 0
            high = len(nums) - 1
            mid = 0
            
            while nums1 != target1:
                prev = mid
                mid = (low+high) // 2
                
                if prev == mid:
                    mid = -1
                    break
                if nums1[mid] > target1:
                    high = mid
                else:
                    low = mid
            return mid
            
            
        def bnsright(nums1,target1):
            prev = mid
                mid = (low+high) // 2
                
                if prev == mid:
                    mid = -1
                    break
                if nums1[mid] > target1:
                    high = mid
                else:
                    low = mid
            return mid
        
        return 
                
                
                
                
                
                
                