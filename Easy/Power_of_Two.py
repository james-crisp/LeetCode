#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 12:21:58 2022

@author: jamescrisp
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n <= 0:
            return False
        
        if n == 1:
            return True
        
        number = n
        
        while number > 1:
            number = number / 2
            if number == 1:
                return True
        
        return False