#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 20:12:06 2022

@author: jamescrisp
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        count = 0
        
        for i in range(len(nums)):
            if nums[i] == val:
                count += 1
                j = i + 1
                
                while j != len(nums):
                    if nums[j] != val:
                        nums[i] = nums[j]
                        nums[j] = val
                        j = len(nums)
                    else:
                        j += 1
                    
        print(count)
            
        return count
                    
                    
                    