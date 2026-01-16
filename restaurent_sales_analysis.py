# ===========================================
# RESTAURANT SALES ANALYSIS PROJECT - FULL CODE
# ===========================================

# Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Improve plot style
sns.set(style='whitegrid', palette='muted', font_scale=1.1)

# Step 2: Load CSV
df = pd.read_csv('dataset.csv')  # <-- full path

# Step 3: Explore Data
print("----- HEAD -----")
print(df.head())

print("\n----- INFO -----")
print(df.info())

print("\n----- DESCRIBE -----")
print(df.describe())

print("\n----- Check Missing Values -----")
print(df.isnull().sum())

# Step 4: Data Cleaning
# Drop rows with missing Feedback Score or Favorite Dish
df = df.dropna(subset=['Feedback Score (1-5)', 'Favorite Dish'])

# Fill missing Amount Spent with median (if any)
df['AMOUNT SPENT ON THAT DAY(20/10/2024)'] = df['AMOUNT SPENT ON THAT DAY(20/10/2024)'].fillna(
    df['AMOUNT SPENT ON THAT DAY(20/10/2024)'].median()
)

# ===============================
# Step 5: Graphs & Visualizations
# ===============================

# 5.1 Count of Favorite Dishes
plt.figure(figsize=(10,5))
sns.countplot(data=df, x='Favorite Dish', order=df['Favorite Dish'].value_counts().index)
plt.xticks(rotation=45)
plt.title('Number of Orders per Favorite Dish')
plt.show()

# 5.2 Average Feedback Score per Favorite Dish
plt.figure(figsize=(10,5))
sns.barplot(
    data=df, 
    x='Favorite Dish', 
    y='Feedback Score (1-5)',
    order=df.groupby('Favorite Dish')['Feedback Score (1-5)'].mean().sort_values(ascending=False).index
)
plt.xticks(rotation=45)
plt.title('Average Feedback Score per Favorite Dish')
plt.show()

# 5.3 Amount Spent vs Feedback Score Scatter
plt.figure(figsize=(8,5))
sns.scatterplot(
    data=df, 
    x='AMOUNT SPENT ON THAT DAY(20/10/2024)',
    y='Feedback Score (1-5)', 
    hue='Favorite Dish', 
    alpha=0.7
)
plt.title('Amount Spent vs Feedback Score by Dish')
plt.show()

# 5.4 Top 10 Users by Feedback Score
top_users = df.sort_values(by='Feedback Score (1-5)', ascending=False).head(10)
plt.figure(figsize=(10,5))
sns.barplot(
    data=top_users, 
    x='USER ID', 
    y='Feedback Score (1-5)', 
    hue='Favorite Dish', 
    dodge=False
)
plt.xticks(rotation=45)
plt.title('Top 10 Users by Feedback Score')
plt.show()

# 5.5 Correlation Heatmap (Numeric Columns)
plt.figure(figsize=(8,6))
sns.heatmap(df[['AMOUNT SPENT ON THAT DAY(20/10/2024)', 'Feedback Score (1-5)']].corr(), 
            annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

# ===============================
# Step 6: Insights / Analysis
# ===============================
print("\n----- Insights -----")
print("1. Total Orders:", df.shape[0])
print("2. Different Dishes Ordered:", df['Favorite Dish'].nunique())
print("3. Highest Feedback Score User:", df.loc[df['Feedback Score (1-5)'].idxmax()]['USER ID'])
print("4. Lowest Feedback Score User:", df.loc[df['Feedback Score (1-5)'].idxmin()]['USER ID'])
print("5. Average Amount Spent:", round(df['AMOUNT SPENT ON THAT DAY(20/10/2024)'].mean(),2))
print("6. Average Feedback Score:", round(df['Feedback Score (1-5)'].mean(),2))