#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 10:54:10 2022

@author: jamescrisp
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        IntSol = []
        IntSol.append(roman[s[0]])
        
        for x in range(1,len(s)):
            if (s[x] == 'M' or s[x] == 'D') and (s[x-1] == 'C'):
                IntSol.append(-200)
            elif (s[x] == 'L' or s[x] == 'C') and (s[x-1] == 'X'):
                IntSol.append(-20)
            elif (s[x] == 'X' or s[x] == 'V') and (s[x-1] == 'I'):
                IntSol.append(-2)
            IntSol.append(roman[s[x]])
        
        total = 0
        for x in IntSol:
            total = total + x
        
        return total
            
        