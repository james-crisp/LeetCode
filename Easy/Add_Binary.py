#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 21:58:14 2022

@author: jamescrisp
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        carry = 0
        
        aa = list(a)
        bb = list(b)
        
        while a or b or carry:
            if a:
                aa += 1
            if b:
                bb += 1
            
            
        return final