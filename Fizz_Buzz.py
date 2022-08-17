#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 15:27:50 2022

@author: jamescrisp
"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        string_output = []
        
        for i in range(1,n+1):
            if i % 3 == 0:
                if i % 5 == 0:
                    string_output.append("FizzBuzz")
                else:
                    string_output.append("Fizz")
            elif i % 5 == 0:
                string_output.append("Buzz")
            else:
                string_output.append(f'{i}')
                    
            
        return string_output