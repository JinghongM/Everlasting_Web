# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 13:09:31 2017

@author: Jinghong Miao
"""
import csv
import pandas as pd
import os.path
class ImgException(Exception):
    def __init__(self, msg='No msg'):
        self.msg = msg
def classifier(Clothing_Genome_Project):
    if(os.path.isfile(Clothing_Genome_Project) == False):
        raise ImgException(Clothing_Genome_Project + ' not found')
        
    def findIDs(SearchWords,Dictionaries):
        if len(SearchWords) == 0:
            return -1,-1
        for StyleID,subDictionary in Dictionaries.items():
            for subKey,subValue in subDictionary.items():
                if any(word in subKey for word in SearchWords):
                    return StyleID,subValue
        return -1,-1
    StyleColumn = 3
    GenusColumn = 4 #main table column
    SpeciesColumn=5 #main table column
    AgeColumn = 9 #main table column
    CGP = pd.read_csv(Clothing_Genome_Project)
    StyleErrorBucket = []
    GenusErrorBucket = []
    SpeciesErrorBucket = []
    ageErrorBucket = []
    for row in range(1,CGP.shape[0]):
        size = str(CGP.iat[row,AgeColumn]) 
        if 'mo' in size:
            size = size[:-2]
            if "-" in size:
                ageFrom = int(size[:size.find("-")])
                ageTo = int(size[size.find("-") + 1:])
                if ageFrom<6 or ageTo<6:
                    age_error={}
                    age_error['row']=row+2
                    age_error['Item #']=CGP.iat[row,0]
                    age_error['size']=size
                    ageErrorBucket.append(age_error)
                    
            else:
                if int(size)<6:
                    age_error={}
                    age_error['row']=row+2
                    age_error['Item #']=CGP.iat[row,0]
                    age_error['size']=size
                    ageErrorBucket.append(age_error)
                    

        genus = str(CGP.iat[row,GenusColumn])
        if not genus.isdigit() and genus != "nan":
            genus_error={}
            genus_error['row']=row+2
            genus_error['Item #']=CGP.iat[row,0]
            genus_error['genus']=genus
            GenusErrorBucket.append(genus_error)
            
        species = str(CGP.iat[row, SpeciesColumn])
        if not species.isdigit() and species != "nan":
            # species_error={}
            # species_error['row']=row+2
            # species_error['Item #']=CGP.iat[row,0]
            # species_error['species']=species
            # SpeciesErrorBucket.append(species_error)
            if species in SpeciesErrorBucket:
                continue
            else:
                SpeciesErrorBucket.append(species)





    if len(ageErrorBucket) != 0:
        keys = ageErrorBucket[0].keys()
        with open('age error.csv', 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(ageErrorBucket)
    else:
        print("No age errors")


    if len(GenusErrorBucket) != 0:
        keys = GenusErrorBucket[0].keys() 
        with open('genus error.csv', 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(GenusErrorBucket)
    else:
        print("No genus error")


    if len(SpeciesErrorBucket) != 0:

        with open("species error.csv",'a') as resultFile:
            wr = csv.writer(resultFile, dialect='excel')
            for element in SpeciesErrorBucket:
                print([element])
                wr.writerow([element])
    else:
        print("No species error")
classifier("test.csv")