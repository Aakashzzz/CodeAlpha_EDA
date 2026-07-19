import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Program Started")

# Read Dataset
df = pd.read_csv("dataset.csv")

# First 5 Rows
print(df.head())

# Dataset Info
print(df.info())

# Shape
print(df.shape)

# Column Names
print(df.columns)

# Statistics
print(df.describe())

# Missing Values
print(df.isnull().sum())

# Duplicate Rows
print(df.duplicated().sum())

# Histogram
df.hist(figsize=(8,5))
plt.show()

# Correlation Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
plt.show()
plt.figure(figsize=(6,4))
plt.scatter(df["Age"], df["Salary"])

plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")

plt.show()
plt.figure(figsize=(6,4))
sns.boxplot(data=df[["Age", "Salary"]])
plt.title("Box Plot")
plt.show()