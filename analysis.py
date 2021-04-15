'''A program that will investigate the Iris dataset. GMIT - GA_KDATG_L08 Y4. Programming and Scripting Project 2021'''

#Author: Jon Ishaque G00398244



######################################
#IMPORTS
import pandas as pd  #alias pd
from csv import reader
import matplotlib.pyplot as plt
import os #for os path
from matplotlib.colors import ListedColormap #scatter plot colors
#try using seaborn
import seaborn as sns
sns.set(style="white", color_codes=True)
######################################

#attribute names, a list used through out the exploratin of the 
col_names  =['Sepal Length(cm)','Sepal Width(cm)','Petal Length(cm)','Petal Width(cm)','species']

def cleanLabel(label):
    label = label.replace('_',' ')
    label=label.title()
    return label
def readCSV():
    #(Lynn, 2021)
    with open('iris_data.csv', 'r') as reader_object:
        csv_reader = reader(reader_object)
        for row in csv_reader:
            #print at most granular level. 
            print(row[0],row[1],row[2],row[3],row[4])

def createVarHist(iris_df):
    

    for col_name in col_names:
        if col_name !="species": # make a histogram
            plt.figure(figsize = (10, 7))
            #get x plot
            x = iris_df[col_name]
            
            plt.hist(x, bins = 20, color = "green")
            plt.title(cleanLabel(col_name))
            plt.xlabel(cleanLabel(col_name) )
            plt.ylabel("Count")
            plt.savefig(col_name +".png")

def createVarSummary(dfTmp,varName):
    
    
   #Iris_Sum_decimals = pd.Series([2,3,2,3,3,3,2], index=['mean', 'std','min','25%','50%','75%','max']) #(pandas.DataFrame.round — pandas 1.2.3 documentation, 2021)
    dfTmp.round({'mean ':2, 'std ':2,'min ':2,'25% ':2,'50% ':2,'75% ':2,'max ':2}) #Not working
   
    #dfTmp.to_csv("Attributes Grouped" + ".csv", sep=',',  mode='a', encoding='utf-8')

    
    with open('Iris_Variable_Summaries.txt', 'a') as f:
        
       
        f.write("This is content of iris dataset grouped by variable and summarised."+'\n'+'\n')
        dfTmp.to_string(f)
        f.write ('\n'+'\n')
        f.close()

        


def group_by_attribute(iris_df):

    attributes_grouped = iris_df.groupby("species").describe()
    #If Iris_Variable_Summaries.txt already exists, delete to avoid
    #the same text is not constantly repeated
    if os.path.exists(''):
        os.remove("Iris_Variable_Summaries.txt")

    #print (bl_IVS)
    with open('Iris_Variable_Summaries.txt', 'a') as f:
        #write file header
        
        f.write("This is content of iris dataset grouped by variable and summarised."+'\n'+'\n')
        #use attribute names to loop through groups. 
        for col_name in col_names:            
            if col_name !="species": #do not create summary output for species - it is not a group. Enhancements required
                #write variable header, using col name and cleaning using clean label function
                f.write (cleanLabel(col_name)+'\n'+'\n')               
                #new df based on group
                dfTmp = attributes_grouped[col_name]
                #Iris_Sum_decimals = pd.Series([2,3,2,3,3,3,2], index=['mean', 'std','min','25%','50%','75%','max']) #(pandas.DataFrame.round — pandas 1.2.3 documentation, 2021)
                dfTmp.round({'mean ':2, 'std ':2,'min ':2,'25% ':2,'50% ':2,'75% ':2,'max ':2}) #Not working                         
                dfTmp.to_string(f)
                f.write ('\n'+'\n')
    f.close()



def group_by_species(iris_df):
    #group by species
    species_grouped = iris_df.groupby('species')
    for key, item in species_grouped:
        print (key)
        #print(species_grouped.get_group(key), "\n\n")
 


def  createScatterPlots(iris_df):
    #["sepal_length","sepal_width","petal_length","petal_ width",
    #species = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    #cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
    # create a scatter plot of SEPAL WIDTH versus SEPAL LENGTH and color by SPECIES
    #plt.scatter(iris_df['sepal_length'], iris_df['sepal_width'], c = ['red'],cmap=cmap_bold)
    #plt.title("Sepal Width vs. Sepal Length")
    #plt.xlabel(cleanLabel('sepal_length') + ' CM')
    #plt.ylabel(cleanLabel('sepal_width')  + ' CM')
    #plt.show()'''
    #'''now create for 1 pair for 3 species on one plot for each pair combi'''

    #try seaborne
    
    sns.FacetGrid(iris_df, hue='species', height=5) \
        .map(plt.scatter, 'Sepal Length(cm)', 'Sepal Width(cm)') \
        .add_legend() 
    plt.title('Sepal Length vs. Sepal Width')

    sns.FacetGrid(iris_df, hue='species', height=5) \
        .map(plt.scatter, 'Sepal Length(cm)', 'Petal Width(cm)') \
        .add_legend() 
    plt.title('Sepal Length vs. Petal Width')
   # sns.jointplot('Sepal Length(cm)', 'Petal Width(cm)'), data=iris_df,kind="kde", space=0, color="g")
    
    #iris = sns.load_dataset("iris_df")
    sns.pairplot(iris_df)
    
    plt.show()


    g = sns.FacetGrid(iris_df, row='Sepal Length(cm)', col='Petal Width(cm)')
    #g.map(sns.scatter, "age")
    plt.show()
def main():
    #create a menu function to make call variousl anayis methods
    #read csv into a df
    iris_df = pd.read_csv("iris_data.csv",  header = None, names =col_names)
    #readCSV()
    #print(iris_df)

    #Create Histo grams based on four variables 
    #createVarHist(iris_df)
    
    #write the groupe attributed to a single txt file
    group_by_attribute(iris_df)
    
    #group_by_species(iris_df)
    #cerate scatter plots for pairs of variables
    createScatterPlots(iris_df)


if __name__=="__main__":
    main()
