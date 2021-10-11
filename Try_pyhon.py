# this code show how you can write code in GitHub
print("this is try python")
%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
import numpy as np
# simple mathematical operations 
a=10
b=122
c= a+b
print('the sum of two numbers is : ',c)
print('Subtruction is given be: ',b-c)
print('Multiplication is :', a * b)
print('division with decimal:',b/a)
print('division with rounded: ', b//a)
# Data Explanatory
path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df = pd.read_csv(path)
df.head()
# To install Seaborn we use pip 
%%capture
!pip install seaborn
# to calculate the relationship b/ entities use corr
df.corr()
# Posetive Linear relation 
sns.regplot(x='engine-size', y='price', data= df)
plt.ylim(0,)
# We can exminethe correlation b/n engine size and price by
df[['engine-size','price']].corr()
