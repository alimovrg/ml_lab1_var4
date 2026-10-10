# %% 1 
import pandas as pd
df = pd.read_csv('kc_house_data.csv', parse_dates=['date'], dtype={'zipcode': 'str'})
print(df.head(3))
print(df.dtypes)

# %% 2
df2 = df[['date', 'price', 'yr_built', 'yr_renovated', 
          'sqft_living', 'condition', 'grade',
            'zipcode']].copy()
df2['real_year'] = df2[['yr_built', 'yr_renovated']].max(axis=1)
print(df2.head(3))


# %% 3
df3 = df2.sort_values(by=['real_year', 'sqft_living', 'condition'])
print(df3.head(3))

# %% 4
df4 = df3[['real_year']].copy()
df4['count'] = df4.groupby('real_year')['real_year'].transform('count')
df4 = df4.drop_duplicates().sort_values(by='count')
print(df4.head())

# %% 5
df5 = df4[['real_year', 'count']].copy()
head2 = df5.head(2)['real_year'].tolist()
tail2 = df5.tail(2)['real_year'].tolist()
list1 = head2 + tail2
df5 = df3[df3['real_year'].isin(list1)]
print(df5['real_year'].value_counts())

# %% 6
df6 = df3[~df3['real_year'].isin(list1)]
print(df6['real_year'].value_counts().head(3))
print(len(df3))
print(len(df5))
print(len(df6))
print(len(df5) + len(df6))
print(df6['real_year'].isin([2014, 2005, 1935, 1934]).sum())

# %% 7
df7 = df6['condition'].value_counts().sort_values(ascending=False).reset_index()
print(df7)