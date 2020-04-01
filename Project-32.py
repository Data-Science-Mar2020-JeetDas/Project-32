# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import pandas


df = pd.read_csv("C:/Users/Jeet Das/Desktop/Project-32.csv",encoding="utf-8")

print("\n----------------------- output data :---------------------\n")
print("Project-32 : Probability (%) of dying between age 30 and exact age 70 from any of cardiovascular disease, cancer, diabetes, or chronic respiratory disease [By WHO] using Python");
print("\n------------------------------------------------------------\n")


# Question – A : get row and column numbers 

print('---------------------------------------------')
print("Dimension of the data frame = ",df.shape)
print('---------------------------------------------')

# Question – B : print column names :

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# Question - C : print available country

country = df.groupby(['Location'])[['Period']].count()
print("---------------------------------")
print("\tAvailable country names : ")
print("-------------------------------")
print(country)
print("-------------------------------")
count = 0
for row in range(len(country)): 
        count = count+1
print("total no. of country = ",count)        
print("-----------------------------\n")


# Question - D : Available years data for which data is available

years = df.groupby(['Period'])[['Location']].count()
print("---------------------------------")
print("\tAvailable years data : ")
print("-------------------------------")
print(years)
print("-------------------------------")
count = 0
for row in range(len(years)): 
        count = count+1
print("total no. of years = ",count)        
print("-----------------------------\n")



# Question - E :Types of available indicators

indicator = df.groupby(['Indicator'])[['Period']].count()
print("---------------------------------")
print("\tAvailable types of indicators : ")
print("-------------------------------")
print(indicator)
print("-------------------------------")
count = 0
for row in range(len(indicator)): 
        count = count+1
print("total no. of indicators = ",count)        
print("-----------------------------\n")


#******************* Question - 01 : 2000 : Probability (%) of dying between age 30 and exact age 70 ********************


df2000 = df[df.Period == 2000]
print("\n\n--------------[ OUTPUT for 2000 ]----------------------\n\n")
print(df2000[['Location','Period','Dim1','First Tooltip']])

df2000_both = df2000[df2000.Dim1 == 'Both sexes']
print("\n\n--------------[ OUTPUT for 2000 Both sexes ]----------------------\n\n")
print(df2000_both[['Location','Period','Dim1','First Tooltip']])
                                                         
df2000_male = df2000[df2000.Dim1 == 'Male']
print("\n\n--------------[ OUTPUT for 2000 Male ]----------------------\n\n")
print(df2000_male[['Location','Period','Dim1','First Tooltip']])
                                                         
df2000_female = df2000[df2000.Dim1 == 'Female']
print("\n\n--------------[ OUTPUT for 2000 Female ]----------------------\n\n")
print(df2000_female[['Location','Period','Dim1','First Tooltip']])

i = np.arange(len(df2000_both['Location']))
print(i)

i1 = np.arange(len(df2000_male['Location']))
print(i1)

i2 = np.arange(len(df2000_female['Location']))
print(i2)

#--------------- plot for 2000 ----------------------

plt.title('Question - 01 : 2000 : Probability (%) of dying between age 30 and exact age 70')

plt.xlabel("Country sl. no --- >")
plt.ylabel("Probability(%) --- >")
    
