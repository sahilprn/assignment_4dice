import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the diabetes dataset
diabetes = load_diabetes()

# Create a DataFrame for better visualization
data = pd.DataFrame(data=diabetes.data, columns=diabetes.feature_names)
data['target'] = diabetes.target

# Split the data into training and testing sets
X = data.drop(columns='target')  # Features
y = data['target']  # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and fit the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Display results
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Model R^2 Score (Train):", model.score(X_train, y_train))
print("Model R^2 Score (Test):", model.score(X_test, y_test))

# Optional visualization - comparing predicted vs actual values
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue', label='Predicted vs Actual')
plt.xlabel('Actual Target')
plt.ylabel('Predicted Target')
plt.title('Linear Regression Results')
plt.legend()
plt.grid()
plt.show()