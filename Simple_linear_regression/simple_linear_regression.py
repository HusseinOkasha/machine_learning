

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.model_selection import  train_test_split
from sklearn.linear_model import LinearRegression
dataset=pd.read_csv("Salary_Data.csv")
x = dataset.iloc[:,:-1]
y = dataset.iloc[:,1]
x_train , x_test , y_train, y_test =train_test_split(x,y,test_size=1/3, random_state=0)

regressor= LinearRegression()
regressor.fit(x_train, y_train)

y_predicted= regressor.predict(x_test)
plt.scatter(x_test,y_test , color="red")
plt.plot(x_train, regressor.predict(x_train), color="blue")
plt.show()





