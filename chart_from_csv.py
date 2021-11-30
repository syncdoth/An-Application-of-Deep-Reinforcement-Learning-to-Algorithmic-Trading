import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np

data_dir = './Data'
stock_dict = {'APPLE': 'AAPL', 'SAMSUNG': '005930'}

def gen_chart(stock_name, data_dir=data_dir):
    csv_path_train = os.path.join(data_dir, stock_dict[stock_name] + '_2012-1-1_2018-1-1.csv')
    csv_path_test = os.path.join(data_dir, stock_dict[stock_name] + '_2018-1-1_2020-1-1.csv')
    
    df_train = pd.read_csv(csv_path_train)
    df_test = pd.read_csv(csv_path_test)

    df_train['Timestamp'] = pd.to_datetime(df_train['Timestamp'])
    df_train.reset_index(inplace=True)
    
    x = np.arange(0, len(df_train))
    fig, (ax, ax2) = plt.subplots(2, figsize=(12, 8), gridspec_kw={'height_ratios': [5, 1]})
    timestep = 30
    running_timestep = 0

    for idx, item in df_train.iterrows():
        running_timestep += 1
        color = 'r'
        if item['Open'] > item['Close']:
            color= 'g'
        ax.plot([x[idx], x[idx]], [item['Low'], item['High']], 
                color=color)
        ax.plot([x[idx], x[idx]-0.1], [item['Open'], item['Open']], 
                color=color)
        ax.plot([x[idx], x[idx]+0.1], [item['Close'], item['Close']], 
                color=color)
        ax2.bar(x, df_train['Volume'], color='lightgrey')
        
        if running_timestep == timestep:
            break
    
    plt.show()




gen_chart('APPLE')
gen_chart('SAMSUNG')
