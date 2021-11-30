import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta, date
import cv2
import io

data_dir = './Data'
stock_dict = {'Apple': 'AAPL', 'Samsung': '005930'}
timestep = 30
suffix = {'train': '_2012-1-1_2018-1-1.csv', 'test': '_2018-1-1_2020-1-1.csv'}
 
def fig2data(fig):
    fig.canvas.draw()
    img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
    img  = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    # img is rgb, convert to opencv's default bgr
    img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    img = cv2.resize(img, (112, 112))
    
    return img


def gen_chart(stock_name, start_date, phase='train', timestep=timestep, data_dir=data_dir, save=False):
    #stock_name: APPLE, SAMSUNG
    #start_date: yyyy-dd-mm (str)
    #timestep: (int)
    #data_dir: /data/dir (str)

    csv_path = os.path.join(data_dir, stock_dict[stock_name] + suffix[phase])
    
    df = pd.read_csv(csv_path)

    #df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    #df.reset_index(inplace=True)
    
    x = np.arange(0, len(df))
    fig, (ax, ax2) = plt.subplots(2, figsize=(12, 8), gridspec_kw={'height_ratios': [5, 1]})
    running_timestep = 0

    start_idx = 0
    while True:
        if start_date in df['Timestamp'].values.tolist():
            start_idx = df['Timestamp'].values.tolist().index(start_date)
            break
        else:
            date_tmp = datetime.strptime(start_date, '%Y-%m-%d')
            date_tmp += timedelta(days=1)
            start_date = date_tmp.strftime('%Y-%m-%d')
    print('{}: from {}'.format(stock_name, start_date))
    
    df_current = df[start_idx:start_idx+timestep]
    for idx, item in df_current.iterrows():
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
        ax2.bar(x, df['Volume'], color='lightgrey')
        
        if running_timestep == timestep:
            break
    
    image = fig2data(fig)
    if save:
        date_tmp = datetime.strptime(start_date, '%Y-%m-%d')
        date_tmp += timedelta(days=timestep)
        end_date = date_tmp.strftime('%Y-%m-%d')
        cv2.imwrite('./charts/{}_{}_{}.png'.format(stock_name, start_date, end_date), image)
    #cv2.imshow('image', image)
    #cv2.waitKey(1)
    
    plt.close('all')
    return image

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2012, 1, 1)
end_date = date(2017, 11, 15) #30 business days before 12.29
end_date_test = date(2019, 11, 15)

for single_date in daterange(start_date, end_date):
    if single_date.weekday() <= 4:
        single_date = single_date.strftime('%Y-%m-%d')
        print('generating chart with ', single_date)
        for stock_name in ['Apple', 'Samsung']:
            gen_chart(stock_name, single_date, phase='train', timestep=timestep, data_dir=data_dir, save=True)

for single_date in daterange(end_date, end_date_test):
    if single_date.weekday() <= 4:
        single_date = single_date.strftime('%Y-%m-%d')
        print('generating chart with ', single_date)
        for stock_name in ['Apple', 'Samsung']:
            gen_chart(stock_name, single_date, phase='test', timestep=timestep, data_dir=data_dir, save=True)
