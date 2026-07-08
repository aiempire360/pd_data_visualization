import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('electronics_annual_sales.csv')
plt.hist(df['Microwave'])
plt.show()