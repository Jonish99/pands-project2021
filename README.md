# pands - project 20201

## GMIT repository for Jon Ishaque - G00398244

## Higher Diploma Data Analytics GA_KDATG_L08

## Programming and Scripting Project 2021


The Iris data set is a data science standard for training and demonstration. "What most people know about the Iris data set is that it has records on the length and width measures for sepals and petals. It was originally created by Dr. Edgar Anderson. This data-set consists of 50 records for each of three Iris species: Iris Setosa, Iris Virginica, and Iris Versicolor." (The Iris Dataset — A Little Bit of History and Biology, 2021). It was Sir Ronal Aylmer Fisher who originally used this data set to able to distinguish between the three species of Iris. However, as a side note, Fisher's statistical analysis is less useful than the morphology of the different seeds of these plants noted by Anderson.

Fishers data set is a grid or table collection of data and this lends itself to analysis in python using data structures such as a dictionary or a Pandas data-frame. This project will demonstrate how the data-set works and how Python can be used to illustrate this.


## Variables.
The Variables used to differentiate the classes of IRs are sepal length, sepal width, petal length and petal width.
The species of Iris is also a variable - the documentation for the data-set refers to species as class, but taxonomically the three named iris(Iris-Setosa,Iris-Versicolor,Iris-Virginica) are species (ITIS Standard Report Page: Iris Germanica, 2021)
Each sample plant that was taken, is not given a sample id in the data-set (other than row number)
Initially the project will give each sample an id which may or may not be used in the final draft.

splLnght    - float
splWdh      -float
ptlLnght    -float
ptlWdth     -float
irsSpc     -string
smpId       -int/string

## Analysis.py
The program is stored in the file analysis.py and be run off command line interface on a computer with python installed and the following python libraries:


```python
import pandas as pd 
from itertools import combinations 
import seaborn as sns
import matplotlib.pyplot as plt
```

*pandas* is a python library that assists data manipulation and handling throug data structures. In this program, pandas data frames are the primary data handling data structure.

*combinations* from itertools, is a small utility used in this program to create a array of pair values. Used in the program to determine the correct combination of variable pairs when producing scatter plots.

*seaborn* is a data visualisation python library based on matplotlib but generates more visually appealing visualisations and is better integrated with pandas for dataframe handling. In this program it generates all of the visualisations. (Misal 2021)

*matplotlib* is also a data visualisation python library.

Files created by the program are saved in the same directory as the program.

The program creates a default color pallete for seaborn to use throught out the program. 
```python
IrisPallette=['red','green','blue']
```

Two tuples are created, one containing the variable names, the other the species/class names from the Iris data set. These are used by various functions within the program.
```python
attributes  =('Sepal Length(cm)','Sepal Width(cm)','Petal Length(cm)','Petal Width(cm)')
species = ('Iris-setosa','Iris-versicolor','Iris-virginica')
```
There is a utility funciton used throughout the program, it's purpose is to tidy up labels for output headings and file names. It manipulates strings using string methods.
```python
def cleanLabel(label):
```

The following part of this README file explains via the programs menu options how python has been used and how this helps investigate the Iris data set. The business logic of the program is describe and the flow of the program including function calls. However, line line technical explanations are found in the file analysis.py

The main function is called on load by the __main__ variable which ensures that it is this file that will initiate the code in this program.

The main function calls the **readCSV()** function to read the iris data set in to a data-frame and returns the data frame(iris_df) to the main program. It is this instance of the data-frame that is a passed to the various menu choice function calls. A data-frame is a data structure used to by the *pandas* library to handle data. It contains labels, indexes and data in more than data type. (Intro to data structures — pandas 1.2.4 documentation, 2021)

A while loop will ensures the program remains open until the user inputs 'q'
```python
while(choice != 'q'):
```

A user choice is returned to the main() function by the menu(). Each analytical process offers a show and save choice each with the same content. 

The choice returned from the menu is passed to an if else statement for all possible conditions.

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
Above shows the functions definition and the named parameters it will receive from the function call.
Within each main function there is a conditional statement to determine how the program will output the analysis. e.g. 
 
        ```python
if output_action =='view':
            plt.show()
elif output_action =='save':
            plt.savefig(sctTitle +'.png')
```
The program has four principal analytical functions each of which is called with an optional output described above.

