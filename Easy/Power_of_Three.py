#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 19:47:40 2022

@author: jamescrisp
"""

class Solution:
    import math
    def isPowerOfThree(self, n: int) -> bool:
        
        if n <= 0:
            return False
        logba = float(math.log(n)/math.log(3))
        print(logba)
        if logba.is_integer():
            return True
        else:
            return False
        