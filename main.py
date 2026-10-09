# %% 1 
import pandas as pd
df = pd.read_csv('kc_house_data.csv', parse_dates=['date'], dtype={'zipcode': 'str'})
print(df.head())
print(df.dtypes)

# %% 2
print(df[['date', 'price', 'yr_built', 'yr_renovated', 
          'sqft_living', 'condition', 'grade', 'zipcode']].head(3))

# %%
