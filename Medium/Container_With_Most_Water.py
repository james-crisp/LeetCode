#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 20:59:27 2022

@author: jamescrisp
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        #Maxmimum area calculation
        
        #How to calculate without iterating through each and ever volume?
        
        i = 0
        j = len(height)-1
        water = 0
        
        while i != j:
            water = max(water,(j-i)*min(height[i],height[j]))
            
            if height[i] <= height[j]:
                i+=1
            else:
                j-=1
        
        return water
            
            