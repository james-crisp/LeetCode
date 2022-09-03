#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 16:16:06 2022

@author: jamescrisp
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        count = 0
        isItSpace = True
        
        for i in range(1,len(s)+1):
            
            if s[-i] == " ":
                if isItSpace == False:
                    return count
            else:
                isItSpace = False
                count += 1
                
        return count