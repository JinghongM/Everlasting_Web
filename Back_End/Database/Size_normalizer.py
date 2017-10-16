# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd


class sizeNormalizer:
    def __init__(self,testFileName,collectorFileName):
        self.testFileName = testFileName
        self.collectorFileName = collectorFileName
    def getUnit(self,input): # get the unit whatever it has or not
        unit = ''
        for character in input:
            if character.isalpha():
                unit=unit+character
        return unit
    
    def convertUnit(self,sizeInput,df2,manuelUnit=''):
        if manuelUnit != '':
            return sizeInput + manuelUnit
        originUnit = self.getUnit(sizeInput)
        for column in df2.columns:
            for element in df2[column]:
                if originUnit == str(element):  
                    return column, sizeInput.replace(originUnit,column)
            
        return originUnit,sizeInput
    def getBrand(self,rawBrand):
        Brand = ''
        if '(' in rawBrand:
            Brand = rawBrand[:rawBrand.index('(')]
            return Brand
        else:
            return rawBrand

    def main(self):
        brandUnit={}
        df = pd.read_csv(self.testfile,encoding = 'utf-8')
        unitExcel = pd.read_excel(self.collectorfile)
        for row in range(1,df.shape[0]):
            Size = str(df.iloc[row,1])
            Brand = str(df.iloc[row,0])
            Brand = self.getBrand(Brand)
            Unit = self.getUnit(Size)
            if Size == 'nan': #if the size has nothing, throw it away.
                continue
            else:
                if Unit != '': # if the size has its own unit, convert it to a normal unit and save the new unit in the brandUnit
                        #and rewrite it in the df
                        unit, newSize = self.convertUnit(str(Size),unitExcel)
                        df.set_value(row,'Sizes for all',newSize)
                        if Brand not in brandUnit:
                            brandUnit[Brand] = []
                            brandUnit[Brand].append(unit)
                        else:
                             if self.getUnit(newSize) in brandUnit[Brand]:
                                 continue
                             else:
                                 brandUnit[Brand].append(self.getUnit(newSize))
                else: #if the size has not unit, see if the brand has unit or not
                    if Brand in brandUnit:
                        newSize = self.convertUnit(Size,unitExcel,brandUnit[Brand][-1])
                        df.set_value(row,'Sizes for all',newSize)
                
        df.to_csv('test.csv',index=False)


        
