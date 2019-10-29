# BNS Attribute Curve Fitting
# Author: dbnryanc92 (玉蜂丷)
# Attribute: Abnormal Attack (Lv.60)

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from scipy.optimize import curve_fit

# Allows plt to show UTF-8 chinese characters
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

# Read rawdata to dataframe
dirname = os.path.dirname(__file__)
df = pd.read_csv(dirname + '/Raw Data/rawdata_abnormal_lv60.csv', comment='#')
df = df.rename(columns={'abnormalValue': 'value', 'abnormalRate': 'rate'})

# Define a model function
def model_func(x, a, b, c):
    return b * x / (x + a) + c

# Fits the function
popt, pcov = curve_fit(model_func, df['value'], df['rate'])
print("a = {0:.9f}, b = {1:.9f}, c = {2:.9f}".format(*popt))

#Plot the result
fig = plt.figure()
ax = fig.add_subplot()
ax.plot(df['value'], df['rate'], '.b', label='訓練數據 Training Points')
x_pred = np.linspace(0, 10000)
ax.plot(x_pred, model_func(x_pred, *popt), '-', color='brown', label='最佳擬合曲線 Best Fit Curve\nA = %.4f\nB = %.4f\nC = %.4f'%(popt[0],popt[1],popt[2]))

ax.set_title('BNS劍靈 異常狀態傷害數值 Abnormal Attack Value vs 異常狀態傷害率 Abnormal Attack Rate (Lv.60版本) by 玉蜂丷 (dbnryanc92)\nSciPy Curve Fitting | ' +  r'$y=\frac{Bx}{x+A}+C$')
ax.set_xlabel('x = 異常狀態傷害數值 Abnormal Attack Value')
ax.set_ylabel('y = 異常狀態傷害率 Abnormal Attack Rate')
ax.legend(loc='lower right')

ax.set_xlim(left=0, right=10000)
ax.set_ylim(bottom=1, top=2.5)
ax.set_xticks(np.arange(0, 10001, 2000))
ax.set_xticks(np.arange(0, 10001, 500), minor=True)
ax.set_yticks(np.arange(1, 2.501, 0.5))
ax.set_yticks(np.arange(1, 2.501, 0.1), minor=True)
ax.yaxis.set_major_formatter(PercentFormatter(1))
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)
plt.show()