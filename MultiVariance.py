import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.pyplot import xticks
from matplotlib.pyplot import yticks
plt.style.use('ggplot')
#Importing The DataSet
df=pd.read_csv("Salary Data - Copy.csv")
r,c=df.shape
print(f"Number of Rows: {r}")
print(f"Number of Columns: {c}")
print("\n")

#Calculating The Statistics DataSet(Mean,SD,Median) 
stat=df.describe()
print(f"Statistics of The DataSet:\n{stat}")
print("\n")

 #Dropping The Null Values
drop=df.dropna()
print(f"Table After Dropping Null Values:\n{drop}")
print(f"Number of Rows After Dropping Null Values:{drop.shape[0]}")
print(f"Number of Columns After Dropping Null Values:{drop.shape[1]}")
print("\n")

 #Finding The Nul Values
null=df.isnull().sum()
print(f"Number of Null Values:\n{null}")
df=df.dropna()
print("\n")

#Finding The Null Values After Dropping Null Values
nan=df.isna().sum()
print(f"Number of Null Values After Dropping Null Values:\n{nan}")
columns=df.columns
print(f"Columns Name:\n{columns}")
c=df.shape
print(f'Shape of DataSet:\n{c}')

#Finding The Information of The Dataset
info=df.info()
print(f"Information of The DataSet:\n{info}")
#Plotting The DataSet
auto = df[['Age', 'Gender', 'Education Level', 'Job Title', 'Years of Experience','Salary']]
sns.pairplot(auto)#Plot Only Numerical Columns Dataset
plt.show()

#Finding The Correlation Between The Datset
auto1=df[['Age','Years of Experience','Salary']]
cor=auto1.corr()#Finding The Correlation Between The Numerical Columns
print(f"Correlation Between The Numerical Columns:\n{cor}")

#Plotting The Correlation Using HeatMap
sns.heatmap(auto1.corr(),annot=True,cmap="coolwarm",linewidths=0.5)
plt.show()

#Adding The Gender Column in a DataSet
gen=pd.get_dummies((auto['Gender']),drop_first=True)
print(f'Gender Column After Adding in DataSet:\n{gen}')
auto2=pd.concat([auto,gen],axis=1)
print(f"Gender Column After Concatenating in DataSet:\n{auto2}")

#Education Level Column in a DataSet
edu=pd.get_dummies((auto['Education Level']),drop_first=True)
print(f"Education Level Column After Adding in DataSet:\n{edu}")
auto3=pd.concat([auto2,edu],axis=1)
print(f'Education Level Column After Concatenating in DataSet:\n{auto3}')

#Adding The Job Title Column in a DataSet
job=auto['Job Title'].value_counts()
print(f"Job Title Column After Adding in Dataset:\n{job}")

#Dropping The Old Columns Table Such as (Gender,Education Level,Job Title)
auto4=auto3.drop(['Gender','Education Level','Job Title'],axis=1)
print(f"Table After Dropping The Duplicate Column:\n{auto4}")

#Finding The Correlation of the New DataSet
cor1=auto4.corr()
print(f"Correlation of The New DataSet:\n{cor1}")
sns.heatmap(auto4.corr(),annot=True,cmap="coolwarm",linewidths=0.5)
plt.show()

#Droppinh The Unnecessary Columns
auto5=auto4.drop(['Male'],axis=1)
print(f"Dropping Male Column;\n{auto5}")
sns.heatmap(auto5.corr(),annot=True,cmap="coolwarm",linewidths=0.5)
plt.show()

#Traning and Testing The DataSet
from sklearn.model_selection import train_test_split
df_train,df_test=train_test_split(auto5,train_size=0.85,test_size=0.15,random_state=42)

#Starting The Linear Regression Model
X_train=df_train[["Age","Years of Experience","Master's","PhD"]]
y_train=df_train['Salary'].astype('int')
print(f"Training The DataSet:\n{X_train}")
print(f"Training The Target Variable:\n{y_train}")

#For Linear Regression Model
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
model=lr.fit(X_train,y_train)

#For Logistic Regression Model
from sklearn.linear_model import LogisticRegression
lg=LogisticRegression(max_iter=1000)
lg_model=lg.fit(X_train,y_train)

#For Polynomial Regression Model
from sklearn.preprocessing import PolynomialFeatures
poly=PolynomialFeatures(degree=2)
X_poly=poly.fit_transform(X_train)
pf=LinearRegression()
poly_reg=pf.fit(X_poly,y_train)

#Preparing Data For Testing
data=auto5.iloc[200:201]
print("\n")
print(f"Data For Testing:\n{data}")
actual=data['Salary']
data=data.drop(['Salary'],axis=1)
print("\n")
print(f"Data After Dropping Salary Column:\n{data}")
print("\n")

#Linear Regression Prediction
print("Linear Regression Prediction")
print(f"Prediction Salary is:{model.predict(data)}")
print(f"Actual Salary is:{actual}")
print("\n")

#Logistic Regression Prediction
print('Logistic Regression Prediction')
print(f'Prediction Salary is:{lg_model.predict(data)}')
print(f'Actual Salary is:{actual}')
print("\n")

#Polynomial Regression Prediction
print("Polynomial Regression prediction")
predict_salary=poly_reg.predict(poly.fit_transform(data))
print(f"Prediction Salary is:{predict_salary}")
print(f"Actual Salary is:{actual}")
print("\n")

#Finding The Score of Traning Regression Models
print(f"Score of Linear Regression Model is:{model.score(X_train,y_train)*100:.2f}")
print(f"Score of Logistic Regression Model is:{lg_model.score(X_train,y_train)*100:.2f}")
print(f'Score of Polynomial Regression Model is:{poly_reg.score(X_poly,y_train)*100:.2f}')

#Finding The Score of Testing Regression Models
test_data=df_test
y_test=test_data['Salary'].astype('int')
x_test=test_data.drop(['Salary'],axis=1)

print(f"Score of Linear Regression Model is:{model.score(x_test,y_test)*100:.2f}")
print(f'Score of Logistic Regression Model is:{lg_model.score(x_test,y_test)*100:.2f}')
print(f"Score of Polynomial Regression Model is:{poly_reg.score(poly.fit_transform(x_test),y_test)*100:.2f}")

#Importing The Pickle
import pickle as pk
filename='Salary-Prediction-Model.pkl'
pk.dump(model,open(filename,'wb'))

#Asking The User To Input The Data For Prediction
age=int(input('Enter Your Age:'))
years=int(input('Enter Your Years of Experience:'))
master=int(input("Enter 1 If You Have Master's Degree Otherwise Enter 0:"))
phd=int(input('Enter 1 If You Have Phd Degree Otherwise Enter 0:'))
df1=pd.DataFrame({"Age":[age],"Years of Experience":[years],"Master's":[master],'PhD':[phd]})
print(f'Data For Prediction:\n{df1}')

#Predicting The Salary Using Th Linear Regression Model
predict_salary=model.predict(df1)
print(f'Predicted Salary is:{predict_salary[0]:.2f}')

#Plotting the Data For Prediction
plt.scatter(X_train['Years of Experience'],y_train,color="red",label="Training Data")
plt.scatter(x_test['Years of Experience'],y_test,color='blue',label="Testing Data")
plt.scatter(df1['Years of Experience'],predict_salary,color="green",label="Prediction Data")
plt.legend()
plt.show()



