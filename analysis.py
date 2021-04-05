'''A program that will investigate the Iris dataset. GMIT - GA_KDATG_L08 Y4. Programming and Scripting Project 2021'''

#Author: Jon Ishaque G00398244



######################################
#IMPORTS
import pandas as pd  #alias pd
from csv import reader
import matplotlib.pyplot as plt
######################################

#attribute names, a list used through out the exploratin of the 
col_names  =["sepal_length","sepal_width","petal_length","petal_ width","species"]


def readCSV():
    #(Lynn, 2021)
    with open('iris.data.csv', 'r') as reader_object:
        csv_reader = reader(reader_object)
        for row in csv_reader:
            #print at most granular level. 
            print(row[0],row[1],row[2],row[3],row[4])

def createVarHist():
    x=1



def createVarSummary(dfTmp,varName):
    
    
    Iris_Sum_decs = pd.Series([2,3,2,3,3,3,2], index=['mean', 'std','min','25%','50%','75%','max']) #(pandas.DataFrame.round — pandas 1.2.3 documentation, 2021)
    dfTmp.round(Iris_Sum_decs)
    print(dfTmp)
    #write to file
    dfTmp.to_csv(varName + ".csv", sep=',', encoding='utf-8')


def readintodf():
    #(pandas.DataFrame — pandas 1.2.3 documentation, 2021)
    # Read data from file 'iris.data.csv' 
    # read into dataframe
    irisDF = pd.read_csv("iris.data.csv",  header = None, names =col_names)
    # Preview the first 5 lines of the loaded data 
    #print(irisDF.head())



    attributes_grouped = irisDF.groupby("species").describe()
    #print(attributes_grouped)
    #use attribute names to loop through groups. 
    for col_name in col_names:
        
        if col_name !="species": #do not create summary output for species - it is not a group. Enhancements required
            print(col_name)
            #print (attributes_grouped[col_name])
            #new df based on group
            dfTmp = attributes_grouped[col_name]
            createVarSummary(dfTmp,col_name)


    for col_name in col_names:
        if col_name !="species": # make a histograme


def test():
    x=x

def main():
    readintodf()



if __name__=="__main__":
    main()
