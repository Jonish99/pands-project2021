'''A program that will investigate the Iris dataset. GMIT - GA_KDATG_L08 Y4. Programming and Scripting Project 2021'''

#Author: Jon Ishaque G00398244



######################################
#IMPORTS
import pandas as pd  #alias pd
from csv import reader
######################################




def readCSV():
    with open('iris.data.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            print(row[0],row[1],row[2],row[3],row[4])


def readintodf():
    
    # Read data from file 'filename.csv' 
    # (in the same directory that your python process is based)
    # Control delimiters, rows, column names with read_csv (see later) 
    irisDF = pd.read_csv("iris.data.csv",  header = None, names =["sepal length","sepal width","petal length","petal width","species"] )
    # Preview the first 5 lines of the loaded data 
    print(irisDF.head())


def main():
    readintodf()



if __name__=="__main__":
    main()
