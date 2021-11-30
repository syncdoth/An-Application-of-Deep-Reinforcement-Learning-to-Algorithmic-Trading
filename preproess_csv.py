from datetime import time
import pandas as pd
import numpy as np

#filename = input("Enter the filepath of csv: ")
filename = './Data/HistoricalQuotes.csv'

df = pd.read_csv(filename)
timestamps = []
cols = df.columns.tolist()
df = df.rename(columns={' Close/Last': 'Close', ' Volume': 'Volume', ' Open': 'Open', ' High': 'High', ' Low': 'Low'})

OHLC = ['Open', 'High', 'Low', 'Close']

for idx, item in df.iterrows():
    date = item['Date']
    mm, dd, yyyy = date.split('/')
    timestamp = '{}-{}-{}'.format(yyyy, mm, dd)
    timestamps.append(timestamp)
    for each_col in OHLC:
        new_entry = item[each_col].replace('$', '')
        df[each_col][idx] = new_entry

df['Timestamp'] = timestamps
df = df.drop(columns=['Date'], axis=1)
cols = ['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']
df = df[cols]
print(df.head())

df['Timestamp'] = pd.to_datetime(df['Timestamp'])
train_condition1 = df['Timestamp'].dt.year >= 2012
train_condition2 = df['Timestamp'].dt.year < 2018
test_condition1 = df['Timestamp'].dt.year >= 2018
test_condition2 = df['Timestamp'].dt.year < 2020

df_train = df[train_condition1]
df_train = df_train[train_condition2]
df_train.sort_values(by=['Timestamp'], inplace=True)

df_test = df[test_condition1]
df_test = df_test[test_condition2]
df_test.sort_values(by=['Timestamp'], inplace=True)


#df_train.to_csv('./Data/AAPL_2012-1-1_2018-1-1.csv', index=False)
#df_test.to_csv('./Data/AAPL_2018-1-1_2020-1-1.csv', index=False)
