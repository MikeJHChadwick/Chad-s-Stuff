import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics as st

df_woo = pd.read_csv('C:/Users/Learner_9ZH3Z126/2023_data_engineering/sammis_python_work/Chad\'s Stuff/woocommerce-product-export.csv')

# Print(df_woo.info)
# print(df_woo.describe())
# print(df_woo.head())
# print(df_woo.tail())
### question 7
print(df_woo[['total_profit', 'month_number']])
df_bar = df_woo[['total_profit', 'month_number']]
total_bar = df_bar.groupby('month_number').sum()
total_bar.plot(kind='bar',  legend=False, width=.8)
plt.xlabel('Month number') # add to x-label to the plot
plt.ylabel('Total profit') # add y-label to the plot
plt.title('Company profit per month') # add title to the plot
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.xticks(range(1,13,2))
plt.grid(linestyle='--')
plt.show()
### question 8
# df_line = df_woo[['total_profit', 'month_number']]
# total_line = df_line.groupby('month_number').sum()
# total_line.plot(kind='line', linestyle='dashed', color='red', 
#                 marker='o', markerfacecolor= 'black', markersize=5, linewidth=3)
# plt.xlabel('Month number') # add to x-label to the plot
# plt.ylabel('Total profit') # add y-label to the plot
# plt.title('Company profit per month') # add title to the plot
# plt.yticks([100000, 200000, 300000, 400000, 500000])
# plt.xticks(range(1,13))
# plt.legend(['Profit data of last year'], loc='lower right')
# plt.show()
### question 9
# df_products = df_woo[['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']]
# df_products.plot(kind='line', marker='o')
# plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
# plt.xticks(df_products.index, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# plt.legend(['Face cream Sales Data', 'Face Wash Sales Data', 'Toothpaste Sales Data', 'Bathing Soap Sales Data', 
#            'Shampoo Sales Data', 'Moisturizer Sales Data'])
# plt.show()
### question 10
# df_bs = df_woo['bathingsoap']
# plt.scatter(range(1,13), df_bs)
# plt.grid(linestyle='--')
# plt.xlabel('Month Number')
# plt.ylabel('Number of units Sold')
# plt.title('bathingsoap Sales data')
# plt.legend(['bathing soap Sales data'])#dunno why I have to add it in a list to get it to print out properly
# plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# plt.show()
### section 2
# date=['25/12','26/12','27/12']
# temp=[8.5, 10.5, 6.8]
# plt.plot(date, temp)
# plt.xlabel('Date')
# plt.ylabel('temperature')
# plt.title('Date-wise Temperature')
# plt.show()

# height=[121.9,124.5,129.5,134.6,139.7,147.3,152.4,157.5,162.6]
# weight=[19.7,21.3,23.5,25.9,28.5,32.1,35.7,39.6,43.2]
# # avg_height = round(st.mean(height), 1)
# # avg_weight = round(st.mean(weight))
# # print(avg_height, avg_weight)
# plt.plot(weight, height, linestyle='dashdot', color='green', marker='o', markersize=10)
# plt.xlabel('Weight in kg')
# plt.ylabel('Height in cm')
# plt.title('Average weight with respect to average height')
# plt.legend(['avg weight to height'], loc='lower right')
# plt.show()
