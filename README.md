# pands - project 20201

## GMIT repository for Jon Ishaque - G00398244

## Higher Diploma Data Analytics GA_KDATG_L08

## Programming and Scripting Project 2021


The Iris data set is a data science standard for training and demonstration. "What most people know about the Iris data set is that it has records on the length and width measures for sepals and petals. It was originally created by Dr. Edgar Anderson. This data-set consists of 50 records for each of three Iris species: Iris Setosa, Iris Virginica, and Iris Versicolor." (The Iris Dataset — A Little Bit of History and Biology, 2021). It was Sir Ronal Aylmer Fisher who originally used this data set to able to distinguish between the three species of Iris. However, as a side note, Fisher's statistical analysis is less useful than the morphology of the different seeds of these plants noted by Anderson.

![Images](iris%20images.png)
(RPubs - Iris Dataset, 2021)

Fishers data set is a grid or table collection of data and this lends itself to analysis in python using data structures such as a dictionary or a Pandas data-frame. This project will demonstrate how the data-set works and how Python can be used to illustrate this.


## Variables.
The Variables used to differentiate the classes of iris are sepal length, sepal width, petal length and petal width.
The species of iris is also a variable - the documentation for the data-set refers to species as class, but taxonomically the three named iris(Iris-Setosa,Iris-Versicolor,Iris-Virginica) are species (ITIS Standard Report Page: Iris Germanica, 2021)
Each sample plant that was taken, is not given a sample id in the data-set (other than row number)

Earlier drafts had the variable names as program variables without spaces, however, pandas can handle column names with spaces and they are referenced in the program via a tuple.

Sepal Length(cm)    - float
Sepal Width(cm)      -float
Petal Length(cm)    -float
Petal Width(cm)     -float
species     -string
Id       -int/string



## Analysis.py
The program is stored in the file analysis.py and can be run from the command line in Windows on a PC with python installed.  The program users the following python libraries:

```python
import pandas as pd 
from itertools import combinations 
import seaborn as sns
import matplotlib.pyplot as plt
```

*pandas* is a python library that assists data manipulation and handling throug data structures. In this program, pandas data frames are the primary data handling data structure.

*combinations* from *itertools*, is a small utility used in this program to create an list of pair values. It used in the program to determine the correct combination of variable pairs when producing scatter plots.

*seaborn* is a data visualisation python library based on matplotlib but generates more visually appealing visualisations and is better integrated with pandas for data-frame handling. In this program it generates all of the visualisations. (Misal, 2021)

*matplotlib* is also a data visualisation python library.

Files created by the program are saved in the same directory as the program.

The program creates a default color palette for seaborn to use through out the program. 
```python
IrisPallette=['red','green','blue']
```

Two tuples are created, one containing the variable names, the other the species/class names from the Iris data set. These are used by various functions within the program.
```python
attributes  =('Sepal Length(cm)','Sepal Width(cm)','Petal Length(cm)','Petal Width(cm)')
species = ('Iris-setosa','Iris-versicolor','Iris-virginica')
```
*CleanLabel(string)* is a utility function used throughout the program, it's purpose is to tidy up labels for output headings and file names. It manipulates strings using string methods.
```python
def cleanLabel(label):
```

The following part of this README file explains via the programs menu options how python has been used and how this helps investigate the iris data set. The business logic of the program is described and the flow of the program including function calls. However, line by line technical explanations are found in the file Analysis.py

The *main()* function is called when the program first runs by the *\_\_main__* variable which ensures that it is this file that will initiate the code in this program.

The *main(*) function calls the *readCSV()* function to read the iris data set from *iris_data.csv* into a data-frame and returns the data frame(iris_df) to the main program. It is this instance of the data-frame that is a passed to the various menu choice function calls. A data-frame is a data structure used to by the *pandas* library to handle data, it contains labels, indexes and data in more than data type. (Intro to data structures — pandas 1.2.4 documentation, 2021)

A while loop  ensures the program remains open until the user inputs 'q'
```python
while(choice != 'q'):
```

A user choice menu is output by function *menu()* called from within main(). Each analytical process offers a choice of *show* or *save* for the same content.

The choice returned from the menu is passed to an if else block for all avalible options.

A snippet of the if else block handling user choice:
```python
if choice == '1':
            create_var_summary(iris_df,'view')
elif choice == '2':
            create_var_summary(iris_df,'save')
```
In the above snippet the program deals with user choices 1 and 2. Both call the same function, create_var_summary (detailed below). All menu choices pass the iris_df dataframe to the function. Each call is also passing a parameter to the function call which will determine the output for the function, *view* or *save*.

