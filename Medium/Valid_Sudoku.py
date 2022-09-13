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
        
        def checkBoxes(sudo):
            #First 3 boxes
            for x in range(3):
                temparray = array.copy()
                for i in range(3):
                    for j in range(3):
                        
                        if sudo[i][j+x*3].isdigit():
                        
                            temparray[int(sudo[i][j+x*3])-1] += 1
                            if temparray[int(sudo[i][j+x*3])-1] > 1:
                                return False
            #Second 3 boxes
            for x in range(3):
                temparray = array.copy()
                for i in range(3,6):
                    for j in range(3):
                        
                        if sudo[i][j+x*3].isdigit():
                        
                            temparray[int(sudo[i][j+x*3])-1] += 1
                            if temparray[int(sudo[i][j+x*3])-1] > 1:
                                return False
            #Third 3 boxes
            for x in range(3):
                temparray = array.copy()
                for i in range(6,9):
                    for j in range(3):
                        
                        if sudo[i][j+x*3].isdigit():
                        
                            temparray[int(sudo[i][j+x*3])-1] += 1
                            if temparray[int(sudo[i][j+x*3])-1] > 1:
                                return False
                    
        
        if checkBoxes(board) == False:
            return False
        
        return True