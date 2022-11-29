#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 20:27:53 2022

@author: jamescrisp
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #print(len(matrix))
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = matrix[j][i]
        
        return matrix