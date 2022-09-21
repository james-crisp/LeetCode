#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 20:19:11 2022

@author: jamescrisp
"""

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for row in image:
            for number in range(int(len(row)/2)):
                
                temp = row[number]
                
                row[number] = row[-number-1]
                row[-number-1] = temp
        
        for row in image:
            for number in range(len(row)):
                if row[number] == 0:
                    row[number] = 1
                else:
                    row[number] = 0
        
        return image