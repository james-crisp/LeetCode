#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 21:58:14 2022

@author: jamescrisp
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        carry = 0
        
        final = []
        
        while a and b:
            final = a + b
            if carry == 1:
                final[i+1] = 1
            
            
        return final