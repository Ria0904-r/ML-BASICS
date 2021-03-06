#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas


# In[3]:


df=pandas.read_csv("Housing Prices.csv")


# In[4]:


df


# In[5]:


df.dtypes
#to find data types of variable


# In[6]:


df.head(10)
#to display top 10 rows 


# In[7]:


df.tail(10)
#to display last 10 rows of data set


# In[8]:

df.describe()

#include string and category variable
df.describe(include='all')

df.info()

#Descriptive statistics for a single variable

df['Sale Price'].mean()
df['Sale Price'].min()
df['Sale Price'].max()
df['Sale Price'].std()
#std deviation

df['Sale Price'].quantile(.25)

#unique  function
#it is used for a string variable for finding out theunique values that exist for that variable in the data set
df['Condition of the House'].unique()


# Now we will use numpy to calculate the standard deviation

import numpy as np

np.std(df['Sale Price'])

#There is diff in std deviation while calculating with different methods because the formula is different
df['Sale Price'].std()-np.std(df['Sale Price'])

#We can fix this By putting degree of freedom as 1
np.std(df['Sale Price'],ddof=1)


#Visualizing using graphs

import matplotlib.pyplot as plt
#line graph
#Plt.plot(X and Y values)
#x and y= Plt.plot(data_set_name[variable name])
plt.plot(df['Sale Price'])

#To label the data
plt.xlabel("Record Number")
plt.ylabel("Sale Price")

#To colour the line
plt.plot(df['Sale Price'],color='green')

#complilation of all above codes for line graph
plt.plot(df['Sale Price'],color='green')
plt.title("My first graph")
plt.xlabel("Record Number")
plt.ylabel("Sale Price")
plt.show()


#In order to modify the graphs
plt.plot(df['Sale Price'],marker='o',markerfacecolor='Blue',markersize=5,color='yellow',linewidth=5,linestyle='dashed')

#PIE CHART
df.groupby('Condition of the House')['ID'].count()
#Based on output we define two variable value and labels
values=(30,1701,14031,5679,172)
labels=('Bad','Excellent','Fair','Good','Okay')
plt.pie(values,labels=labels)

#Bar Graph
plt.bar(labels,values,color='purple',linewidth=5,linestyle='dashed')
plt.xlabel("Condition of the house")
plt.ylabel("Count of the House")
plt.title("CONDITION GRAPH")
plt.show()


#Scatter plot
plt.scatter(x=df['Flat Area (in Sqft)'],y=df['Sale Price'],color='red')
plt.xlabel("Area")
plt.ylabel("Selling Price")
plt.title("Selling Price vs Area")
plt.show()

plt.scatter(x=df['No of Bathrooms'],y = df['Sale Price'],color='red')
plt.xlabel("No of Bathrooms")
plt.ylabel("Selling Price")
plt.title("Selling Price vs No of bathrooms")
plt.show()

#Histogram
df.describe()
plt.hist(df['Age of House (in Years)'],bins=10)
plt.hist(df['Age of House (in Years)'],bins=10)
plt.xlabel("Age of House (in Years)")
plt.ylabel("No of Records")
plt.title("Age wise distribution of Houses")
plt.show()

#BOX PLOT
plt.boxplot(df['Age of House (in Years)'])


#PANDAS

#RELATION BETWEEN CONDITION OF THE HOUSE AND THE SALE PRICE

#Calculate the mean of the "Sale price with respect to the condition of the house
zip_condition_sale=df.groupby(['Condition of the House','Zipcode'])['Sale Price'].mean()  
zip_condition_sale

