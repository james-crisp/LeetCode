#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 09:05:58 2022

@author: jamescrisp
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        #Solution slow, uses push/pull stack
        
        #False palindrome if negative number.
        if x < 0:
            return False
        
        #variables
        stack = []
        stringx = str(x)
        length = len(stringx)
        
        if (length%2) == 0: #even length number
            #Put numbers into stack
            for i in range(int(length/2)):
                stack.append(stringx[i])
            
            #Check numbers in stack
            for i in range(int(length/2) , length):
                if stringx[i] != stack.pop():
                    return False
                
            return True
            
        else: #odd length number
            #Put numbers in stack
            for i in range(int((length-1)/2)):
                stack.append(stringx[i])
            
            #Check stack
            for i in range(int((length+1)/2) , length):
                if stringx[i] != stack.pop():
                    return False
            
            return True
             