#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 13:55:04 2022

@author: jamescrisp
"""

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        
        for i in range(0,len(matrix)-1):
            for j in range(1,len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
    
        return matrix