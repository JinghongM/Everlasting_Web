# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
def getUnit(input): # get the unit whatever it has or not
    unit = ''
    for character in input:
        if character.isalpha():
            unit=unit+character
    return unit
    
    
def convertUnit(input, unit=''): #conert the unit of the size; and can still add unit
    if not(any(char.isdigit() for char in input)):
        return input
    if 'MM' in input:
        return input.replace('MM','mm')
    if 'M' in input:
        return input.replace('M','mo')
    if 'm' in input and 'mo' not in input and 'cm' not in input:
        return input.replace('m','mo')
    if 'y' in input and 'year' not in input:
        return input.replace('y','yr')
    if 'Y' in input:
        return input.replace('Y','yr')
    if 'X' in input and 'L' not in input:
        return input.replace('X','yr and half')

    return input + unit

def getBrand(rawBrand):
    Brand = ''
    if '(' in rawBrand:
        Brand = rawBrand[:rawBrand.index('(')]
        return Brand
    else:
        return rawBrand
    
brandUnit={}
df = pd.read_csv('Test.csv',encoding = 'utf-8')
for row in range(1,df.shape[0]):
    Size = str(df.iloc[row,1])
    Brand = str(df.iloc[row,0])
    Brand = getBrand(Brand)
    Unit = getUnit(Size)
    if Size == 'nan': #if the size has nothing, throw it away.
        continue
    else:
        if Unit != '': # if the size has its own unit, convert it to a normal unit and save the new unit in the brandUnit
                        #and rewrite it in the df
             newSize = convertUnit(str(Size))
             df.set_value(row,'Sizes for all',newSize)
             if Brand not in brandUnit:
                 brandUnit[Brand] = []
                 brandUnit[Brand].append(getUnit(newSize))
             else:
                 if getUnit(newSize) in brandUnit[Brand]:
                     continue
                 else:
                     brandUnit[Brand].append(getUnit(newSize))
        else: #if the size has not unit, see if the brand has unit or not
            if Brand in brandUnit:
                newSize = convertUnit(Size,brandUnit[Brand][-1])
                df.set_value(row,'Sizes for all',newSize)
                
df.to_csv('test.csv',index=False)

