#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 16:42:59 2022

@author: jamescrisp
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        if len(s)%2 == 0:
            for i in range(int(len(s)/2)):
                temp = s[i]
                s[i] = s[-i-1]
                s[-i-1] = temp
        else:
            for i in range(int((len(s)-1)/2)):
                temp = s[i]
                s[i] = s[-i-1]
                s[-i-1] = temp
        
        return