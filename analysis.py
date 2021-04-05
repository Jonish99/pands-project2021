'''A program that will investigate the Iris dataset. GMIT - GA_KDATG_L08 Y4. Programming and Scripting Project 2021'''

#Author: Jon Ishaque G00398244



######################################
#IMPORTS
import pandas as pd  #alias pd
from csv import reader
######################################


attribute_names  =["sepal length","sepal width","petal length","petal width","species"]

def readCSV():
    #(Lynn, 2021)
    with open('iris.data.csv', 'r') as reader_object:
        csv_reader = reader(reader_object)

    
        for row in csv_reader:
            #print at most granular level. 
            print(row[0],row[1],row[2],row[3],row[4])



def write_To_File():
    x =1

def readintodf():
    #(pandas.DataFrame — pandas 1.2.3 documentation, 2021)
    # Read data from file 'iris.data.csv' 
 
    # read into dataframe
    irisDF = pd.read_csv("iris.data.csv",  header = None, names =attribute_names)
    # Preview the first 5 lines of the loaded data 
    #print(irisDF.head())

    
    
  



    attributes_grouped = irisDF.groupby("species").describe()

   
    #use attribute names to loop through groups. 
    for att_name in attribute_names:
        
        
        if att_name !="species": #do not create summary output for species - it is not a group. Enhancements required
            print(att_name)
            print (attributes_grouped[att_name])
            #new df based on group
            dfTmp = attributes_grouped[att_name]
            #write to file
            dfTmp.to_csv(att_name, sep='\t', encoding='utf-8')

    #for group_name, df_group in attributes_grouped:
        #print (group_name)
        #attributes_grouped("petal length")
        

        


        
      
    

  


def test():
    x=x

def main():
    readintodf()



if __name__=="__main__":
    main()
