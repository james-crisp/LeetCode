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
        
        if len(nums) == 0: return [-1,-1]
        
        def bnsleft(nums1,target1):
            low, high = 0, len(nums) - 1
            mid,prev=0,0
            while prev!=mid:
                prev = mid
                mid = (low+high) // 2
                if nums1[mid] > target1:
                    high = mid
                else:
                    low = mid
            return low - 1
            
            
        def bnsright(nums1,target1):
            low, high = 0, len(nums) - 1
            mid,prev=0,0
            while prev!=mid:
                prev = mid
                mid = (low+high) // 2
                if nums1[mid] > target1:
                    high = mid
                else:
                    low = mid
            return high - 1
        left = bnsleft(nums,target)
        right = bnsright(nums,target)
        if left == -1:right = -1
        return [left,right]
                
                
                
                
                
                
                