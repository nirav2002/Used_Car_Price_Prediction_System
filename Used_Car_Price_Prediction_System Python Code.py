#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
url = ""
dataframe = pd.read_csv('C:/Users/bjaya/Downloads/vehicles.csv')
dataframe1 = pd.read_csv('C:/Users/bjaya/Downloads/vehicles.csv')


# In[2]:


dataframe


# In[3]:


dataframe.describe()


# In[4]:


#dataframe = dataframe.sort_values(by='price')


# In[5]:


import seaborn as sns

sns.heatmap(dataframe.isnull())


# In[6]:


print("Unique values in Transmission: ",dataframe['transmission'].unique())
print("Unique values in Type: ",dataframe['type'].unique())
print("Unique values in Fuel: ",dataframe['fuel'].unique())
print("Unique values in Condition: ",dataframe['condition'].unique())
print("Unique values in Title status: ",dataframe['title_status'].unique())
print("Unique values in Cylinders: ",dataframe['cylinders'].unique())
print("Unique values in Drive: ",dataframe['drive'].unique())
print("Unique values in Manufacturer: ",dataframe['manufacturer'].unique())


# In[7]:


from matplotlib import pyplot as plt
dataframe['drive'].value_counts().plot(kind='pie',title ="Drive",radius=2)


# In[8]:


from matplotlib import pyplot as plt
dataframe['manufacturer'].value_counts().plot(kind='pie',title ="Manufacturer",radius=2)


# In[9]:


from matplotlib import pyplot as plt
dataframe['transmission'].value_counts().plot(kind='pie',title ="Transmission",radius=2)


# In[10]:


from matplotlib import pyplot as plt
dataframe['type'].value_counts().plot(kind='pie',title ="Type",radius=2)


# In[11]:


dataframe['title_status'].value_counts().plot(kind='pie',title ="Title Status",radius=2)


# In[12]:


dataframe['fuel'].value_counts().plot(kind='pie',title ="Fuel",radius=2)


# In[13]:


dataframe['cylinders'].value_counts().plot(kind='pie',title ="Cylinders",radius=2)


# In[14]:


dataframe['condition'].value_counts().plot(kind='pie',title ="Condition",radius=2)


# In[15]:


dataframe=dataframe.drop('posting_date', axis=1)
dataframe=dataframe.drop('county', axis=1)
dataframe=dataframe.drop('description', axis=1)
dataframe=dataframe.drop('image_url', axis=1)
dataframe=dataframe.drop('VIN', axis=1)
dataframe=dataframe.drop('url', axis=1)
dataframe=dataframe.drop('region_url', axis=1)
dataframe=dataframe.drop('id', axis=1)
dataframe=dataframe.drop('model', axis=1)
dataframe=dataframe.drop('state', axis=1)
dataframe=dataframe.drop('lat', axis=1)
dataframe=dataframe.drop('long', axis=1)
dataframe=dataframe.drop('region', axis=1)
dataframe=dataframe.drop('paint_color', axis=1)
dataframe=dataframe.drop('size', axis=1)


# In[16]:


import seaborn as sns

sns.heatmap(dataframe.isnull())


# In[17]:


from sklearn import preprocessing
le = preprocessing.LabelEncoder()
dataframe['manufacturer'] = le.fit_transform(dataframe['manufacturer'])
dataframe['fuel'] = le.fit_transform(dataframe['fuel'])
dataframe['transmission'] = le.fit_transform(dataframe['transmission'])
dataframe['type'] = le.fit_transform(dataframe['type'])
dataframe['drive'] = le.fit_transform(dataframe['drive'])
dataframe['condition'] = le.fit_transform(dataframe['condition'])
dataframe['cylinders'] = le.fit_transform(dataframe['cylinders'])
dataframe['title_status'] = le.fit_transform(dataframe['title_status'])


# In[18]:


dataframe


# In[19]:


dataframe.corr()


# In[20]:


sns.heatmap(dataframe.corr())


# In[21]:


dataframe.describe()


# In[22]:


from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
ds=['cylinders','price','manufacturer','condition','fuel','title_status','year','transmission','drive','type','odometer']

