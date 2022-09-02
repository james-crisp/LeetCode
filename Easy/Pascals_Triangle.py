#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 19:38:33 2022

@author: jamescrisp
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        oglist = []
        
        #Initialize space for number of rows and amount of numbers in each row.
        
        for i in range(0,numRows):
            templist = [1]
            for j in range(i):
                templist.append(1)
            oglist.append(templist)
        
        #Change each row's number to the previous rows numbers to the right and left of it.
        
        for i in range(2,numRows):
            for j in range(1,i):
                oglist[i][j] = oglist[i-1][j-1] + oglist[i-1][j]
        
        return oglist