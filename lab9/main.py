
from IPython.display import display
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read data from csv data
data = pd.read_csv('russia_losses_personnel.csv', sep=',');

#Convert each Nan value to 0
data = data.fillna(0)

#deleting 'personnel*' and 'POW columns';
data = data.drop('personnel*', axis=1).drop('POW', axis=1)

# display(data)

# tranforming series into list
personnel_list= data["personnel"].tolist()
new_list = []
statistics_per_each_day = []
for index, persons in enumerate(personnel_list):
    if(index == 0): new_list.append(personnel_list[index])
    if(index+1 < len(personnel_list) ):
        new_list.append(personnel_list[index+1] - personnel_list[index])
    else:
        new_list.append(personnel_list[index]-personnel_list[index-1])


#Concating DataFrame with Series
personnel_series = pd.Series(new_list, name='personnel_per_day')
data = data.drop("personnel", axis=1)
data = pd.concat([data, personnel_series], axis=1)
data = data.drop(data.index[-1])
data["day"] = data["day"].astype(int)
display(data)




data['date'] = pd.to_datetime(data['date'])

# Додавання стовпця з роком та місяцем
data['Year'] = data['date'].dt.year
data['Month'] = data['date'].dt.month

# Агрегація за місяць та сумування кількості товарів
aggregated_df = data.groupby(['Year', 'Month'])['personnel_per_day'].sum().reset_index()

# Виведення результату
print(aggregated_df)

# Perform linear regression using numpy
coefficients = np.polyfit(aggregated_df.index, aggregated_df['personnel_per_day'], 1)
polynomial = np.poly1d(coefficients)

# Create a trend line DataFrame
trend_line = pd.DataFrame({'Month': aggregated_df.index, 'TrendLine': polynomial(aggregated_df.index)})

# Plot the original data points and the trend line
plt.scatter(aggregated_df.index, aggregated_df['personnel_per_day'], label='Personnel per Day')
plt.plot(trend_line['Month'], trend_line['TrendLine'], color='red', label='Trend Line')
plt.xlabel('Month')
plt.ylabel('Personnel per Day')
plt.title('Trend Line of russian looses for each month')
plt.legend()
plt.show()







# # Perform linear regression using numpy
# coefficients = np.polyfit(aggregated_df['Month'], aggregated_df['personnel_per_day'], 1)
# polynomial = np.poly1d(coefficients)

# # Create a trend line DataFrame
# trend_line = pd.DataFrame({'Month': aggregated_df['Month'], 'TrendLine': polynomial(aggregated_df['Month'])})

# # Plot the original data points and the trend line
# plt.scatter(aggregated_df['Month'], aggregated_df['personnel_per_day'], label='Data Points')
# plt.plot(trend_line['Month'], trend_line['TrendLine'], color='red', label='Trend Line')
# plt.xlabel('Month')
# plt.ylabel('Count')
# plt.legend()
# plt.show()