imputer = IterativeImputer()
imputer.fit(dataframe[ds])
dataframe[ds]=imputer.transform(dataframe[ds])


# In[23]:


dataframe.corr()


# In[24]:


sns.heatmap(dataframe.corr())


# In[25]:


fig,ax = plt.subplots(figsize =(10, 7))
ax.hist(dataframe['price'], bins = [0,50000,100000,150000,200000,250000,300000])

plt.show()


# In[26]:


for i in range(len(dataframe)):
    if(dataframe['price'][i]>=100000):
        dataframe.drop(i,inplace=True)


# In[27]:


len(dataframe)


# In[28]:


sns.heatmap(dataframe.corr())


# In[29]:


import seaborn as sns

sns.heatmap(dataframe.isnull())


# In[30]:


dataframe.describe()


# In[31]:


df=dataframe.dropna()


# In[ ]:


na='price'
pIQR=dataframe[na].quantile(0.75)-dataframe[na].quantile(0.25)
pupper=dataframe[na].quantile(0.75)+1.5*pIQR
plower=dataframe[na].quantile(0.25)-1.5*pIQR

print(na)
print(dataframe[na].quantile(0.75))
print(dataframe[na].quantile(0.05))
print(pupper)
print(plower)


na='odometer'
oIQR=dataframe[na].quantile(0.75)-dataframe[na].quantile(0.25)
oupper=dataframe[na].quantile(0.75)+1.5*oIQR
olower=dataframe[na].quantile(0.25)-1.5*oIQR
dataframe=dataframe[dataframe.price<pupper]
dataframe=dataframe[dataframe.odometer<oupper]


# In[32]:


dataframe


# In[33]:


df


# In[34]:


y = df['price']
x = df.drop('price',axis= 1)


# In[35]:


# creating train and test sets

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)


# In[36]:


output=[]
output.append(["Regression Algorithm","RMSE","R Squared","Mean Squared Error","Absolute Mean Error"])


# In[37]:


from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=True)

model.fit(X_train,y_train)


predictions = model.predict(X_test)

print('Linear Regression\nmean_squared_error : ', mean_squared_error(y_test, predictions))
print('mean_absolute_error : ', mean_absolute_error(y_test, predictions))
print("R-Squared",model.score(X_test,y_test, sample_weight=None))

import matplotlib.pyplot as plt
plt.figure(figsize=(40,40))
plt.plot( y_test, predictions,'b.',alpha=0.05)
plt.plot(y_test,y_test,'r-')


mse=mean_squared_error(y_test, predictions)
mae=mean_absolute_error(y_test, predictions)
rs=model.score(X_test,y_test, sample_weight=None)
rmse=math.sqrt(mse)

output.append(["Linear Regression",rmse,rs,mse,mae])


# In[38]:


plt.figure(figsize=(40,40))
plt.plot(t.index, t.values, 'b.')


# In[39]:


from sklearn.linear_model import Ridge
model = Ridge(fit_intercept=True,random_state=1)

model.fit(X_train,y_train)
predictions = model.predict(X_test)
print('Ridge Regression\nmean_squared_error : ', mean_squared_error(y_test, predictions))
print('mean_absolute_error : ', mean_absolute_error(y_test, predictions))
print("R-Squared",model.score(X_train,y_train, sample_weight=None))

import matplotlib.pyplot as plt
plt.figure(figsize=(40,40))
plt.plot( y_test, predictions,'b.',alpha=0.05)
plt.plot(y_test,y_test,'r-')

mse=mean_squared_error(y_test, predictions)
mae=mean_absolute_error(y_test, predictions)
rs=model.score(X_test,y_test, sample_weight=None)
rmse=math.sqrt(mse)

output.append(["Ridge Regression",rmse,rs,mse,mae])


# In[40]:


plt.figure(figsize=(40,40))
plt.plot(t.index, t.values, 'b.')


# In[41]:


from sklearn.linear_model import Lasso

model = Lasso(fit_intercept=True,random_state=1)
model.fit(X_train,y_train)
predictions = model.predict(X_test)
print('Lasso\nmean_squared_error : ', mean_squared_error(y_test, predictions))
print('mean_absolute_error : ', mean_absolute_error(y_test, predictions))
print("R-Squared",model.score(X_train,y_train, sample_weight=None))

