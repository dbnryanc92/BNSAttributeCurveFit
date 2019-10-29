# BNS Attribute Curve Fitting (Polynomial Regression)
# Author: dbnryanc92 (玉蜂丷)
# Attribute: Critical (Lv.60)

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from sklearn import datasets, linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.pipeline import make_pipeline
from sklearn.exceptions import DataConversionWarning

import warnings
warnings.filterwarnings('ignore')

# Allows plt to show UTF-8 chinese characters
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

# Read rawdata to dataframe
dirname = os.path.dirname(__file__)
df = pd.read_csv(dirname + '/Raw Data/rawdata_crit_lv60.csv', comment='#')
X_train = df[['critValue']]
y_train = df[['critRate']]

x_plot = np.linspace(0, 30000)
colors = ['teal', 'yellowgreen', 'gold']
fig = plt.figure()
ax = fig.add_subplot()


for count, degree in enumerate([3, 4, 5]):
    model = make_pipeline(PolynomialFeatures(degree), Ridge())
    model.fit(X_train, y_train)
    y_plot = model.predict(x_plot.reshape(-1,1))
    ax.plot(x_plot, y_plot, color=colors[count], label="Degree %d 次" % degree)

ax.plot(X_train, y_train, color='brown', label="真實數據 Ground Truth")
ax.plot(X_train, y_train, '.b', label='訓練數據 Training Points')

ax.set_title('BNS劍靈 暴擊數值 Crit Value vs 暴擊率 Crit Rate (Lv.60版本)\nPolynomial regression of degree 3, 4, 5\n作者：玉蜂丷（dbnryanc92）')
ax.set_xlabel('x = 暴擊數值 Crit Value')
ax.set_ylabel('y = 暴擊率 Crit Rate')
ax.legend(loc='lower right')

ax.set_xlim(left=0, right=30000)
ax.set_ylim(bottom=0, top=1)
ax.set_xticks(np.arange(0, 30001, 5000))
ax.set_xticks(np.arange(0, 30001, 1000), minor=True)
ax.set_yticks(np.arange(0, 1.001, 0.2))
ax.set_yticks(np.arange(0, 1.001, 0.05), minor=True)
ax.yaxis.set_major_formatter(PercentFormatter(1))
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)
plt.show()