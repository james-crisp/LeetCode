#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 21:13:27 2022

@author: jamescrisp
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        #modify the array 
        for i in range(len(nums)):
            if i == len(nums)-1:
                return 1
            if nums[i] != nums[i+1]:
                break
        
        count = 1
        
        for i in range(len(nums)-1):
            k = 1
            count += 1
            while nums[i] == nums[i+k]:
                if k+i == len(nums) - 1:
                    break
                nums[i+k] = nums[i] + 1
                k += 1
                
            if k+i == len(nums) - 1:
                break
            nums[i+1] = nums[i] + 1
        '''
        count = 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return count
            count += 1
        '''
        return count
            
        
            
        