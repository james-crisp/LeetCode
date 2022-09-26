#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 18:22:36 2022

@author: jamescrisp
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        length_word = len(s)
        
        final_word = [s[0]]
        
        #First Row
        
        x = numRows*2 - 2
        
        while x < length_word:
            final_word.append(s[x])
            x = x*2
        
        #Second Row
        
        x = 1
        
        while x < length_word:
            final_word.append(s[x])
            x = x*3
            
        return
        
            
        