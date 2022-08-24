#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 17:09:30 2022

@author: jamescrisp
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = []
        
        if len(strs) == 1:
            return strs[0]
        
        if "" in strs:
            return ""
        
        if strs[0] > strs[1]:
            for i in range(len(strs[1])):
                if strs[1][i] == strs[0][i]:
                    prefix.append(strs[1][i])
                else:
                    break
        else:
            for i in range(len(strs[0])):
                if strs[0][i] == strs[1][i]:
                    prefix.append(strs[1][i])
                else:
                    break
        
        for i in range(2,len(strs)):
            if len(prefix) < len(strs[i]):
                for j in range(len(prefix)):
                    if strs[i][j] != prefix[j]:
                        prefix = prefix[0:j]
                        print(prefix)
                        break
            else:
                prefix = prefix[0:len(strs[i])]
                for j in range(len(strs[i])):
                    if strs[i][j] != prefix[j]:
                        prefix = prefix[0:j]
                        print(prefix)
                        break
        
        prefix = "".join(prefix)
        
        return prefix