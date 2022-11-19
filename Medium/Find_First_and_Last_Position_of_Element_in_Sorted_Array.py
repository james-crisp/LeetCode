#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 21:11:38 2022

@author: jamescrisp
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        #binary search
        
        low = 0
        mid = 0
        high = len(nums) - 1
        answer = []
        
        if len(nums) == 0:
            return [-1,-1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            
        while nums[mid] != target:
            temp = mid
            mid = (high+low) // 2
            if temp == mid:
                break
            if nums[mid] > target:
                high = mid
            else:
                low = mid
            
        if nums[mid] != target:
            return [-1,-1]
        
        answer.append(mid)
        while nums[mid] == target:
            mid += 1
        answer.append(mid-1)
        
        return answer
                
                
                
                