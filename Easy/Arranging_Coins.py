#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 19:59:25 2022

@author: jamescrisp
"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0:
            return 0
        
        row = 1
        number = 1
        total = 1
        while n >= total:
            row += 1
            number = number + 1
            total = total + number
        
        return row-1