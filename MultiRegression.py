from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

#Creating the DataSet
x=np.array([[i] for i in range(1,21)])
y=np.array([[3*i] for i in range(1,21)])

#Training and Testing the Model
X_train, X_test, y_train, y_test =train_test_split(x,y,test_size=0.3 ,random_state=42)
model=LinearRegression()
model.fit(X_train,y_train) #y=mx+c
#Testing the Model
test=model.score(X_test,y_test)
print(f"Training The Data:len{X_train} and Testing The Data:len{X_test}")
print(f"Model Testing R^2 Score:{test}")
 