# BNS Attribute Curve Fitting
# Author: dbnryanc92 (玉蜂丷)
# Attribute: CritDmg & AttackHit (Derivative)

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

# Define a model function
def derivate(x, a, b, c):
    return a * b / pow(x + a, 2)

# Plot
critdmgcoeff = [7201.28, 2.91, 0]
attackhitcoeff = [12002.79, 2.91, 0]
x_pred = np.linspace(0, 40000)
ax.plot(x_pred, derivate(x_pred, *critdmgcoeff), '-', label='Lv.60 暴擊傷害率提升 Increase in Crit Dmg Rate')
ax.plot(x_pred, derivate(x_pred, *attackhitcoeff), '-', label='Lv.60 功力率提升 Increase in Attack Hit Rate')

ax.set_title('BNS劍靈 屬性率的邊際提升 Marginal Increse of Attribute Rate \nby 玉蜂丷 (dbnryanc92) | ' + r'$\frac{dy}{dx}=\frac{AB}{(x+A)^2}$')
ax.set_xlabel('x = 屬性數值 Attribute Value')
ax.set_ylabel('y = 屬性率提升 Increase in Attribute Rate')
ax.legend(loc='top right')

ax.set_xlim(left=0, right=40000)
ax.set_ylim(bottom=0, top=0.0004)
ax.set_xticks(np.arange(0, 40001, 5000))
ax.set_xticks(np.arange(0, 40001, 1000), minor=True)
ax.set_yticks(np.arange(0, 0.00041, 0.0001))
ax.set_yticks(np.arange(0, 0.00041, 0.00002), minor=True)
ax.yaxis.set_major_formatter(PercentFormatter(1))
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)
plt.show()