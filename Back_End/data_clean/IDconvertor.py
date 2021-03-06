# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:35:27 2017

@author: Jinghong Miao
"""
import pandas as pd
import copy
import os.path

class ImgException(Exception):
    def __init__(self, msg='No msg'):
        self.msg = msg
def IDconvertor(Clothing_Genome_Project,Item_ID_Info):
    if(os.path.isfile(Clothing_Genome_Project) == False):
        raise ImgException(Clothing_Genome_Project + ' not found')
    if(os.path.isfile(Item_ID_Info) == False):
        raise ImgException(Item_ID_Info + ' not found')
    def findIDs(SearchWords,Genus_Species):   
        for word in SearchKeyWords:        
            for GenusID,species in Genus_Species.items():
                if word in species:
                    return GenusID,species[word]
                
        return -1,-1
    Quantity=9
    EWNumber = 0
    GenusColumn=3
    SpeciesColumn=4
    StyleGenreIDStartColumn = 6
    StyleGenreIDENDColumn = 9
    GenreColumnStart = 12
    GenreColumnEnd = 18
    IInfo = pd.read_excel(Item_ID_Info)
    CGP = pd.read_excel(Clothing_Genome_Project)
    Genus_Species={} # this is a dictionary which key is Stype Genre Genus ID, value is the Special ID
    Genres = {}
    for column in range(StyleGenreIDStartColumn,StyleGenreIDENDColumn+1):
        GenusBlock = IInfo.iat[0,column]
        GenusName = GenusBlock[:GenusBlock.find("=")]
        GenusID = int(GenusBlock[GenusBlock.find("=")+1:])
        Genus_Species[GenusID] = {}
        Genus_Species[GenusID][GenusName] = GenusID 
    
    for column in range(0,len(Genus_Species)):
        for row in range(1,IInfo.shape[0]):
            if str(IInfo.iat[row,StyleGenreIDStartColumn+column]) =='nan':
                break
            else:
                Block = IInfo.iat[row,StyleGenreIDStartColumn+column]
                SpeciesName = Block[:Block.find("=")]
                SpeciesID=Block[Block.find("=")+1:]
                Genus_Species[column][SpeciesName] =SpeciesID

    for row in range(1,CGP.shape[0]):
        Species = CGP.iat[row,SpeciesColumn]
        Genus = CGP.iat[row,GenusColumn]
        SearchKeyWords=[]
        if str(Species)=="nan" and str(Genus) == "nan":
            print("No Genus or Species at " + str(row))
            continue
        else:
            SearchKeyWords.append(str(Genus))
            GenusWords=Genus.split(" ")
            for word in GenusWords:
                SearchKeyWords.append(str(word))
            if str(Species) !='nan':
                SearchKeyWords.append(str(Species))
            GenusID, SpeciesID = findIDs(SearchKeyWords,Genus_Species)
        if GenusID == -1 and SpeciesID == -1:
            continue
        CGP.iat[row,GenusColumn] = GenusID
        CGP.iat[row,SpeciesColumn] = SpeciesID
    for row in range(1,CGP.shape[0]):
        originRow=copy.deepcopy(CGP.loc[row])
        quantity = str(originRow.iat[Quantity]) 
        CGP.iat[row,EWNumber] = str(originRow.iat[EWNumber]) + '-1'
        
        if quantity !='nan' and quantity != '1':
            for i in range(2,int(quantity)+1):
                newrow = copy.deepcopy(originRow)
                newrow.iat[EWNumber] = str(originRow.iat[EWNumber]) + '-'+ str(i)
                CGP=CGP.append(newrow) 
    #process genre
    for genre in IInfo['Genre']:
        if str(genre) == 'nan':
            break
        else:
            Genres[genre[:genre.find('=')]] = genre[genre.find('=')+1:]
    GenreTitle = []
    for i in range(GenreColumnStart,GenreColumnEnd):
        GenreTitle.append(CGP.iat[0,i])
    for element in range(len(GenreTitle)):
        for char in GenreTitle[element].split('/'):
            if char in Genres:
                GenreTitle[element] = Genres[char]

    for row in range(1,CGP.shape[0]):
        genres = []
        for column in range(len(GenreTitle)):
            if CGP.iat[row,column+GenreColumnStart] == 'x':
                genres.append(GenreTitle[column])

        if len(genres) == 0:
            CGP.iat[row,GenreColumnStart] = 0
        elif len(genres) == 1:
            CGP.iat[row,GenreColumnStart] = genres[0]
        else:
            CGP.iat[row,GenreColumnStart] = genres[0]
            originRow=copy.deepcopy(CGP.iloc[row])
            for genreId in genres[1:]:
                newrow = copy.deepcopy(originRow)
                newrow.iat[GenreColumnStart] = genreId
                CGP = CGP.append(newrow)
    CGP = CGP.drop(CGP.columns[GenreColumnStart+1:GenreColumnEnd],axis = 1)
    CGP = CGP.drop(CGP.columns[Quantity],axis = 1)
    
    i=0 #process headers
    while i<len(CGP.columns.values):
        if "Unnamed" in CGP.columns.values[i]:
            CGP.columns.values[i] = ''
        i+=1
    CGP.to_csv('test.csv',index=False)          
