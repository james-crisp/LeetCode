#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 20:46:24 2022

@author: jamescrisp
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        
        a = b = 1
        
        for i in range(n):
            temp = b
            b = a+b
            a = temp
        
        return a