import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.style.use('ggplot')

#Importing The DataSet
data=pd.read_csv("salary_data.csv")
X=data.iloc[:,:-1].values #getting value of data of all rows and all column except last column
y=data.iloc[:,1].values #getting the value of data of all rows and only last column
#splitting the DataSet

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)
from sklearn.linear_model import LinearRegression
r=LinearRegression()
r.fit(X_train,y_train)#Model that Train The Data

#Visualizing The Training Data
plt.figure(figsize=(8,5))
plt.scatter(X_train,y_train,color="red",label="Training Data",edgecolors="black",alpha=0.7) 
plt.plot(X_train,r.predict(X_train),color="blue")
plt.title("Salary and Experience(Training Set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()
plt.show()

#Visualizing The Testing Data
plt.figure(figsize=(8,5))
plt.scatter(X_test,y_test,color="red",label="Testing Data",edgecolors="black",alpha=0.7)
plt.plot(X_train,r.predict(X_train),color="blue")
plt.title("Salary and Experience(Testing Set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()
plt.show()

#Asking User Input
print("\n"+"="*30)
print("AI Salary Prediction")
print("="*30)

while True:
    print("\n")
    user_input=float ((input("Enter Any Year of Experience to Predict Your Salary:")))
    if user_input==exit:
        print("Existing The Program... , Good Bye Bro!")
        break
    try:
        predict_salary=r.predict([[user_input]])
        salary_int=int(predict_salary[0])
        print(f"Preedicted Salary For {user_input} Year of Experience is :{salary_int}")
        plt.figure(figsize=(8,5))
        
        # Plot the background "Knowledge" (Training Data)
        plt.scatter(X_train, y_train, color="lightgray", label="Other Employees", alpha=0.5)
        
        # Plot the AI's Rule (The Line)
        plt.plot(X_train, r.predict(X_train), color="blue", linewidth=2, label="Salary Trend")
        
        # Plot YOUR Prediction (The New UI Dot)
        plt.scatter([[user_input]], [salary_int], color="lime", s=50, edgecolors="black", label="YOU Are Here", zorder=10)
        
        # Add a text label next to the green dot
        plt.text(user_input + 0.5, salary_int, f'${salary_int:,}', fontsize=12, fontweight='bold')

        plt.title(f"Positioning for {user_input} Years of Experience")
        plt.xlabel("Years of Experience")
        plt.ylabel("Salary ($)")
        plt.legend()
        plt.show()
    except ValueError:
        print("Invalid Input,Please Enter a Valid Number of Year of Experience eg:(1,2)")    
            
        
        