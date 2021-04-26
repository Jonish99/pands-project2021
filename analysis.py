'''A program that will investigate the Iris dataset. 
GMIT - GA_KDATG_L08 Y4. Programming and Scripting Project 2021'''

#Author: Jon Ishaque G00398244



#====================================IMPORTS==================================
#IMPORTS
import pandas as pd  #alias pd


from itertools import combinations  #used to created a paired list to simplify the scatter plot creation.

import matplotlib.pyplot as plt #alias plt

import seaborn as sns

#create a palette to be used in the scatter plot which will be consistent with histograms and graphical summary
IrisPallette=['red','green','blue']
#=================================================================================

#attribute names, a tuple used through out the exploration of the data set. 
col_names  =('Sepal Length(cm)','Sepal Width(cm)','Petal Length(cm)','Petal Width(cm)','species')
attributes  =('Sepal Length(cm)','Sepal Width(cm)','Petal Length(cm)','Petal Width(cm)')
#species tuple
species=('Iris-setosa','Iris-versicolor','Iris-virginica')

#=================================================================================
#===================================== FUNCTIONS =================================
#=================================================================================

#clean label utiltity funciton to tidy up strings
def cleanLabel(label):
    label = label.replace('_',' ')
    label=label.title()
    label = label.replace('(Cm)','(cm) ')
    return label

#=================================================================================
#function that reads the whole dataset into a dataframe
#it returs the iris dataframe which is pass in turn passed to various functions based on menu choice in main()

def readCSV():
        #https://www.analyticsvidhya.com/blog/2020/04/exception-handling-python/
    #Read the whole csv file into the  a pandas dataframe, irisdf - used through this program
    try:
        irisdf= pd.read_csv("iris_data.csv",  header = None, names =col_names) 
    
    except FileNotFoundError:
        print('iris_data.csv not found')
    except Exception as e:
        print('ERROR: ', e.message, e.args)
    
    #returnt to main function
    return irisdf
#========================================================================================
#================================ Menu choices 1 & 2 ====================================
#========================================================================================
#Create variable summaries, menu choices 1 & 2
def create_var_summary(iris_df,f_action):
    #use the groupby method to group the dataframe by the columnspecies, 
    #this will group the other four columns(variables) based on unique cells in species 
    #(ie 3 species rows in 4 column groups).
    #The describe method creates statistical analyis for each variable.
    attributes_grouped = iris_df.groupby("species").describe()
    
    #determine view or save action
    if f_action=='view':
        #print each group stacked vertically
        for attr in attributes:            
            print(cleanLabel(attr))
            print(attributes_grouped[attr], "\n\n")
        #use input to pause the while loop, whilst use assimilates output.
        x = input("Press any key to return to menu: ")
    elif f_action=='save':
        #open a new copy/overwrite(w) existing verision of txt file to save summaries to.
        with open('Iris_Variable_Summaries.txt', 'w') as f:
            #write file header
            f.write("This file contains statistical summaries of each variable in the iris dataset ."+'\n'+'\n')
            #use attribute names to loop through groups. 
            #i.e. for each variable in the list do...
            for attr in attributes:         
            
                #write variable summary headerheader, using col name and cleaning using clean label function
                f.write (cleanLabel(attr)+'\n'+'\n')               
                #new df based on group
                dfTmp = attributes_grouped[attr]
                #Iris_Sum_decimals = pd.Series([2,3,2,3,3,3,2], index=['mean', 'std','min','25%','50%','75%','max']) #(pandas.DataFrame.round — pandas 1.2.3 documentation, 2021)
                dfTmp.round({'mean ':2, 'std ':2,'min ':2,'25% ':2,'50% ':2,'75% ':2,'max ':2}) #Not working                         
                dfTmp.to_string(f)
                f.write ('\n'+'\n')    
        f.close()

#================================ Menu choices 3 & 4 ====================================
#Create variable histogram
#A useful enhnacement that I have not yet implemented would be to loop through each of the species.
# Arguaably a nested loop here may be too complicated.
#=================================================================================
def create_var_hist(iris_df,f_action):
    #Get each species into one dataframe
    ir_set =iris_df[iris_df.species=="Iris-setosa"]
    ir_ver =iris_df[iris_df.species=="Iris-versicolor"]
    ir_vig =iris_df[iris_df.species=="Iris-virginica"]

    sns.set(style="white", color_codes=True)
    #sns.set_palette("husl")
    
    for attr in attributes:
        
        plt.figure(figsize = (10, 7))
        #create a histogram for each species which will be overlain oneanother on plt.figure.
        sns.histplot(ir_set[attr],   label='Iris-setosa',color='red')
        sns.histplot(ir_ver[attr],   label='Iris-versicolor',color='green')
        sns.histplot(ir_vig[attr],  label='Iris-virginica',color='blue')
            
        #add legend
        plt.legend()
        #create title
        hsTitle = ('Histogram showing {} frequency for the Iris data set').format(cleanLabel(attr))
        #add title to plots
        plt.title(hsTitle)
        #add x and y labels to plots
        plt.xlabel(cleanLabel(attr) )
        plt.ylabel('Frequency' )       
        
        #determine view or save action
        if f_action =='view':
            plt.show()
        elif f_action=='save':
        #save and clean '(cm)' off file name
            plt.savefig(attr.replace('(cm)','') +".png")
     