import matplotlib.pyplot as plt
plt.figure(figsize=(40,40))
plt.plot( y_test, predictions,'b.',alpha=0.05)
plt.plot(y_test,y_test,'r-')



mse=mean_squared_error(y_test, predictions)
mae=mean_absolute_error(y_test, predictions)
rs=model.score(X_test,y_test, sample_weight=None)
rmse=math.sqrt(mse)

output.append(["Lasso",rmse,rs,mse,mae])


# In[42]:


plt.figure(figsize=(40,40))
plt.plot(t.index, t.values, 'b.')


# In[43]:


from sklearn.tree import DecisionTreeRegressor
from sklearn import tree
model = DecisionTreeRegressor(max_depth=47,max_features='auto',random_state=1)

model.fit(X_train,y_train)
predictions = model.predict(X_test)
print('Decision Tree Regressor\nmean_squared_error : ', mean_squared_error(y_test, predictions))
print('mean_absolute_error : ', mean_absolute_error(y_test, predictions))
print("R-Squared",model.score(X_train,y_train, sample_weight=None))

import matplotlib.pyplot as plt
plt.figure(figsize=(40,40))
plt.plot( y_test, predictions,'b.',alpha=0.05)
plt.plot(y_test,y_test,'r-')



mse=mean_squared_error(y_test, predictions)
mae=mean_absolute_error(y_test, predictions)
rs=model.score(X_test,y_test, sample_weight=None)
rmse=math.sqrt(mse)

output.append(["Decision Tree Regressor",rmse,rs,mse,mae])


# In[44]:


plt.figure(figsize=(40,40))
plt.plot(t.index, t.values, 'b.')


# In[48]:


from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=100,max_depth=41,max_features='log2',random_state=1)

model.fit(X_train,y_train)
predictions = model.predict(X_test)
print('Random Forest Regressor\nmean_squared_error : ', mean_squared_error(y_test, predictions))
print('mean_absolute_error : ', mean_absolute_error(y_test, predictions))
print("R-Squared",model.score(X_train,y_train, sample_weight=None))

import matplotlib.pyplot as plt
plt.figure(figsize=(40,40))
plt.plot( y_test, predictions,'b.',alpha=0.05)
plt.plot(y_test,y_test,'r-')




mse=mean_squared_error(y_test, predictions)
mae=mean_absolute_error(y_test, predictions)
rs=model.score(X_test,y_test, sample_weight=None)
rmse=math.sqrt(mse)

output.append(["Random Forest Regressor",rmse,rs,mse,mae])


# In[49]:


plt.figure(figsize=(40,40))
plt.plot(t.index, t.values, 'b.')


# In[51]:


from sklearn.neural_network import MLPRegressor
model=MLPRegressor(hidden_layer_sizes=(20,20,20,1),activation='relu',learning_rate='adaptive', learning_rate_init=0.00001, solver='adam', max_iter=1300,random_state=1)
model.fit(X_train,y_train)
predictions = model.predict(X_test)
print('MLP Regressor\nmean_squared_error : ', mean_squared_error(y_test, predictions))
print('mean_absolute_error : ', mean_absolute_error(y_test, predictions))
print("R-Squared",model.score(X_train,y_train, sample_weight=None))

import matplotlib.pyplot as plt
plt.figure(figsize=(40,40))
plt.plot( y_test, predictions,'b.',alpha=0.05)
plt.plot(y_test,y_test,'r-')



mse=mean_squared_error(y_test, predictions)
mae=mean_absolute_error(y_test, predictions)
rs=model.score(X_test,y_test, sample_weight=None)
rmse=math.sqrt(mse)

output.append(["MLP Regressor",rmse,rs,mse,mae])


# In[52]:


plt.figure(figsize=(40,40))
plt.plot(t.index, t.values, 'b.')


# In[ ]:


from sklearn.linear_model import BayesianRidge
model=BayesianRidge(fit_intercept=True)

