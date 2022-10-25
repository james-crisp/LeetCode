#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 21:58:14 2022

@author: jamescrisp
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        carry = 0
        final = ''
        
        aa = list(a)
        bb = list(b)
        
        while a or b or carry:
            if aa:
                carry += int(aa.pop())
            print(b)
            if bb:
                carry += int(bb.pop())
            
            final += str(carry %2)
            carry = carry//2
            
        
        return final