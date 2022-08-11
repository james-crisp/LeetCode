#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 10:52:13 2022

@author: jamescrisp
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        tempList = []
        
        for number in nums:
            if number in tempList:
                return True
            else:
                tempList.append(number)
                
        
        return False