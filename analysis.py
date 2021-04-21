'''A program that will investigate the Iris dataset. GMIT - GA_KDATG_L08 Y4. Programming and Scripting Project 2021'''

#Author: Jon Ishaque G00398244



#====================================IMPORTS==================================
#IMPORTS
import pandas as pd  #alias pd
from csv import reader
import matplotlib.pyplot as plt #alias plt
import os #for os path
#from matplotlib.colors import ListedColormap #scatter plot colors
import seaborn as sns
#=================================================================================

#attribute names, a list used through out the exploratin of the. These column title 
#are available as an externally imported list but, like the Iris dataset itself are 
#manually added to this functionality.
col_names  =('Sepal Length(cm)','Sepal Width(cm)','Petal Length(cm)','Petal Width(cm)','species')

#===================================== FUNCTIONS =================================

def cleanLabel(label):
    label = label.replace('_',' ')
    label=label.title()
    return label

#=================================================================================

def readCSV():
    #Read the whole csv file into the  a pandas dataframe, irisdf - used through this program
    irisdf= pd.read_csv("iris_data.csv",  header = None, names =col_names) 
    #returnt to main function
    return irisdf

#=================================================================================

#Create variable summaries, menu choices 1 & 2
def create_var_summary(iris_df,f_action):
    #use the groupby method to group the dataframe by the columnspecies, 
    #this will group the other four columns(variables) based on unique cells in species 
    #(ie 3 species rows in 4 column groups).
    #The describe method creates statistical analyis for each variable.
    attributes_grouped = iris_df.groupby("species").describe()
    print(attributes_grouped)
    if f_action=='view':
        #print each group stacked vertically
        for col_name in col_names:
            if col_name !="species": #do not create summary output for species - it is not a group.  
                print(cleanLabel(col_name))
                print(attributes_grouped[col_name], "\n\n")
        #use input any key to pause the while loop, whilst use assimilates output.
        x = input("Press any key to return to menu: ")
    elif f_action=='save':
        #open a new copy/overwrite(w) existing verision of txt file to save summaries to.
        with open('Iris_Variable_Summaries.txt', 'w') as f:
            #write file header
            f.write("This file contains statistical summaries of each variable in the iris dataset ."+'\n'+'\n')
            #use attribute names to loop through groups. 
            #i.e. for each variable in the list do...
            for col_name in col_names:            
                if col_name !="species": #do not create summary output for species - it is not a group. 
                    #write variable summary headerheader, using col name and cleaning using clean label function
                    f.write (cleanLabel(col_name)+'\n'+'\n')               
                    #new df based on group
                    dfTmp = attributes_grouped[col_name]
                    #Iris_Sum_decimals = pd.Series([2,3,2,3,3,3,2], index=['mean', 'std','min','25%','50%','75%','max']) #(pandas.DataFrame.round — pandas 1.2.3 documentation, 2021)
                    dfTmp.round({'mean ':2, 'std ':2,'min ':2,'25% ':2,'50% ':2,'75% ':2,'max ':2}) #Not working                         
                    dfTmp.to_string(f)
                    f.write ('\n'+'\n')    
        f.close()

#=================================================================================

#Create variable histograms, menu choices 3 & 4
def create_var_hist(iris_df,f_action):
    
    for col_name in col_names:
        if col_name !="species": # make a histogram
            plt.figure(figsize = (10, 7))
            #get x plot
            x = iris_df[col_name]
            plt.hist(x, bins = 20, color = "green")
            plt.title(cleanLabel(col_name))
            plt.xlabel(cleanLabel(col_name) )
            plt.ylabel("Count")
            if f_action =='view':
                plt.show()
            elif f_action=='save':
                #save and clean '(cm)' off file name
                plt.savefig(col_name.replace('(cm)','') +".png")
     

#=================================================================================

