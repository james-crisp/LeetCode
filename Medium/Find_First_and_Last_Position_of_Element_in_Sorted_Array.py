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
        high = len(nums) - 1
        mid = high+low // 2
        answer = []
        prev = 0
        
        while mid != prev:
            prev = mid
            mid = high+low // 2
            print(mid)
            if nums[mid] > target:
                low = mid
            elif nums[mid] < target:
                high = mid
            else:
                break
        
        answer.append(mid)
        answer.append(0)
        
        return answer
                
                