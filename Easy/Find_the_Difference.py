#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 18:36:48 2022

@author: jamescrisp
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        for char in t:
            
            count_t = t.count(char)
            
            if char in s:
                count_s = s.count(char)
                if count_s != count_t:
                    return char
            else:
                return char
            
                
        
        return "No char"
                