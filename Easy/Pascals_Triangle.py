#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 19:38:33 2022

@author: jamescrisp
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        oglist = []
        
        for i in range(1,numRows+1):
            templist = []
            for j in range(i):
                templist.append(1)
            oglist.append(templist)
        
        return oglist