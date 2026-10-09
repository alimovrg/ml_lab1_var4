# %% 1 
import pandas as pd
df = pd.read_csv('kc_house_data.csv', parse_dates=['date'], dtype={'zipcode': 'str'})
print(df.head())
print(df.dtypes)
