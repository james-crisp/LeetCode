#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 19:23:50 2022

@author: jamescrisp
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        
        rowIt = [1]
        rowNew = [1,1]
        
        if rowIndex == 0:
            return rowIt
        
        if rowIndex == 1:
            return rowNew
        
        rowIt = rowNew.copy()
        
        for i in range(1,rowIndex):
            
            rowNew.append(1)
            for j in range(1,i+1):
                rowNew[j] = rowIt[j-1] + rowIt[j]
                
            rowIt = rowNew.copy()
            
        return rowIt