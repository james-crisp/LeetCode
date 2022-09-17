#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 10:32:34 2022

@author: jamescrisp
"""

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n == 1:
            return True
        power = 1
        while power < n:
            power *= 4
            if power == n:
                return True
        
        return False