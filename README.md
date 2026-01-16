
# Restaurant Sales Analysis Project 🍽️

## Project Overview
This project analyzes the sales and customer feedback data of a restaurant. Using Python, Pandas, and Seaborn, it provides insights into customer spending habits, favorite dishes, feedback scores, and overall restaurant performance.

The analysis helps the restaurant understand customer preferences, improve services, and make data-driven decisions.

---

## Dataset
- **File:** `dataset.csv`  
- **Number of Entries:** 1000  
- **Columns:**
  - `USER ID` – Unique identifier for each customer
  - `AMOUNT SPENT ON THAT DAY(20/10/2024)` – Amount spent by the customer
  - `Payment Method` – Mode of payment
  - `Feedback Score (1-5)` – Customer rating (1=poor, 5=excellent)
  - `Favorite Dish` – Customer's favorite dish
  - `Visit Frequency` – How often the customer visits
  - `DATE` – Date of the transaction

---

## Project Features
1. **Data Cleaning & Exploration**
   - Checked for missing values
   - Filled missing amounts with median
   - Dropped rows with missing feedback or favorite dish

2. **Visualizations**
   - Count of orders per favorite dish
   - Average feedback score per dish
   - Scatter plot: Amount spent vs Feedback score
   - Top 10 users by feedback score
   - Correlation heatmap of numeric features

3. **Insights**
   - Total number of orders
   - Number of different dishes ordered
   - Users with highest & lowest feedback scores
   - Average amount spent and average feedback score

---

## Libraries Used
- `pandas` – Data manipulation
- `matplotlib` – Basic plotting
- `seaborn` – Advanced visualizations

---

## How to Run
1. Clone the repository:
```bash
git clone https://github.com/YourUsername/Restaurant_Sales_Analysis.git
