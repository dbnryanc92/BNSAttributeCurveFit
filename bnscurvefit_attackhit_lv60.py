# BNS Attribute Curve Fitting
# Author: dbnryanc92 (玉蜂丷)
# Attribute: Attack Hit (Lv.60)

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
df = pd.read_csv(dirname + '/Raw Data/rawdata_attackhit_lv60.csv', comment='#')
df = df.rename(columns={'attackhitValue': 'value', 'attackhitRate': 'rate'})

# Define a model function
def model_func(x, a, b, c):
    return x / (a + b * x) + c

# Fits the function
popt, pcov = curve_fit(model_func, df['value'], df['rate'])
print("a = {0:.9f}, b = {1:.9f}, c = {2:.9f}".format(*popt))

#Plot the result
fig = plt.figure()
ax = fig.add_subplot()
ax.plot(df['value'], df['rate'], '.b', label='訓練數據 Training Points')
x_pred = np.linspace(0, 15000)
ax.plot(x_pred, model_func(x_pred, *popt), '-', color='brown', label='最佳擬合曲線 Best Fit Curve\nA = %.4f\nB = %.4f\nC = %.4f'%(popt[0],popt[1],popt[2]))

ax.set_title('BNS劍靈 功力數值 Attack Hit Value vs 功力傷害率 Attack Hit Rate (Lv.60版本)\nSciPy Curve Fitting | y=x/(A+Bx)+C\n作者：玉蜂丷（dbnryanc92）')
ax.set_xlabel('x = 功力數值 Attack Hit Value')
ax.set_ylabel('y = 功力傷害率 Attack Hit Rate')
ax.legend(loc='lower right')

ax.set_xlim(left=0, right=15000)
ax.set_ylim(bottom=1, top=3)
ax.set_xticks(np.arange(0, 15001, 2000))
ax.set_xticks(np.arange(0, 15001, 500), minor=True)
ax.set_yticks(np.arange(1, 3.001, 0.5))
ax.set_yticks(np.arange(1, 3.001, 0.1), minor=True)
ax.yaxis.set_major_formatter(PercentFormatter(1))
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)
plt.show()