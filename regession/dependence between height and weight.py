import matplotlib.pyplot as plt

heights = [160, 165, 170, 175, 180, 185, 190]  # in cm
weights = [55, 60, 68, 72, 80, 85, 90]        # in kg

# Scatter plot
plt.scatter(heights, weights, color='blue', alpha=0.7)
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.title('Height vs Weight Scatter Plot')
plt.grid(True)
plt.show()
