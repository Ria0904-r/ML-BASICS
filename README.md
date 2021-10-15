# ML-BASICS

#Numpy Library
It is an essential library for mathematical calculations and contains several mathematical functions.

#Grouping the data
means finding count of records in each of the unique values of a variable .

The"Groupby" function groups the categorical or string variable

#Histogram
is used to plot frequency count(or simply count of records)over the range of values a variable can have
To create a Histogram , divide the data in bins.
Bins divide the entire range(difference between minimum valur and maximum value)of values for a numeric variable in 'n equal parts , where 'n' is specifies by us and count the number of records present in each of those parts.


The Bar Chart displays the percentage where as the histogram displays frequency.


#pandas.groupby()
#pandas.pivot_table()

Syntax of groupby():
dataframe.groupby(["list of colums to be group by"])["Column to be grouped"].how_to_group()

Limitations ofpandas.groupby():
1) It cannot perform very complex aggregations.
2) The formatting cannot be changes to suit our needs.

#To remove these we have pandas.pivot_table();
1)It can easily handle more complex operation.
2)It provides better representation.







