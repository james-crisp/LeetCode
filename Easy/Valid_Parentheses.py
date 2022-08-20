#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 11:04:29 2022

@author: jamescrisp
"""

class Solution:
    def isValid(self, s: str) -> bool:
        
        para = 0
        brack = 0
        curve = 0
        
        for char in s:
            if char == '(':
                para += 1
            elif char == ')':
                para -= 1
            elif char == '[':
                brack += 1
            elif char == ']':
                brack -= 1
            elif char == '{':
                curve += 1
            else:
                curve -= 1
        
        if para != 0 or brack != 0 or curve != 0:
            return False
        else:
            return True
            

            