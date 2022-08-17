#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 11:04:29 2022

@author: jamescrisp
"""

class Solution:
    def isValid(self, s: str) -> bool:
        
        paranths = []
        brackets = []
        bracks = []
        
        for char in s:
            if char == '(':
                paranths.append(1)
            elif char == ')':
                paranths.append(2)
            elif char == '[':
                brackets.append(1)
            elif char == ']':
                brackets.append(2)
            elif char == '{':
                bracks.append(1)
            else:
                bracks.append(2)
        
        def checker(numbers):
            if numbers[0] == 2 or numbers[-1] == 1:
                return False
            
            
            
        return