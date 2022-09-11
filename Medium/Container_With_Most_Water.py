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
        
        area = 0

        left = 0
        right = 1
        middle = right-left
        
        def findArea (l,r,m):
            
            if height[l] <= height[r]:
                return height[l]*height[l]*m
            else:
                return height[l]*height[l]*m
        
        area = findArea(left,right,middle)
        print(area)
            
        for i in range(2,len(height)):
            
            if height[i] > height[left] or height[i] > height[right]:
                templeft = right
                tempright = i
                tempmiddle = tempright - templeft
            
            temp_area = findArea(templeft,tempright,tempmiddle)
            print(temp_area)
            
            if temp_area > area:
                area = temp_area
                left = templeft
                right = tempright
                middle = tempmiddle
        
        return area
            