#Create scatter plots for variable pair combination, menu choices, 5 & 6
def  create_scatter_plots(iris_df,f_action):
    #Using the seaborn library to great scatter plots for each pair of variables
    #load iris df, use hue to create different colors for each species/class
    #1. 'Sepal Length(cm)', 'Sepal Width(cm)'
    sns.FacetGrid(iris_df, hue='species', height=5) \
        .map(plt.scatter, 'Sepal Length(cm)', 'Sepal Width(cm)') \
        .add_legend() 
    #set title
    plt.title('1. Sepal Length vs. Sepal Width')
    if f_action =='view':
        plt.show()
    elif f_action =='save':
        plt.savefig('1. Sepal Length vs. Sepal Width' +'.png')
    #############
    sns.FacetGrid(iris_df, hue='species', height=5) \
        .map(plt.scatter, 'Sepal Length(cm)', 'Petal Width(cm)') \
        .add_legend() 
    plt.title('2. Sepal Length vs. Petal Width')
    if f_action =='view':
        plt.show()
    elif f_action =='save':
        plt.savefig('2. Sepal Length vs. Petal Width' +'.png')

#=================================================================================

#Create overall graphical summary, menu choices 7 & 8
def grahical_summary(iris_df,f_action):
    #The six possible pair comparions are best shown together, to determine which (if any)
    #are better identifiers of species.
    #Markers and hue enable different identification of each species
    #the corner parameter enable the plot to show just one half of the diagonal. 
    #The benefit of this is that whilst seeing the plots together is very useful, 
    #repeating the same plots with the axes inverted is too much information. 
    #the diagonal in this example produce historgrams, for each of the four variables, 
    # with the 3 species overlain ach other.

    #set the style parameter and colors for this use of seaborn
    sns.set(style="white", color_codes=True)

    g=sns.pairplot(iris_df, hue="species",markers=["o", "s", "D"], corner=True,diag_kind="hist")
    #use suptitle to add title to whole graphci 
    g.fig.suptitle("Graphical summary of paried variable combinations of the Iris Dataset") 
    if f_action =='view':
        plt.show()
    elif f_action =='save':
        plt.savefig('Graphical Summary' +'.png')

#=================================================================================

def displayMenu():
    #output initial menu with command and instructions for the user.
    print('Blurb abou the menu')
    #Output user choices
    print("What would you like to do?")
    print("\t(1) View variable summaries")
    print("\t(2) Save variable summaries to txt file")
    print("\t(3) View histogram for each variable")
    print("\t(4) Save histogram for each variable to png file")
    print("\t(5) View scatter plot for each variable pair comination")
    print("\t(6) Save scatter plot for each variable pair comination to png file")
    print("\t(7) View all scatter plots and histograms with species identified")
    print("\t(8) Save all scatter plots and histograms with species identified")    
    print("\t(q) Quit")
    #get user choice
    choice = input("Select a choice from the above menu: ").strip()
    #return choice to main menu
    return choice

#=================================================================================

def main():
    #create a menu function to make call variousl anayis methods

    #call readCSV to get Iris dataset as dataframe
    iris_df=readCSV()
    #print(iris_df)
    
    #call display menu function
    choice = str(displayMenu())    
    #print(choice)           
    #use choice input to control flow of main while loop.
    while(choice != 'q'):
        #print("In while")        
        
    
        #1 View variable summaries
        if choice == '1':
            create_var_summary(iris_df,'view')
        #2 Save variable summaries to txt file
        elif choice == '2':
            create_var_summary(iris_df,'save')
        #3 View histogram for each variable
        elif choice == '3':
            create_var_hist(iris_df,'view')
        #4 Save histogram for each variable to png file
        elif choice == '4':
            create_var_hist(iris_df,'save')
        #5 View scatter plot for each variable pair comination
        elif choice == '5':
            create_scatter_plots(iris_df,'view')
        #6 Save scatter plot for each variable pair comination to png file
        elif choice == '6':
            create_scatter_plots(iris_df,'save')
        #7 View graphcial summary with species identified
        elif choice == '7':
            grahical_summary(iris_df,'view')
        #8 Save graphical with species identified
        elif choice == '8':
            grahical_summary(iris_df,'save')
        else:
        #call dsiplay menu to get user choice
            print("Invalid input, plese input an option from the menu.")
        print("here")
        choice=displayMenu()

            
    

if __name__=="__main__":
    main()
