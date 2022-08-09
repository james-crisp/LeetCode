#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 11:09:12 2022

@author: jamescrisp
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        binary_n = bin(n)
        
        binary_n_string = str(binary_n)
        
        total = 0
        
        for char in binary_n_string:
            if char == "1": total += 1
               
        
        return total
    