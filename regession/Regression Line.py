import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

height = np.array([150, 155, 160, 165, 170, 175, 180, 185, 190]).reshape(-1, 1)
weight = np.array([50, 53, 56, 61, 65, 68, 74, 78, 83])

model = LinearRegression()
model.fit(height, weight)

predicted_weight = model.predict(height)

plt.figure(figsize=(8, 5))
plt.scatter(height, weight, color='blue', label='Actual data')
plt.plot(height, predicted_weight, color='red', linewidth=2, label='Regression line')
plt.title("Height vs. Weight with Regression Line")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
