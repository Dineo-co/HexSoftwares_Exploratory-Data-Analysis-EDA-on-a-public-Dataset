# Import necessary libraries
import pandas as pd
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the datasetdir
df = pd.read_csv("c:/Users/Dineo/Desktop/Dataset/hello.py/yes.py")
# Display the first 5 rows
print(df.head())

# 1. Data Cleaning
print("\nMissing Values:\n", df.isnull().sum())  # Check for missing values
df_cleaned = df.dropna()  # Drop rows with missing values

# 2. Basic Statistical Analysis
print("\nBasic Statistics:\n", df_cleaned.describe())  # Summary statistics

# 3. Visualize Distributions
plt.figure(figsize=(10, 6))
sns.histplot(df_cleaned.select_dtypes(include='number').iloc[:, 0], kde=True)  # First numeric column
plt.title('Distribution of First Numeric Column')
plt.show()

# 4. Correlation Matrix
plt.figure(figsize=(10, 8))
corr_matrix = df_cleaned.corr()  # Compute correlations
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

# 5. Scatter Plot (Replace 'column_x' and 'column_y' with actual column names)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='column_x', y='column_y', data=df_cleaned)  # Update column names
plt.title('Scatter Plot')
plt.show()

