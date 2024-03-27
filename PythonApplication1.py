from pickle import MARK
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas.core.groupby.generic import SeriesGroupBy
import seaborn as sns

df=pd.read_csv("company_sales_data.csv")
df.plot(x='month_number',y='total_profit')
plt.xlim(0,13)
plt.ylim(100000,500000)
plt.title("Company profit per month")
plt.show()

df.plot('month_number','total_units',marker='o',linewidth=3,color='red',linestyle='--',markerfacecolor='black')
plt.title("Company Sales data of last year")
plt.show()

df.plot(x='month_number',y=['facecream','facewash','toothpaste','bathingsoap','shampoo','moisturizer'],marker='o',
        label=['face cream sales data','face wash sales data','toothpaste sales data','bathing soap sales data','shampoo saless data','moistureize sales data'])
plt.title("sales data")
plt.ylabel("sales units in month")
plt.xlabel("month number")
plt.legend()
plt.show()

ax=df.plot(x='month_number',y='toothpaste',marker='o',color='blue',linestyle=' ',ylabel="number unit sold",xlabel="month number",title="toothpaste sales data")
plt.grid(True)
ax.xaxis.set_major_locator(plt.IndexLocator(1,0))
plt.show()

plt.figure()
plt.bar(df['month_number']-0.1,df['facecream'],width=0.3,label="face cream sales data")
plt.bar(df['month_number']+0.2,df['facewash'],width=0.3,label="face wash sales data")
plt.legend()
plt.xlabel("sales unit in number")
plt.ylabel("month number")
plt.title("sales data")
plt.grid(linestyle='--')
plt.xticks(df['month_number'])
plt.show()

plt.figure()
plt.bar(df['month_number'],df['bathingsoap'])
plt.ylabel("sales unit in number")
plt.xlabel("month")
plt.title("sales data")
plt.grid()
plt.xticks(df['month_number'])
plt.show()

plt.figure()
plt.hist(df['total_profit'],[150000,175000,200000,225000,250000,300000,350000],label="profit data")
plt.ylabel("actual profit in dollar")
plt.xlabel("profit range in dollar")
plt.title("profit data")
plt.legend()
plt.show()

total=[sum(df['facecream']),sum(df['facewash']),sum(df['toothpaste']),sum(df['bathingsoap']),sum(df['shampoo']),sum(df['moisturizer'])]
label=["face cream","face wash","toothpaste","bathing soap","shampoo","moisturizer"]
plt.pie(total,autopct='%1.1f%%',labels=label)
plt.legend()
plt.show()

f,ax=plt.subplots(2,sharex=True)
ax[0].plot(df['month_number'],df['bathingsoap'],label="bathing soap",marker='o',color='black')
ax[0].set_title("sales data of a bathingsoap")
ax[1].plot(df['month_number'],df['facewash'],label="face wash",marker='o',color='red')
ax[1].set_title("sales data of a facewash")
plt.xticks(df['month_number'])
plt.xlabel("month")
plt.ylabel("sales unit in number")
plt.show()

plt.figure()
plt.stackplot(
    df['month_number'],
    df['facecream'],
    df['facewash'],
    df['toothpaste'],
    df['bathingsoap'],
    df['shampoo'],
    df['moisturizer'],
    colors=['m','c','r','k','g','y'],
    labels=["face cream","face wash","toothpaste","bathing soap","shampoo","moisturizer"]
)
plt.legend(loc='upper left')
plt.show()