model.fit(X_train,y_train)
predictions = model.predict(X_test)
print('Bayesian Ridge Regressor\nmean_squared_error : ', mean_squared_error(y_test, predictions))
print('mean_absolute_error : ', mean_absolute_error(y_test, predictions))
print("R-Squared",model.score(X_train,y_train, sample_weight=None))

import matplotlib.pyplot as plt
plt.figure(figsize=(40,40))
plt.plot( y_test, predictions,'b.',alpha=0.05)
plt.plot(y_test,y_test,'r-')




mse=mean_squared_error(y_test, predictions)
mae=mean_absolute_error(y_test, predictions)
rs=model.score(X_test,y_test, sample_weight=None)
rmse=math.sqrt(mse)

output.append(["Bayesian Ridge Regressor",rmse,rs,mse,mae])


# In[ ]:


plt.figure(figsize=(40,40))
plt.plot(t.index, t.values, 'b.')


# In[ ]:


from lightgbm import LGBMRegressor
model=LGBMRegressor(max_depth=13,random_state=1)

model.fit(X_train,y_train)
predictions = model.predict(X_test)
print('LGBM Regressor\nmean_squared_error : ', mean_squared_error(y_test, predictions))
print('mean_absolute_error : ', mean_absolute_error(y_test, predictions))
print("R-Squared",model.score(X_train,y_train, sample_weight=None))
t=abs(predictions-y_test)
temp=t.values
c=0
for i in temp:
    if (i<10000):
        c+=1
print("\nAccuracy: ",c/len(temp))
import matplotlib.pyplot as plt
plt.figure(figsize=(40,40))
plt.plot(X_test.index, predictions, 'r.')
plt.plot(X_test.index, y_test, 'b.')


mse=mean_squared_error(y_test, predictions)
mae=mean_absolute_error(y_test, predictions)
rs=model.score(X_test,y_test, sample_weight=None)
rmse=math.sqrt(mse)

output.append(["LGBM Regressor",rmse,rs,mse,mae])


# In[ ]:


plt.figure(figsize=(40,40))
plt.plot(t.index, t.values, 'b.')


# In[ ]:


import xgboost as xg
model=xg.XGBRegressor(max_depth=32,random_state=1)

model.fit(X_train,y_train)
predictions = model.predict(X_test)
print('XGB Regressor\nmean_squared_error : ', mean_squared_error(y_test, predictions))
print('mean_absolute_error : ', mean_absolute_error(y_test, predictions))
print("R-Squared",model.score(X_train,y_train, sample_weight=None))

import matplotlib.pyplot as plt
plt.figure(figsize=(40,40))
plt.plot( y_test, predictions,'b.',alpha=0.05)
plt.plot(y_test,y_test,'r-')




mse=mean_squared_error(y_test, predictions)
mae=mean_absolute_error(y_test, predictions)
rs=model.score(X_test,y_test, sample_weight=None)
rmse=math.sqrt(mse)

output.append(["XGB Regressor",rmse,rs,mse,mae])


# In[ ]:


plt.figure(figsize=(40,40))
plt.plot(t.index, t.values, 'b.')


# In[ ]:


from sklearn.ensemble import GradientBoostingRegressor
model=GradientBoostingRegressor(max_depth=21,random_state=1)

model.fit(X_train,y_train)
predictions = model.predict(X_test)
print('XGB Regressor\nmean_squared_error : ', mean_squared_error(y_test, predictions))
print('mean_absolute_error : ', mean_absolute_error(y_test, predictions))
print("R-Squared",model.score(X_train,y_train, sample_weight=None))

import matplotlib.pyplot as plt
plt.figure(figsize=(40,40))
plt.plot( y_test, predictions,'b.',alpha=0.05)
plt.plot(y_test,y_test,'r-')




mse=mean_squared_error(y_test, predictions)
mae=mean_absolute_error(y_test, predictions)
rs=model.score(X_test,y_test, sample_weight=None)
rmse=math.sqrt(mse)
output.append(["Gradient Boosting Regressor",rmse,rs,mse,mae])


# In[ ]:


plt.figure(figsize=(40,40))
plt.plot(t.index, t.values, 'b.')


# In[ ]:


#output.pop(4)
output


# In[ ]:




