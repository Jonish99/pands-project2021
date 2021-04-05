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

def createVarHist(iris_df):
    

    for col_name in col_names:
        if col_name !="species": # make a histogram
            plt.figure(figsize = (10, 7))
            x = iris_df[col_name]
            
            plt.hist(x, bins = 20, color = "green")
            plt.title(col_name)
            plt.xlabel(col_name + " cm")
            plt.ylabel("Count")
            plt.savefig(col_name +".png")

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
    iris_df = pd.read_csv("iris.data.csv",  header = None, names =col_names)
    # Preview the first 5 lines of the loaded data 
    #print(iris_df.head())

    return(iris_df)


def group_by_species(iris_df):
    attributes_grouped = iris_df.groupby("species").describe()
    #print(attributes_grouped)
    #use attribute names to loop through groups. 
    for col_name in col_names:
        
        if col_name !="species": #do not create summary output for species - it is not a group. Enhancements required
            print(col_name)
            #print (attributes_grouped[col_name])
            #new df based on group
            dfTmp = attributes_grouped[col_name]
            createVarSummary(dfTmp,col_name)


    


def test():
    x=x

def main():
    #read csv into a df
    iris_df = readintodf()

    #print(iris_df)

    #group df
    group_by_species(iris_df)

    
    #create histogram for each variable
    createVarHist(iris_df)



if __name__=="__main__":
    main()
