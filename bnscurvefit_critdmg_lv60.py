# BNS Attribute Curve Fitting
# Author: dbnryanc92 (玉蜂丷)
# Attribute: Critical Damage (Lv.60)

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
df = pd.read_csv(dirname + '/Raw Data/rawdata_critdmg_lv60.csv', comment='#')
df = df.rename(columns={'critdmgValue': 'value', 'critdmgRate': 'rate'})

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
x_pred = np.linspace(0, 25000)
ax.plot(x_pred, model_func(x_pred, *popt), '-', color='brown', label='最佳擬合曲線 Best Fit Curve\nA = %.4f\nB = %.4f\nC = %.4f'%(popt[0],popt[1],popt[2]))

ax.set_title('BNS劍靈 暴擊傷害數值 CritDmg Value vs 暴擊傷害率 CritDmg Rate (Lv.60版本) by 玉蜂丷 (dbnryanc92)\nSciPy Curve Fitting | ' +  r'$y=\frac{Bx}{x+A}+C$')
ax.set_xlabel('x = 暴擊傷害數值 Crit Dmg. Value')
ax.set_ylabel('y = 暴擊傷害率 Crit Dmg. Rate')
ax.legend(loc='lower right')

ax.set_xlim(left=0, right=25000)
ax.set_ylim(bottom=1.2, top=3.7)
ax.set_xticks(np.arange(0, 25001, 5000))
ax.set_xticks(np.arange(0, 25001, 1000), minor=True)
ax.set_yticks(np.arange(1.2, 3.701, 0.5))
ax.set_yticks(np.arange(1.2, 3.701, 0.1), minor=True)
ax.yaxis.set_major_formatter(PercentFormatter(1))
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)
plt.show()