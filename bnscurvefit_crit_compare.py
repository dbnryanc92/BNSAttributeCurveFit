# BNS Attribute Curve Fitting
# Author: dbnryanc92 (玉蜂丷)
# Attribute: Critical (Compare)

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from scipy.optimize import curve_fit

# Allows plt to show UTF-8 chinese characters
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

# Initialiation
dirname = os.path.dirname(__file__)
fig = plt.figure()
ax = fig.add_subplot()

# Setup comparison
compare_item = ['55', '60']
colors = ['yellowgreen', 'teal']

for count, lv in enumerate(compare_item):
    df = pd.read_csv(dirname + '/Raw Data/rawdata_crit_lv' + lv + '.csv', comment='#')
    df = df.rename(columns={'critValue': 'value', 'critRate': 'rate'})

    # Define a model function
    def model_func(x, a, b, c):
        return b * x / (x + a) + c

    # Fits the function
    popt, pcov = curve_fit(model_func, df['value'], df['rate'])
    print("Lv. " + lv + ": a = {0:.9f}, b = {1:.9f}, c = {2:.9f}".format(*popt))

    # Plot the result
    #ax.plot(df['value'], df['rate'], '.', label='Lv. %s 數據'%(lv))
    x_pred = np.linspace(0, 40000)
    ax.plot(x_pred, model_func(x_pred, *popt), '-', color=colors[count], label='Lv. %s'%(lv))

# Prediction
popt2 = [11657.57, 0.97, 0]
x_pred = np.linspace(0, 40000)
ax.plot(x_pred, model_func(x_pred, *popt2), '-', color='darkgreen', label='Lv. 65? (推測)')

ax.set_title('BNS劍靈 暴擊數值 Crit Value vs 暴擊率 Crit Rate (版本比較) by 玉蜂丷 (dbnryanc92)\nSciPy Curve Fitting | ' +  r'$y=\frac{Bx}{x+A}+C$')
ax.set_xlabel('x = 暴擊數值 Crit Value')
ax.set_ylabel('y = 暴擊率 Crit Rate')
ax.legend(loc='lower right')

ax.set_xlim(left=0, right=40000)
ax.set_ylim(bottom=0, top=1)
ax.set_xticks(np.arange(0, 40001, 5000))
ax.set_xticks(np.arange(0, 40001, 1000), minor=True)
ax.set_yticks(np.arange(0, 1.001, 0.2))
ax.set_yticks(np.arange(0, 1.001, 0.05), minor=True)
ax.yaxis.set_major_formatter(PercentFormatter(1))
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)
plt.show()