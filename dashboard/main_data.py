import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import calendar

"""## Data Wrangling

### Gathering Data
"""

df = pd.read_csv("dashboard/main_data.csv")
df

"""### Assessing Data

### *Memeriksa* tipe data dari tiap kolom
"""

df.info()

"""Semua tipe data sudah sesuai

### Cleaning Data

Handling duplicate data
"""

print("Jumlah duplikasi: ", df.duplicated().sum())

"""Handling missing value"""

df.isna().count()

"""Mengubah tipe data yang tidak sesuai"""
variabel = ['year', 'month', 'day', 'hour']
df[variabel] = df[variabel].astype('category') 

"""Fill missing value """
# Fill missing values with the constant values 
df_filled= df.fillna(0)

df_filled.isna().sum()

# Fill missing values with the mode of each column
df_filled['wd'].fillna(df_filled['wd'].mode()[0], inplace=True)


df.to_csv("cleaning.csv", index = False)