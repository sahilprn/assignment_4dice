from sklearn.linear_model import LinearRegression
import pandas as pd

data = pd.read_csv('weight-height.csv')

# Simple linear regression (Height only)
X = data[['Height']]
y = data['Weight']

model = LinearRegression()
model.fit(X, y)

print(f"R²: {model.score(X, y):.2f}")
print(f"Coefficients: {model.coef_}")