**create_var_summary(iris_df,output_action)** - View variable summaries

**create_var_hist(iris_df,output_action)**- View histogram for each variable

**create_scatter_plots(iris_df,output_action)** - View scatter plot for each variable pair combination

**grahical_summary(iris_df,output_action)**  - View all scatter plots and histograms with species identified

## 1. Variable Summaries. 

```python
create_var_summary(iris_df,output_action)
```

A table for each variable is displayed with columns for a statistical summary for species, in rows. Each group is stacked vertically.

The functions users the groupby method of the pandas dataframe to create groups of based for each column grouped by species. Create a group for each species. The .describe() method will create a statistical analys if of the data frame.

The remaining columns (variables) are looped through using the attributes tuple to produce a summary for each variable.
The summary is  output depending on the output action.

```python
attributes_grouped = iris_df.groupby("species").describe()
```


The .info method provides information on the column headings. An index value for each column name, the column name, the count of non_nulls and the data type.
It also give the memory allocation of the data provided.
Below this is the actual statistical output from the describe()
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

In this function, if the user has selected *view* output then after the output the program is paused to allow the user to view the output before the menu is displayed again.
```python
x = input("Press any key to return to menu: ")
```


2. Histograms for each variable.
```python
create_var_hist(iris_df,output_action)
```

Each species is put into its own dataframe (ir_set, ir_vir, ir_vig).

For example:

```python
ir_set =iris_df[iris_df.species=="Iris-setosa"]
```
This so that 3 plots can be overlain on
The attributes tuple is looped through to create a histogram for each attribute. With 3 separate plots for each species with different color plots. seaborn(sns) histplot is used with matplotlib(plt) to create the scatter plots. Seaborn is used to be so as to create consistent code and visualisation in the program.(seaborn.histplot — seaborn 0.11.1 documentation, 2021)
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
![Petal Lenth Histogram](Petal%20Length.png)

![Petal Width Histogram](Petal%20Width.png)

![Sepal Length Histogram](Sepal%20Length.png)

![Sepal Width Histogram](Sepal%20Width.png)

After a plot is has been created for each species a legend is added, determining the color and name from each plot. The title is formatted and x and y labels are added.

3. Create a scatter plot for each pair of variables
```python
create_scatter_plots(iris_df,output_action)
```
The program creates a scatter plot of each the possible variable pairs. 
There 6 possible unique pairs.
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

The var pairs data structure is then used to efficiently create a scatter plot for each pair via loop:
```python
for y,x in varPairs:
```
The first item in the pair being the y axis, and the second being the x axis. 
The scatter plot uses 

For each iteration of the loop a scatter plot is created using the seaborn facetgrid class. This class, maps uses the matplotlib.scatter class to create a scatter plot. seaborn(sns) facetgrid is used with matplotlib(plt) to create the scatter plots. Seaborn is used to be so as to create consistent code and visualisation in the program.
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

The scatter plots:
![1. Sepal Length vs.Sepal Width](1.%20Sepal%20Length%20vs.Sepal%20Width.png)
![2. Sepal Length vs.Petal Length](2.%20Sepal%20Length%20vs.Petal%20Length.png)
![3. Sepal Length vs.Petal Width](3.%20Sepal%20Length%20vs.Petal%20Width.png)
![4. Sepal Width vs.Petal Length](4.%20Sepal%20Width%20vs.Petal%20Length.png)
![5. Sepal Width vs.Petal Width](5.%20Sepal%20Width%20vs.Petal%20Width.png)
![6. Petal Length vs.Petal Width](6.%20Petal%20Length%20vs.Petal%20Width.png)



