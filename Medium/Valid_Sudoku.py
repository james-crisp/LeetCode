#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 20:06:20 2022

@author: jamescrisp
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #1,2,3,4,5,6,7,8,9
        array = [0,0,0,0,0,0,0,0,0] 
        
        def checkRows(sudo):
            for i in range(len(sudo)):
                temparray = array.copy()
                
                for j in sudo[i]:
                    
                    if j.isdigit():
                        
                        temparray[int(j)-1] += 1
                        if temparray[int(j)-1] > 1:
                            return False
            return True
        
        if checkRows(board) == False:
            return False
        
        def checkColumns(sudo):
            for i in range(len(sudo)):
                temparray = array.copy()
                
                for j in range(len(sudo)):
                    
                    if sudo[j][i].isdigit():
                        
                        temparray[int(sudo[j][i])-1] += 1
                        if temparray[int(sudo[j][i])-1] > 1:
                            return False
            return True
        
        
        if checkColumns(board) == False:
            return False
        
        return True