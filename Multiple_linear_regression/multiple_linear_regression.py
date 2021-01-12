'''
The p-value: is actually the probability of getting a sample like ours.
High p-value: means it's more likely to have a sample like ours
(not strange).

A small p-value: (typically ≤ 0.05) indicates strong evidence against
the null hypothesis, so you reject the null hypothesis.

A large p-value: (> 0.05) indicates weak evidence against the null
hypothesis, so you fail to reject the null hypothesis.

Null hypothesis:the hypothesis that there is no significant difference
between specified populations, any observed difference being due to 
sampling or experimental error.

so in backward elimination when we say that we will remove
the predictor with the highest p-value if it's greater than sl(0.05)
that because it means that the predictor is similar to the others

'''
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.compose import ColumnTransformer

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset=pd.read_csv("50_Startups.csv")
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,4].values

LabelEncoder_x= LabelEncoder()
x[:,3]= LabelEncoder_x.fit_transform(x[:, 3])
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
x = np.array(ct.fit_transform(x))

#avoiding the dummy variable trap.
x=x[:,1:]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)


regressor= LinearRegression()
regressor.fit(x_train, y_train) 

y_predict= regressor.predict(x_test)

 








