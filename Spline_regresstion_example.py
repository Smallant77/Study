# %%
import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns

df = pd.read_csv('https://raw.githubusercontent.com/kirenz/datasets/master/wage.csv')

X = df[['age']]
y = df[['wage']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 1)

# seaborn settings
custom_params = {"axes.spines.right" : False, "axes.spines.top" : False}
sns.set_theme(style="ticks", rc=custom_params)

# %%
from patsy import dmatrix
# Generating cubic spline with 3 knots at 25, 40 and 60
transformed_x = dmatrix(
            "bs(train, knots=(25,40,60), degree=3, include_intercept=False)", 
                {"train": X_train},return_type='dataframe')
transformed_x.head()

# %%
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error
# Fitting generalised linear model on transformed dataset
cs = sm.GLM(y_train, transformed_x).fit()
# Training data
pred_train = cs.predict(dmatrix("bs(train, knots=(25,40,60), include_intercept=False)", {"train": X_train}, return_type='dataframe'))
rmse_train = mean_squared_error(y_train, pred_train, squared=False)

# Test data
pred_test = cs.predict(dmatrix("bs(test, knots=(25,40,60), include_intercept=False)", {"test": X_test}, return_type='dataframe'))
rmse_test =mean_squared_error(y_test, pred_test, squared=False)

# %%
import numpy as np
import matplotlib.pyplot as plt

# Create observations
xp = np.linspace(X_test.min(),X_test.max(), 100)
# Make some predictions
pred = cs.predict(dmatrix("bs(xp, knots=(25,40,60), include_intercept=False)", {"xp": xp}, return_type='dataframe'))

# plot
sns.scatterplot(x=X_train['age'], y=y_train['wage'])

plt.plot(xp, pred, label='Cubic spline with degree=3 (3 knots)', color='orange')
plt.legend();

#출처 : https://www.kirenz.com/post/2021-12-06-regression-splines-in-python/regression-splines-in-python/