#================================ Menu choices 5 & 6 ====================================
#Create scatter plots for variable pair combinations 
#=================================================================================
def  create_scatter_plots(iris_df,f_action):
    #https://www.geeksforgeeks.org/python-all-possible-pairs-in-list/
    # create a paried list of all pair combinations for scatter plots. (6 not 12)
    varPairs = list(combinations(attributes, 2))
    #print(varPairs)
    #counter for file and title number
    i = 1
    
    #loop through each pair creating a scatter
    #use seaborn facetgrid. pass dataframe, hue makes each species a different colour
    for y,x in varPairs:
        sns.FacetGrid(iris_df, hue='species', height=5,palette=IrisPallette) \
            .map(plt.scatter, y, x) \
            .add_legend() 
        #create a title
        sctTitle = str(i) +'. ' + y +' vs.' + x 
        sctTitle = sctTitle.replace('(cm)','')
        
        plt.title(sctTitle)
        #adujst top of plot to prevent title being cut off.
        plt.subplots_adjust(top=0.88)

        #determine view or save action
        if f_action =='view':
            plt.show()
        elif f_action =='save':
            plt.savefig(sctTitle +'.png')        
        i += 1 
        #print (sctTitle)

#================================ Menu choices 7 & 8 ====================================
#Create overall graphical summary
#=================================================================================
def grahical_summary(iris_df,f_action):
    #The six possible pair comparions are best shown together, to determine which (if any)
    #are better identifiers of species.
    #Hue enable different identification of each species by assigning a different color to each species
    #the corner parameter enable the plot to show just one half of the diagonal. 
    #The benefit of this is that whilst seeing the plots together is very useful, 
    #repeating the same plots with the axes inverted is too much information. 
    #the diagonal in this example produced historgrams, for each of the four variables, 
    # with the 3 species overlain one another. Other diagonal plots could be used for to visualise each of the four variables.

    #set the style parameter and colors for this use of seaborn
    sns.set(style="white")#background
    #create a paiplot - pp
    pp=sns.pairplot(iris_df, hue="species", corner=True,diag_kind="hist",palette=IrisPallette)
    #use suptitle to add title to whole graphci 
    pp.fig.suptitle("Graphical summary of paired variable combinations of the Iris Dataset") 
    
    #determine view or save action
    if f_action =='view':
        plt.show()
    elif f_action =='save':
        plt.savefig('Graphical Summary' +'.png')

#=================================================================================
def displayMenu():
    #output initial menu with command and instructions for the user.
    print('Please select one of the choices below to explor the Iris data set')
    print('Each functions of the program has a pair of options, which allow you to save output or view it on screen')
    print('The option list progresses in complexity of analyis, the higher the numeric choice.')
    print(' Users may choose to do this to and gradually explore the data set, or dive in at any point to view analysis.')
    #Output user choices
    print("What would you like to do? ")
    print("\n\t(1) View variable summaries")
    print("\t(2) Save variable summaries to txt file")
    print("\t(3) View histogram for each variable")
    print("\t(4) Save histogram for each variable to png file")
    print("\t(5) View scatter plot for each variable pair comination")
    print("\t(6) Save scatter plot for each variable pair comination to png file")  
    print("\t(7) View all scatter plots and histograms with species identified")
    print("\t(8) Save all scatter plots and histograms with species identified")  
    print("\t(q) Quit")
    #get user choice
    choice = input("\nSelect a choice from the above menu: ")
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
        #8 Save graphical with species identified
        elif choice == '7':
            grahical_summary(iris_df,'view')
        #10 Save graphical with species identified
        elif choice == '8':
            grahical_summary(iris_df,'save')
        else:
        #call dsiplay menu to get user choice
            print("Invalid input, plese input an option from the menu.")
        #print("here")
        choice=displayMenu()

if __name__=="__main__":
    main()
