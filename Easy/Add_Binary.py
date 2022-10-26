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
        
        while aa or bb or carry:
            if aa:
                carry += int(aa.pop())
            #print(aa,bb,carry)
            if bb:
                carry += int(bb.pop())
            
            final += str(carry %2)
            carry //= 2
            
        
        return final[::-1]