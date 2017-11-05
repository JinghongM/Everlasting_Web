# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd



def sizeNormalizer(testFileName,collectorFileName):
    def getUnit(input): # get the unit whatever it has or not
        unit = ''
        for character in input:
            if character.isalpha():
                unit=unit+character
        return unit
    
    def convertUnit(sizeInput,df2,manuelUnit=''):
        if manuelUnit != '':
            return sizeInput + manuelUnit
        originUnit = getUnit(sizeInput)
        for column in df2.columns:
            for element in df2[column]:
                if originUnit == str(element):  
                    return column, sizeInput.replace(originUnit,column)
            
        return originUnit,sizeInput
    def getBrand(rawBrand):
        Brand = ''
        if '(' in rawBrand:
            Brand = rawBrand[:rawBrand.index('(')]
            return Brand
        else:
            return rawBrand
    brandUnit={}
    df = pd.read_csv(testFileName,encoding = 'utf-8')
    unitExcel = pd.read_excel(collectorFileName)
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
                unit, newSize = convertUnit(str(Size),unitExcel)
                df.set_value(row,'Sizes for all',newSize)
                if Brand not in brandUnit:
                    brandUnit[Brand] = []
                    brandUnit[Brand].append(unit)
                else:
                    if getUnit(newSize) in brandUnit[Brand]:
                        continue
                    else:
                        brandUnit[Brand].append(getUnit(newSize))
            else: #if the size has not unit, see if the brand has unit or not
                if Brand in brandUnit:
                    newSize = convertUnit(Size,unitExcel,brandUnit[Brand][-1])
                    df.set_value(row,'Sizes for all',newSize)
                
    df.to_csv('test.csv',index=False)

