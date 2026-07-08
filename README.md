# 📊 Electronics Annual Sales Data Visualization with Pandas, Matplotlib & Seaborn

## 📌 Project Overview

This project demonstrates how to visualize annual electronics sales data using **Pandas**, **Matplotlib**, and **Seaborn** in Python.

The dataset contains **10 years of sales data** for five electronic products:

* 📺 TV
* ❄️ Refrigerator
* 🧺 Washing Machine
* ❄️ Air Conditioner
* 🔥 Microwave

Different types of charts are used to analyze sales trends, compare products, and understand data distribution.

---

# 🚀 Technologies Used

* Python 3
* Pandas
* Matplotlib
* Seaborn

Install the required libraries:

```bash
pip install pandas matplotlib seaborn
```

---

# 📂 Dataset

**File Name**

```
electronics_annual_sales.csv
```

### Dataset Columns

| Column         | Description                  |
| -------------- | ---------------------------- |
| Year           | Sales Year                   |
| TV             | Annual TV Sales              |
| Refrigerator   | Annual Refrigerator Sales    |
| WashingMachine | Annual Washing Machine Sales |
| AirConditioner | Annual Air Conditioner Sales |
| Microwave      | Annual Microwave Sales       |

---

# 📈 Visualizations Included

## 1️⃣ Bar Chart

Displays annual sales comparison for all products.

```python
df.plot(kind="bar", x="Year")
```

---

## 2️⃣ Line Chart

Shows yearly sales trends of every product.

Features:

* Multiple product comparison
* Custom colors
* Axis labels
* Title
* Legend

---

## 3️⃣ Histogram (Matplotlib)

Displays the distribution of Microwave sales.

```python
plt.hist(df["Microwave"])
```

---

## 4️⃣ Histogram (Seaborn)

Uses Seaborn's histogram for a cleaner visualization.

```python
sns.histplot(data=df, x="Microwave")
```

---

## 5️⃣ Scatter Plot

Shows the relationship between:

* Microwave Sales
* Year

```python
sns.scatterplot(data=df, x="Microwave", y="Year")
```

---

## 6️⃣ Pie Chart

Displays the percentage contribution of each product to total sales.

The chart includes:

* Product labels
* Percentage values
* Exploded slices

```python
plt.pie(...)
```

---

# 📊 Libraries Used

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

---

# ▶️ Run the Project

Clone the repository:

```bash
git clone https://github.com/your-username/your-repository.git
```

Open the project folder:

```bash
cd your-repository
```

Run any visualization script:

```bash
python filename.py
```

---

# 📚 Concepts Practiced

* Reading CSV files
* DataFrames
* Data Visualization
* Bar Charts
* Line Charts
* Histograms
* Scatter Plots
* Pie Charts
* Legends
* Axis Labels
* Chart Titles
* Data Analysis using Pandas
* Data Visualization using Matplotlib
* Data Visualization using Seaborn

---

# 🎯 Learning Objectives

After completing this project, you will understand how to:

* Load datasets using Pandas
* Create different chart types
* Compare yearly sales data
* Visualize trends over time
* Analyze sales distributions
* Display product-wise sales percentages
* Build attractive charts using Matplotlib and Seaborn

---

# 📄 License

This project is created for educational and learning purposes.