```python
def create_var_summary(iris_df,output_action):
```
Above shows the a function definition and the named parameters it will receive from the function call.
Within each main function there is a conditional statement to determine how the program will output the analysis. e.g. 
```python
if output_action =='view':
            plt.show()
elif output_action =='save':
            plt.savefig(sctTitle +'.png')
```


The program has four principal analytical functions each of which is called with an optional output described above.

**create_var_summary(iris_df,output_action)** - View variable summaries

**create_var_hist(iris_df,output_action)** - View histogram for each variable

**create_scatter_plots(iris_df,output_action)** - View scatter plot for each variable pair combination

**grahical_summary(iris_df,output_action)**  - View all scatter plots and histograms with species identified

## 1. Variable Summaries. 

```python
create_var_summary(iris_df,output_action)
```

A table for each variable is displayed with columns for a statistical summary for species, in rows. Each group is stacked vertically.

The function uses the *groupby()* method of the pandas data-frame to create groups based for each column grouped by species.  The *.describe()* method creates a statistical analysis  of the data frame.

The columns (variables) are looped through using the attributes tuple to produce a summary for each variable. The summary is  output depending on the output action.

```python
attributes_grouped = iris_df.groupby("species").describe()
```


The *.info()* method provides information on the column headings. An index value for each column name, the column name, the count of non_nulls and the data type.
It also give the memory allocation of the data provided.
Below this is the actual statistical output from the *.describe()* method.
For each species: there is a count giving the size of the sample, the mean measurement, standard deviation and 25th, 50th and 75th percentiles. Maximum and minimum measures are also show. (Python | Pandas Dataframe.describe() method - GeeksforGeeks, 2021)
```python
Petal Width(cm)
<class 'pandas.core.frame.DataFrame'>
Index: 3 entries, Iris-setosa to Iris-virginica
Data columns (total 8 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   count   3 non-null      float64
 1   mean    3 non-null      float64
 2   std     3 non-null      float64
 3   min     3 non-null      float64
 4   25%     3 non-null      float64
 5   50%     3 non-null      float64
 6   75%     3 non-null      float64
 7   max     3 non-null      float64
dtypes: float64(8)
memory usage: 216.0+ bytes
None
                 count   mean       std  min  25%  50%  75%  max
species
Iris-setosa       50.0  0.244  0.107210  0.1  0.2  0.2  0.3  0.6
Iris-versicolor   50.0  1.326  0.197753  1.0  1.2  1.3  1.5  1.8
Iris-virginica    50.0  2.026  0.274650  1.4  1.8  2.0  2.3  2.5
```

In this function, if the user has selected *view* output, then after the output the program is paused to allow the user to view the output before the menu is displayed again.
```python
x = input("Press any key to return to menu: ")
```


## 2. Histograms for each variable.
This function creates a hisotgram for each variable. Distinct histogram peaks for a species in one of the variables may enable identification of that species
```python
create_var_hist(iris_df,output_action)
```
Each species is put into its own data-frame (ir_set, ir_vir, ir_vig).

For example:

```python
ir_set =iris_df[iris_df.species=="Iris-setosa"]
```
This is so that 3 plots can be overlain on the same plot.
The attributes tuple is looped through to create a histogram for each attribute. Based on the each species data-frame (ir_set, ir_vir, ir_vig), three separate plots are produced with a differnet color for each species. 
```python
sns.histplot(ir_set[attr],   label='Iris-setosa',color='red')
sns.histplot(ir_ver[attr],   label='Iris-versicolor',color='green')
sns.histplot(ir_vig[attr],  label='Iris-virginica',color='blue')
```


seaborn(sns) histplot is used with matplotlib(plt) to create the scatter plots.(seaborn.histplot — seaborn 0.11.1 documentation, 2021). Seaborn has been used to so as to create consistent code and visualisation in the program. 

```python
for attr in attributes:
        
        plt.figure(figsize = (10, 7))
        #create a histogram for each species which will be overlain oneanother on plt.figure.
        sns.histplot(ir_set[attr],   label='Iris-setosa',color='red')
        sns.histplot(ir_ver[attr],   label='Iris-versicolor',color='green')
        sns.histplot(ir_vig[attr],  label='Iris-virginica',color='blue')
        #add legend
        plt.legend()
        #create title
        hsTitle = ('Histogram showing {} frequency for the Iris data set').format(attr)
        #add title to plots
        plt.title(hsTitle)
        #add x and y labels to plots
        plt.xlabel(cleanLabel(attr) )
        plt.ylabel('Frequency' )
```
### Histogram plots for the four variables.

![Petal Lenth Histogram](Petal%20Length.png)

![Petal Width Histogram](Petal%20Width.png)

![Sepal Length Histogram](Sepal%20Length.png)

