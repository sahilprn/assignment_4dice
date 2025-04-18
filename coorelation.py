import pandas as pd

# Step 1: Read the CSV file
df = pd.read_csv('weight-height.csv')  # Make sure the path is correct

# Step 2: Select only Height and Weight columns for correlation
numeric_df = df[['Height', 'Weight']]  # Only keep numeric columns

# Step 3: Calculate correlation between Height and Weight
correlation = numeric_df['Height'].corr(numeric_df['Weight'])

# Step 4: Print the correlation value
print(f"Correlation between Height and Weight: {correlation:.2f}")