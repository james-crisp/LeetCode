#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 20:28:10 2022

@author: jamescrisp
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        sets = [[]]
        
        for number in nums:
            temp = []
            temp.append(number)
            sets.append(temp)
            
        for i in range(len(nums)):
            for j in range(i):
                sets.append(i)
        
        return