![Sepal Width Histogram](Sepal%20Width.png)

After a plot is has been created for each species a legend is added, determining the color and name from each plot. The title is formatted and x and y labels are added.

## 3. Create a scatter plot for each pair of variables


```python
create_scatter_plots(iris_df,output_action)
```
The program creates a scatter plot of each the possible variable pairs. 
There are six possible unique pairs. 
The program determines using the combinations function of *itertools* library 
(Python - All possible pairs in List - GeeksforGeeks, 2021)

```python
varPairs = list(combinations(attributes, 2))
```

Possible pair combinations stored in the *varpairs* data structure:

[('Sepal Length(cm)', 'Sepal Width(cm)'),

('Sepal Length(cm)', 'Petal Length(cm)'), 

('Sepal Length(cm)', 'Petal Width(cm)'), 

('Sepal Width(cm)', 'Petal Length(cm)'), 

('Sepal Width(cm)', 'Petal Width(cm)'), 

('Petal Length(cm)', 'Petal Width(cm)')]

An earlier draft of the program had the plot code repeated six times once for each plot. This became increasingly difficult to maintain as the function developed so a pair data structure was introduced. The varPairs data structure is is then used to efficiently create a scatter plot for each pair via loop:
```python
for y,x in varPairs:
```
The first item in the pair being the y axis, and the second being the x axis. 

For each iteration of the loop a scatter plot is created using the seaborn facetgrid class. This class in turn uses the matplotlib.scatter class to create a scatter plot. Seaborn(sns) facetgrid is used with matplotlib(plt) to create the scatter plots. Seaborn is used so as to create consistent code and visualisation in the program.
(seaborn.FacetGrid — seaborn 0.11.1 documentation, 2021)
```python
sns.FacetGrid(iris_df, hue='species', height=5,palette=IrisPallette) \
            .map(plt.scatter, y, x) \
            .add_legend() 
        #create a title
        sctTitle = str(i) +'. ' + y +' vs.' + x 
        sctTitle = sctTitle.replace('(cm)','')
        
        plt.title(sctTitle)
```
A number for each plot is added to the title and filename.

### The six scatter plots:

![1. Sepal Length vs.Sepal Width](1.%20Sepal%20Length%20vs.Sepal%20Width.png)
![2. Sepal Length vs.Petal Length](2.%20Sepal%20Length%20vs.Petal%20Length.png)
![3. Sepal Length vs.Petal Width](3.%20Sepal%20Length%20vs.Petal%20Width.png)
![4. Sepal Width vs.Petal Length](4.%20Sepal%20Width%20vs.Petal%20Length.png)
![5. Sepal Width vs.Petal Width](5.%20Sepal%20Width%20vs.Petal%20Width.png)
![6. Petal Length vs.Petal Width](6.%20Petal%20Length%20vs.Petal%20Width.png)



## 4. Graphical summary of plots
*graphical_summary(iris_df,output_action)*

