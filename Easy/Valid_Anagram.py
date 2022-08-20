#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 20:19:11 2022

@author: jamescrisp
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        for char in s:
            if s.count(char) != t.count(char):
                return False
        
        return True