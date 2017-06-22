#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 13:52:30 2017

@author: Lee
"""

# find the longest substring in alphabetical order
s = 'azcbobobegghakl'
result = ''
i=0

while i < len(s):
    current = ''
    current = current +s[i]
    j=i
    while j+1<len(s) and s[j+1]>=s[j]:
        current = current + s[j+1]
        j = j+1 
    if len(current)>len(result):
        result=current 
    i=i+len(current)

  
        
print ('Longest substring in alphabetical order is: '+result)




def isIn(char,aStr):
    '''
    Recursive check if a char is in the string
    '''

    start = 0
    end = len(aStr)
    test = (start+end)//2

    if char == aStr[test]:
        return True
    if end==0 or start==len(aStr)-1 or start>end or len(aStr)==0:
        return False
    elif char<aStr[test]:
        end = test
        return isIn(char,aStr[start:end])
    elif char>aStr[test]:
        start = test
        return isIn(char,aStr[start:end])

