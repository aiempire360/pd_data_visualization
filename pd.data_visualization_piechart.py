import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('electronics_annual_sales.csv')

sales_Total = df[['TV','Refrigerator','WashingMachine','AirConditioner','Microwave', ]].sum ()

plt.pie(sales_Total, labels = sales_Total.index, autopct ="%1.2f%%",explode = (0.1,0.1,0.1,0.1,0.1))
plt.show()