'''A program that will investigate the Iris dataset. GMIT - GA_KDATG_L08 Y4. Programming and Scripting Project 2021'''

#Author: Jon Ishaque G00398244



######################################
#IMPORTS
import pandas as pd  #alias pd
from csv import reader
######################################




def readCSV():
    #(Lynn, 2021)
    with open('iris.data.csv', 'r') as reader_object:
        csv_reader = reader(reader_object)

    
        for row in csv_reader:
            #print at most granular level. 
            print(row[0],row[1],row[2],row[3],row[4])


def readintodf():
    #(pandas.DataFrame — pandas 1.2.3 documentation, 2021)
    # Read data from file 'iris.data.csv' 
 
    # read into dataframe
    irisDF = pd.read_csv("iris.data.csv",  header = None, names =["sepal length","sepal width","petal length","petal width","species"] )
    # Preview the first 5 lines of the loaded data 
    #print(irisDF.head())

    attributes_grouped = irisDF.groupby("species").describe()

    print(attributes_grouped["sepal length"])
    print(attributes_grouped["sepal width"])
    print(attributes_grouped["petal length"])
    print(attributes_grouped["petal width"])

    df1_grouped = irisDF.groupby("species").describe()
        
      
    

    # print species summary
    #print (irisDF[irisDF["species"] == "Iris-versicolor"].describe())



def test():
    x=x

def main():
    readintodf()



if __name__=="__main__":
    main()
