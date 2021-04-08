# pands - project 20201

## GMIT repository for Jon Ishaque - G00398244

## Higher Diploma Data Analytics GA_KDATG_L08

## Programming and Scripting Project 2021


The Iris data set is a data science standard for training and demonstration. "What most people know about the Iris dataset is that it has records on the length and width measures for sepals and petals. It was originally created by Dr. Edgar Anderson. This dataset consists of 50 records for each of three Iris species: Iris setosa, Iris virginica, and Iris versicolor." (The Iris Dataset — A Little Bit of History and Biology, 2021). It was Sir Ronal Aylmer Fisher who origially used this data set to able to distinguish between the three species of Iris. However, as a side note, Fisher's statistical analysis is less useful than the morphology of the diffent seeds of these plants noted by Anderson.

Fishers data set is a statical analysis and this lends itself to anlysis in Python. data structures such as a disctionary on a Pandas dataframe. This project will demonstrate how the dataset works and how Python can be used to illustrate this.
What units are the measurments?
Variables.
The Variables used to differetiate the clas of IRs are sepal length, sepal width, petal length and petal width.
The species of Iris is also a variable - the documentation for the dataset refers to species as class, but taxonomically the three named iris(Iris-setosa,Iris-versicolor,Iris-virginica) are species (ITIS Standard Report Page: Iris germanica, 2021)
Each sample plant that was taken, is not given a sample id in the dataset (other than row number)
Initially the project will give each sample and id which may or may not be used in the final draft.

splLnght    - float
splWdh      -float
ptlLnght    -float
ptlWdth     -float
irsSpc     -string
smpId       -int/string



The histograms, the first graphical out put produced show clusters/peaks possible idendifying species.
Petal width - noticeble high frequencies at  .2 cm, 1.4 cm, 1.8-1.9 cm
Sepal width - more of a bell curve but high freqnecies noticed at 2.4-2.5 cm, 3.1cm and 3.7cm
Petal Length - a distinct high frequecy at 1.5 cm and the two high freqencies concentrated on 4.5 cm and 5.5 cms
Sepal Lenght - High freqencies noticed at 4.8 cm, 5.7 cm and 6.3 cm
# note:


### The plan is in continuous development during the life of the project, however the final stages will remain in place for submission

1. Research phase
2. Prototyping -
    create analysis py and use it to investigate the dataset.
    read iris data file into dict object
    read iris data fild into pands dataframe    
    Create summary analysis
3. Refining and enhnancing. 
    Clean code, make it more efficient.
    What more can we say about the Iris dataset?




## Table formatting in md
| Column 1       | Column 2     | Column 3     |
| :------------- | :----------: | -----------: |
|  Cell Contents | More Stuff   | And Again    |

| You Can Also   | Put Pipes In | Like this \| |




(Data Science Example - Iris dataset, 2021)


Refererences:

Lac.inpe.br. 2021. Data Science Example - Iris dataset. [online] Available at: <http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html> [Accessed 18 March 2021].

Medium. 2021. The Iris Dataset — A Little Bit of History and Biology. [online] Available at: <https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5> [Accessed 18 March 2021]."

# pands-project2021" 

Itis.gov. 2021. ITIS Standard Report Page: Iris germanica. [online] Available at: <https://www.itis.gov/servlet/SingleRpt/SingleRpt?search_topic=TSN&search_value=43207#null> [Accessed 5 April 2021].

Lynn, S., 2021. Python Pandas read_csv: Load Data from CSV Files | Shane Lynn. [online] Shanelynn.ie. Available at: <https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/> [Accessed 5 April 2021].

Pandas.pydata.org. 2021. pandas.DataFrame — pandas 1.2.3 documentation. [online] Available at: <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html> [Accessed 5 April 2021].

pandas, E., 2021. Efficient way to get group names in pandas. [online] Stack Overflow. Available at: <https://stackoverflow.com/questions/50859987/efficient-way-to-get-group-names-in-pandas> [Accessed 5 April 2021].

Pandas.pydata.org. 2021. pandas.DataFrame.round — pandas 1.2.3 documentation. [online] Available at: <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html> [Accessed 5 April 2021].

https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/