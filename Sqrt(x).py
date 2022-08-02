#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 12:37:51 2022

@author: jamescrisp
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        
        # Find aproximate square-root
        
        prev = 0
        nex = 0
        over = False
        
        while over == False:
            nex = prev + 1
            if nex*nex > x:
                return prev
            prev = nex
        
        return False
                
        
        