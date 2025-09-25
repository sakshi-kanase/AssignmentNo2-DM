import pandas as pd

dataset = pd.read_csv("C:/Users/Admin/Documents/sakshiTY/Data Mining/assignment2/SimpleLinearRegression.csv")
x= dataset.iloc[:,:-1].values
print (dataset)