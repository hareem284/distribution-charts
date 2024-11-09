#importing matplotlib
import matplotlib.pyplot as plt
import pandas as pd
#importing seaborn 
import seaborn as sb
#reading csv
rcsv=pd.read_csv("gab.csv")
print(rcsv.info())
#print(rcsv.head())
#You are a part of a survey team trying to analyze the life expectancy of different categories. A dataset of Life Expectancy for different countries for 2007 is provided to various features that may be a responsible factor for different life expectancies.
#print(rcsv.groupby(['continent']).mean())
#print(grouping.head())
#making barplot
plt.bar(rcsv['continent'],rcsv['life_exp'],color='maroon')
plt.show()
sb.countplot(rcsv,x='continent',palette='winter')
plt.show()