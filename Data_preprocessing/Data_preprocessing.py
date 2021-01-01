

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importing dataset...
dataset = pd.read_csv("Data.csv")
x= dataset.iloc[:,:-1].values # all rows and coulmns excluding the last column
y= dataset.iloc[:,3].values # all values in the last column  
print(x)


#handling massing data...
from sklearn.impute import SimpleImputer

imputer=SimpleImputer(missing_values=np.nan, strategy='mean')
imputer=imputer.fit(x[:,1:]) #calculates the statistics..   
x[:,1:]=imputer.transform(x[:,1:])
print(x)

# Encoding categrical data
# why we encode the data ..??
# Ans: is that we will use mathmatical equations and we can't represent variables 
# like yes , no , france , spain.....   

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.compose import ColumnTransformer
LabelEncoder_x= LabelEncoder()
x[:,0]= LabelEncoder_x.fit_transform(x[:, 0])

# another problem arised here is that the coding of variables is 1,2,3
# which gives weights for the categories however they are the same
# so we use ColumnTransformer to create dumy variables by the number of the unique 
# categories we have. 

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
x = np.array(ct.fit_transform(x))
LabelEncoder_y= LabelEncoder()
y=LabelEncoder_y.fit_transform(y)

#spliting the dataset
from sklearn.model_selection import train_test_split
# test size determine how much of the data will be used as test data
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)
print(X_train)
print(X_test)
print(y_train)
print(y_test)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

# StandardScaler this scales the features using this formula
# z = (x - u) / s where x is the feature , u is the mean of the feature , s is it's standard deviation
X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])
X_test[:, 3:] = sc.transform(X_test[:, 3:])
print(X_train[:, 3:])
print(X_test)



