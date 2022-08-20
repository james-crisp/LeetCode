#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 15:26:29 2022

@author: jamescrisp
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        if len(s) == 1:
            return 0
        
        for i in range(len(s)-1):
            if s[i] not in s[i+1:]:
                if s[i] not in s[:i]:
                    return i
        
        #Test last character
        if s[-1] not in s[:len(s)-1]:
            return len(s) - 1
        
        return -1
            