plt.plot(i,df2000_both['First Tooltip'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] For Both sexes")

plt.plot(i1,df2000_male['First Tooltip'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] For male only")

plt.plot(i2,df2000_female['First Tooltip'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] For Female only")

plt.legend()
plt.show()


#******************* Question - 02 : 2005 : Probability (%) of dying between age 30 and exact age 70 ********************


df2005 = df[df.Period == 2005]
print("\n\n--------------[ OUTPUT for 2005 ]----------------------\n\n")
print(df2005[['Location','Period','Dim1','First Tooltip']])

df2005_both = df2005[df2005.Dim1 == 'Both sexes']
print("\n\n--------------[ OUTPUT for 2005 Both sexes ]----------------------\n\n")
print(df2005_both[['Location','Period','Dim1','First Tooltip']])
                                                         
df2005_male = df2005[df2005.Dim1 == 'Male']
print("\n\n--------------[ OUTPUT for 2005 Male ]----------------------\n\n")
print(df2005_male[['Location','Period','Dim1','First Tooltip']])
                                                         
df2005_female = df2005[df2005.Dim1 == 'Female']
print("\n\n--------------[ OUTPUT for 2005 Female ]----------------------\n\n")
print(df2005_female[['Location','Period','Dim1','First Tooltip']])

i = np.arange(len(df2005_both['Location']))
print(i)

i1 = np.arange(len(df2005_male['Location']))
print(i1)

i2 = np.arange(len(df2005_female['Location']))
print(i2)

#--------------- plot for 2005 ----------------------

plt.title('Question - 02 : 2005 : Probability (%) of dying between age 30 and exact age 70')

plt.xlabel("Country sl. no --- >")
plt.ylabel("Probability(%) --- >")
    
plt.plot(i,df2005_both['First Tooltip'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] For Both sexes")

plt.plot(i1,df2005_male['First Tooltip'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] For male only")

plt.plot(i2,df2005_female['First Tooltip'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] For Female only")

plt.legend()
plt.show()

#******************* Question - 03 : 2010 : Probability (%) of dying between age 30 and exact age 70 ********************


df2010 = df[df.Period == 2010]
print("\n\n--------------[ OUTPUT for 2010 ]----------------------\n\n")
print(df2010[['Location','Period','Dim1','First Tooltip']])

df2010_both = df2010[df2010.Dim1 == 'Both sexes']
print("\n\n--------------[ OUTPUT for 2010 Both sexes ]----------------------\n\n")
print(df2010_both[['Location','Period','Dim1','First Tooltip']])
                                                         
df2010_male = df2010[df2010.Dim1 == 'Male']
print("\n\n--------------[ OUTPUT for 2010 Male ]----------------------\n\n")
print(df2010_male[['Location','Period','Dim1','First Tooltip']])
                                                         
df2010_female = df2010[df2010.Dim1 == 'Female']
print("\n\n--------------[ OUTPUT for 2010 Female ]----------------------\n\n")
print(df2010_female[['Location','Period','Dim1','First Tooltip']])

i = np.arange(len(df2010_both['Location']))
print(i)

i1 = np.arange(len(df2010_male['Location']))
print(i1)

i2 = np.arange(len(df2010_female['Location']))
print(i2)

#--------------- plot for 2010 ----------------------

plt.title('Question - 03 : 2010 : Probability (%) of dying between age 30 and exact age 70')

plt.xlabel("Country sl. no --- >")
plt.ylabel("Probability(%) --- >")
    
plt.plot(i,df2010_both['First Tooltip'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] For Both sexes")

plt.plot(i1,df2010_male['First Tooltip'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] For male only")

plt.plot(i2,df2010_female['First Tooltip'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] For Female only")

plt.legend()
plt.show()


#******************* Question - 04 : 2015 : Probability (%) of dying between age 30 and exact age 70 ********************


df2015 = df[df.Period == 2015]
print("\n\n--------------[ OUTPUT for 2015 ]----------------------\n\n")
print(df2015[['Location','Period','Dim1','First Tooltip']])

df2015_both = df2015[df2015.Dim1 == 'Both sexes']
print("\n\n--------------[ OUTPUT for 2015 Both sexes ]----------------------\n\n")
print(df2015_both[['Location','Period','Dim1','First Tooltip']])
                                                         
df2015_male = df2015[df2015.Dim1 == 'Male']
print("\n\n--------------[ OUTPUT for 2015 Male ]----------------------\n\n")
print(df2015_male[['Location','Period','Dim1','First Tooltip']])
                                                         
df2015_female = df2015[df2015.Dim1 == 'Female']
print("\n\n--------------[ OUTPUT for 2015 Female ]----------------------\n\n")
print(df2015_female[['Location','Period','Dim1','First Tooltip']])

i = np.arange(len(df2015_both['Location']))
print(i)

i1 = np.arange(len(df2015_male['Location']))
print(i1)

i2 = np.arange(len(df2015_female['Location']))
print(i2)

#--------------- plot for 2015 ----------------------

plt.title('Question - 04 : 2015 : Probability (%) of dying between age 30 and exact age 70')

plt.xlabel("Country sl. no --- >")
plt.ylabel("Probability(%) --- >")
    
plt.plot(i,df2015_both['First Tooltip'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] For Both sexes")

plt.plot(i1,df2015_male['First Tooltip'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] For male only")

plt.plot(i2,df2015_female['First Tooltip'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] For Female only")

plt.legend()
plt.show()

#******************* Question - 05 : 2016 : Probability (%) of dying between age 30 and exact age 70 ********************


df2016 = df[df.Period == 2016]
print("\n\n--------------[ OUTPUT for 2016 ]----------------------\n\n")
print(df2016[['Location','Period','Dim1','First Tooltip']])

df2016_both = df2016[df2016.Dim1 == 'Both sexes']
print("\n\n--------------[ OUTPUT for 2016 Both sexes ]----------------------\n\n")
print(df2016_both[['Location','Period','Dim1','First Tooltip']])
                                                         
df2016_male = df2016[df2016.Dim1 == 'Male']
print("\n\n--------------[ OUTPUT for 2016 Male ]----------------------\n\n")
print(df2016_male[['Location','Period','Dim1','First Tooltip']])
                                                         
df2016_female = df2016[df2016.Dim1 == 'Female']
print("\n\n--------------[ OUTPUT for 2016 Female ]----------------------\n\n")
print(df2016_female[['Location','Period','Dim1','First Tooltip']])

i = np.arange(len(df2016_both['Location']))
print(i)

i1 = np.arange(len(df2016_male['Location']))
print(i1)

i2 = np.arange(len(df2016_female['Location']))
print(i2)

#--------------- plot for 2016 ----------------------

plt.title('Question - 05 : 2016 : Probability (%) of dying between age 30 and exact age 70')

plt.xlabel("Country sl. no --- >")
plt.ylabel("Probability(%) --- >")
    
plt.plot(i,df2016_both['First Tooltip'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] For Both sexes")

plt.plot(i1,df2016_male['First Tooltip'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] For male only")

plt.plot(i2,df2016_female['First Tooltip'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] For Female only")

plt.legend()
plt.show()