Seaborn pair plot class enables a graphical summary of scatter plots(or other plots) and histograms(or other plots to be output together as one.(seaborn.pairplot — seaborn 0.11.1 documentation, 2021)  It allows combinations of pairs of variables to be shown and analysis of single variables which form a diagonal across the plot.
the hue parameter enables the species(or other data class) to be identified in the plots based. *Corner = True,* shows only one half of the plots so a not to repeat y and x a axes swapped around. This program uses True because no additional information is gained by showing the scatters plots with swapped axes. The *diag* parameter determines the plot type for the single variable analysis. In this case hist for histogram is chosen, but other plots could have been uses, for example box plots or *kde* plots.


```python
pp=sns.pairplot(iris_df, hue="species", corner=True,diag_kind="hist",palette=IrisPallette)
```

## Other investigations into the Iris data set


## Conclusion
From the first analysis of the dataset, the variable summaries, it was clear that Iris Setosa has a distinctively smaller flower than Iris Virginica and Iris Versicolor and this pattern continued throughout the analysis. Histogram of petal width and petal length show Iris Virginica to be generally larger with these variables than Iris Versicolor.  

## Technology
The Iris data set csv file was downloaded from: http://archive.ics.uci.edu/ml/datasets/Iris

The program was created using VS Code: https://code.visualstudio.com/.

References were created using the website Cite this For Me:  https://www.citethisforme.com/

The README.md file was created using Markdown Monster: https://markdownmonster.west-wind.com/


## Refererences:

Allan, D., 2021. How to print a groupby object. [online] Stack Overflow. Available at: <https://stackoverflow.com/questions/22691010/how-to-print-a-groupby-object/36951842> [Accessed 20 April 2021].

Arora, L., 2021. Exception Handling In Python | Try and Except in Python. [online] Analytics Vidhya. Available at: <https://www.analyticsvidhya.com/blog/2020/04/exception-handling-python/> [Accessed 26 April 2021].

GeeksforGeeks. 2021. Python | Pandas Dataframe.describe() method - GeeksforGeeks. [online] Available at: <https://www.geeksforgeeks.org/python-pandas-dataframe-describe-method/> [Accessed 20 April 2021].

GeeksforGeeks. 2021. Python - All possible pairs in List - GeeksforGeeks. [online] Available at: <https://www.geeksforgeeks.org/python-all-possible-pairs-in-list/> [Accessed 20 April 2021].


Itis.gov. 2021. ITIS Standard Report Page: Iris germanica. [online] Available at: <https://www.itis.gov/servlet/SingleRpt/SingleRpt?search_topic=TSN&search_value=43207#null> [Accessed 5 April 2021].

Kaggle.com. 2021. Python - IRIS Data visualization and explanation. [online] Available at: <https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation> [Accessed 26 April 2021].

Kite.com. 2021. Code Faster with Line-of-Code Completions, Cloudless Processing. [online] Available at: <https://www.kite.com/python/answers/how-to-make-multiple-plots-on-the-same-figure-in-matplotlib-in-python#> [Accessed 11 March 2021].


Lac.inpe.br. 2021. Data Science Example - Iris dataset. [online] Available at: <http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html> [Accessed 18 March 2021].

Lamanna, F., 2021. how to save output from dataframe info to file a excel or text file. [online] Stack Overflow. Available at: <https://stackoverflow.com/questions/35436331/how-to-save-output-from-dataframe-info-to-file-a-excel-or-text-file> [Accessed 29 April 2021].

Lynn, S., 2021. Python Pandas read_csv: Load Data from CSV Files | Shane Lynn. [online] Shanelynn.ie. Available at: <https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/> [Accessed 5 April 2021].

Matthes, E., 2019. Python crash course. San Francisco, CA: No Starch Press.

McKinney, W., 2013. Python for data analysis. Beijing [etc.]: O'Reilly.

Medium. 2021. The Iris Dataset — A Little Bit of History and Biology. [online] Available at: <https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5> [Accessed 18 March 2021]."

Misal, D., 2021. Comparing Python Data Visualization Tools: Matplotlib vs Seaborn. [online] Analytics India Magazine. Available at: <https://analyticsindiamag.com/comparing-python-data-visualization-tools-matplotlib-vs-seaborn/> [Accessed 24 April 2021].

Pandas.pydata.org. 2021. pandas.DataFrame — pandas 1.2.3 documentation. [online] Available at: <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html> [Accessed 5 April 2021].

pandas, E., 2021. Efficient way to get group names in pandas. [online] Stack Overflow. Available at: <https://stackoverflow.com/questions/50859987/efficient-way-to-get-group-names-in-pandas> [Accessed 5 April 2021].

Pandas.pydata.org. 2021. pandas.DataFrame.round — pandas 1.2.3 documentation. [online] Available at: <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html> [Accessed 5 April 2021].

Pandas.pydata.org. 2021. Intro to data structures — pandas 1.2.4 documentation. [online] Available at: <https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html> [Accessed 20 April 2021].

Rpubs.com. 2021. RPubs - Iris Dataset. [online] Available at: <https://rpubs.com/ben_n/Iris_Dataset> [Accessed 26 April 2021].

Seaborn.pydata.org. 2021. seaborn.histplot — seaborn 0.11.1 documentation. [online] Available at: <https://seaborn.pydata.org/generated/seaborn.histplot.html> [Accessed 20 April 2021].

Seaborn.pydata.org. 2021. seaborn.FacetGrid — seaborn 0.11.1 documentation. [online] Available at: <https://seaborn.pydata.org/generated/seaborn.FacetGrid.html> [Accessed 20 April 2021].
https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/

Stack Overflow, 2021. Python, Pandas : write content of DataFrame into text File. [online] Stack Overflow. Available at: <https://stackoverflow.com/questions/31247198/python-pandas-write-content-of-dataframe-into-text-file> [Accessed 26 April 2021].

Seaborn.pydata.org. 2021. seaborn.pairplot — seaborn 0.11.1 documentation. [online] Available at: <https://seaborn.pydata.org/generated/seaborn.pairplot.html> [Accessed 26 April 2021].

Stack Overflow 2021. How to show the title for the diagram of Seaborn pairplot() or PridGrid(). [online] Stack Overflow. Available at: <https://stackoverflow.com/questions/36813396/how-to-show-the-title-for-the-diagram-of-seaborn-pairplot-or-pridgrid> [Accessed 26 April 2021].



