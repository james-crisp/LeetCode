#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 18:46:44 2022

@author: jamescrisp
"""

class Solution:
    def isValid(self, s: str) -> bool:
        
        length = len(s)
        
        for x in range(0,length-1):
            
            if s[x] == '(':
                if s[x+1] != ')':
                    return False
            
            elif s[x] == '[':
                if s[x+1] != ']':
                    return False
            
            elif s[x] == '{':
                if s[x+1] != '}':
                    return False
            
        
        return True