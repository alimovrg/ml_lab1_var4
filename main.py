import pandas as pd

# 1
df = pd.read_csv('kc_house_data.csv', parse_dates=['date'], dtype={'zipcode': 'str'})
print(df.head())
print(df.dtypes)