4. graphical summary of plots
grahical_summary(iris_df,output_action)
Seaborn pair plot class enables a graphical summary of scatter plots(or other plots) and histograms(or other plots to be output together as one.(seaborn.pairplot — seaborn 0.11.1 documentation, 2021)  It allows combinations of pairs of variables to be shown and analysis of single variables which form a diagonal across the plot.
the hue parameter enables the species to be identified in the plots based on species. Corner = True, shows only one half of the plots so a not to repeat y and x a axes inverted. This program uses True because no additional information is gained by showing the scatters plots with swapped axes. The *diag* parameter determines the plot type for the single variable analysis. In this case hist for histogram is chosen, but other plots could have been uses, for example box plots or kde plots.


```python
pp=sns.pairplot(iris_df, hue="species", corner=True,diag_kind="hist",palette=IrisPallette)
```





(Data Science Example - Iris dataset, 2021)


Refererences:

GeeksforGeeks. 2021. Python | Pandas Dataframe.describe() method - GeeksforGeeks. [online] Available at: <https://www.geeksforgeeks.org/python-pandas-dataframe-describe-method/> [Accessed 20 April 2021].

Lac.inpe.br. 2021. Data Science Example - Iris dataset. [online] Available at: <http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html> [Accessed 18 March 2021].

Medium. 2021. The Iris Dataset — A Little Bit of History and Biology. [online] Available at: <https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5> [Accessed 18 March 2021]."



Itis.gov. 2021. ITIS Standard Report Page: Iris germanica. [online] Available at: <https://www.itis.gov/servlet/SingleRpt/SingleRpt?search_topic=TSN&search_value=43207#null> [Accessed 5 April 2021].

Lynn, S., 2021. Python Pandas read_csv: Load Data from CSV Files | Shane Lynn. [online] Shanelynn.ie. Available at: <https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/> [Accessed 5 April 2021].

Misal, D., 2021. Comparing Python Data Visualization Tools: Matplotlib vs Seaborn. [online] Analytics India Magazine. Available at: <https://analyticsindiamag.com/comparing-python-data-visualization-tools-matplotlib-vs-seaborn/> [Accessed 24 April 2021].

Pandas.pydata.org. 2021. pandas.DataFrame — pandas 1.2.3 documentation. [online] Available at: <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html> [Accessed 5 April 2021].

pandas, E., 2021. Efficient way to get group names in pandas. [online] Stack Overflow. Available at: <https://stackoverflow.com/questions/50859987/efficient-way-to-get-group-names-in-pandas> [Accessed 5 April 2021].

Pandas.pydata.org. 2021. pandas.DataFrame.round — pandas 1.2.3 documentation. [online] Available at: <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html> [Accessed 5 April 2021].

Pandas.pydata.org. 2021. Intro to data structures — pandas 1.2.4 documentation. [online] Available at: <https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html> [Accessed 20 April 2021].

Seaborn.pydata.org. 2021. seaborn.histplot — seaborn 0.11.1 documentation. [online] Available at: <https://seaborn.pydata.org/generated/seaborn.histplot.html> [Accessed 20 April 2021].

Seaborn.pydata.org. 2021. seaborn.FacetGrid — seaborn 0.11.1 documentation. [online] Available at: <https://seaborn.pydata.org/generated/seaborn.FacetGrid.html> [Accessed 20 April 2021].
https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/

Kaggle.com. 2021. Python - IRIS Data visualization and explanation. [online] Available at: <https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation> [Accessed 26 April 2021].

Allan, D., 2021. How to print a groupby object. [online] Stack Overflow. Available at: <https://stackoverflow.com/questions/22691010/how-to-print-a-groupby-object/36951842> [Accessed 20 April 2021].

Stack Overflow, 2021. Python, Pandas : write content of DataFrame into text File. [online] Stack Overflow. Available at: <https://stackoverflow.com/questions/31247198/python-pandas-write-content-of-dataframe-into-text-file> [Accessed 26 April 2021].

Seaborn.pydata.org. 2021. seaborn.pairplot — seaborn 0.11.1 documentation. [online] Available at: <https://seaborn.pydata.org/generated/seaborn.pairplot.html> [Accessed 26 April 2021].

Stack Overflow 2021. How to show the title for the diagram of Seaborn pairplot() or PridGrid(). [online] Stack Overflow. Available at: <https://stackoverflow.com/questions/36813396/how-to-show-the-title-for-the-diagram-of-seaborn-pairplot-or-pridgrid> [Accessed 26 April 2021].

GeeksforGeeks. 2021. Python - All possible pairs in List - GeeksforGeeks. [online] Available at: <https://www.geeksforgeeks.org/python-all-possible-pairs-in-list/> [Accessed 26 April 2021].

Arora, L., 2021. Exception Handling In Python | Try and Except in Python. [online] Analytics Vidhya. Available at: <https://www.analyticsvidhya.com/blog/2020/04/exception-handling-python/> [Accessed 26 April 2021].