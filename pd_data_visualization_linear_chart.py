import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('electronics_annual_sales.csv')
plt.plot(df['Year'], df['TV'], color='black', label='TV')
plt.plot(df['Year'], df['Refrigerator'], color='red', label='Refrigerator')
plt.plot(df['Year'], df['WashingMachine'], color='blue' , label='WashingMachine')
plt.plot(df['Year'], df['AirConditioner'], color='green', label='AirConditioner')
plt.plot(df['Year'], df['Microwave'], color='yellow', label='Microwave')
plt.title('Electronics Annual Sales by Year')
plt.xlabel('Sale Year')
plt.ylabel('Product Revenue')
plt.legend()
plt.show()






