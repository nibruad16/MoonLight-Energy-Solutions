import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data_benin = pd.read_csv('/content/drive/MyDrive/Week 0/Data Sets/data/benin-malanville.csv')
data_sierraleones = pd.read_csv('/content/drive/MyDrive/Week 0/Data Sets/data/sierraleone-bumbuna.csv')
data_togo = pd.read_csv('/content/drive/MyDrive/Week 0/Data Sets/data/togo-dapaong_qc.csv')

# Ensure the 'date' column is parsed as datetime (if it exists in your data)
data_benin['date'] = pd.to_datetime(data_benin['date'])
data_sierraleones['date'] = pd.to_datetime(data_sierraleones['date'])
data_togo['date'] = pd.to_datetime(data_togo['date'])

# Line plot for each dataset
plt.figure(figsize=(14, 7))

sns.lineplot(x='date', y='value', data=data_benin, label='Benin')
sns.lineplot(x='date', y='value', data=data_sierraleones, label='Sierra Leone')
sns.lineplot(x='date', y='value', data=data_togo, label='Togo')

plt.title('Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()
