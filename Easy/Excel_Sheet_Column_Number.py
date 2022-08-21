#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 19:23:11 2022

@author: jamescrisp
"""

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        
        multiplier = 1
        total = 0
        
        for i in range(len(columnTitle)):
            total += (columnTitle[-i-1]*multiplier*26*(columnTitle.index(columnTitle[-i-1])+1))
            
        return total