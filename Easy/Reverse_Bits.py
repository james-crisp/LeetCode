#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 11:08:14 2022

@author: jamescrisp
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        
        newbinary = []
        
        getbinary = lambda x, n: format(x, 'b').zfill(n)
        binary_n = getbinary(n,32)
        string_n = str(binary_n)
        
        for i in range(len(string_n)):
            newbinary.append(string_n[-1-i])
        
        newnumber = "".join(x for x in newbinary)
        newint = int(newnumber, 2)
        
        return newint