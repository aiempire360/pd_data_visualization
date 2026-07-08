import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("electronics_annual_sales.csv")

# Scatterplot
sns.scatterplot(data=df, x='Microwave', y= 'Year')
plt.show()