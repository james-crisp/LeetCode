#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 10:57:11 2022

@author: jamescrisp
"""

#Solution successful

class Solution:
    def reverse(self, x: int) -> int:
        
        stringx = str(x)
        negative = False
        
        if stringx[0] == '-':
            negative = True
            stringx = stringx[1:]
        
        reversedStr = ''.join(x for x in reversed(stringx))
        
        if negative == True:
            if -int(reversedStr) < -(2**31):
                return 0
            else:
                return -int(reversedStr)
        
        if int(reversedStr) > (2**31 - 1):
            return 0
        
        return int(reversedStr)