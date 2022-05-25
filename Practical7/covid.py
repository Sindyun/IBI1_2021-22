#import a few python libraries first
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#the code for importing the .csv file
os.chdir("C:/Users/86188")
covid_data = pd.read_csv("full_data.csv")
#the code for showing the first and third columns from rows 10-20(inclusive).
covid_data.iloc[10:21,0:3:2]
#find row where location is "Afghanistan" and print its "total cases"
L = []
i = 0
for i in range(0,7996):
 if covid_data.iloc[i,1]=="Afghanistan":
    L.append(True)
    i+=i+1
 else:
    L.append(False)
    i+=i+1

covid_data.loc[L,"total_cases"]
#for China's new cases and new deaths:
L = []
i = 0
for i in range(0,7996):
 if covid_data.iloc[i,1]=="China":
    L.append(True)
    i+=i+1
 else:
    L.append(False)
    i+=i+1

my_column = [True, False, True, True, False, False]
china_new_data = covid_data.iloc[L,my_column]

china_new_data.describe()
#print boxplot of china new cases and new deaths
new_cases = china_new_data.iloc[:,1]
new_deaths = china_new_data.iloc[:,2]
plt.boxplot(new_cases)
plt.title("New cases")
plt.ylabel("cases")
plt.show()
plt.boxplot(new_deaths)
plt.title("New deaths")
plt.ylabel("cases")
plt.show()
#plot with dates
china_dates = china_new_data.iloc[:,0]
plt.plot(china_dates, new_cases, 'b+')
plt.title("China new cases")
plt.xlabel("time")
plt.ylabel("cases")
plt.show()
#plotted both new cases and new deaths in China over time
plt.plot(china_dates, new_cases, 'ro')
plt.plot(china_dates, new_deaths, 'b+')
plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation=-25)
plt.title("China new cases and new deaths")
plt.xlabel("time")
plt.ylabel("cases")
plt.show()
#answer for questions:
L1=[]
i=1
for i in range(0,7996):
 if covid_data.iloc[i,5]==0:
    L1.append(True)
    i+=i+1
 else:
    L1.append(False)
    i+=i+1

#output the results
covid_data.loc[L1,"total_deaths"]

#0       0
#1       0
#2       0
#3       0
#4       0
#       ..
#7983    0
#7984    0
#7985    0
#7986    0
#7987    0
#Name: total_deaths, Length: 6134, dtype: int64
