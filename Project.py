import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("IMVA.xlsx")
#Countries
df1 = df[["Periods", " Brunei Darussalam ", " Indonesia ", " Malaysia ", " Philippines ", " Thailand ", " Viet Nam ", " Myanmar ", " Japan ", " Hong Kong ", " China ", " Taiwan ", " Korea, Republic Of ", " India ", " Pakistan ", " Saudi Arabia ", " Kuwait ", " UAE "]]
#print(df)
#print(df1)
#Split
Countries = df1['Periods'].str.split(' ', n = 2, expand = True)
#print(Countries)
#Assign a new column named Year
df1 = df1.assign(Year=Countries[1])
df1 = df1.assign(month=Countries[2])
#print(df1.dtypes)
#print(df1)
#Convert
df1["Year"] = pd.to_numeric(df1["Year"])
#print(df1.dtypes)
#TOP 3 Countries
df3 = df1[(df1["Year"] >= 2008) & (df1["Year"] <= 2017)]
df4 = df3[[" Brunei Darussalam ", " Indonesia ", " Malaysia ", " Philippines ", " Thailand ", " Viet Nam ", " Myanmar ", " Japan ", " Hong Kong ", " China ", " Taiwan ", " Korea, Republic Of ", " India ", " Pakistan ", " Saudi Arabia ", " Kuwait ", " UAE "]]
ps = df4.sum().sort_values(ascending=False)
top3countries = ps.head(3)
top3countries.index
#print(ps)
#print(top3countries)
import numpy as np
index = np.arange(len(top3countries.index))
plt.figure(figsize=(10, 10))
plt.xlabel('Countries (Others)', fontsize=10)
plt.ylabel('No. of Travellers (in thousands)', fontsize=8)
plt.xticks(index, top3countries.index, fontsize=7, rotation=60)
plt.title('Top 3 Asian Countries between 2008-2017 (Period 2008-2017)')
plt.bar(top3countries.index, top3countries.values/1000)
plt.show();

index = np.arange(len(ps.index))
plt.xlabel('Countries (Others)', fontsize=10)
plt.ylabel('No. of Travellers (in thousands)', fontsize=8)
plt.xticks(index, ps.index, fontsize=7, rotation=60)
plt.title('Total Asian Countries between 2008-2017 (Period 2008-2017)')
plt.bar(ps.index, ps.values/1000)
plt.show();