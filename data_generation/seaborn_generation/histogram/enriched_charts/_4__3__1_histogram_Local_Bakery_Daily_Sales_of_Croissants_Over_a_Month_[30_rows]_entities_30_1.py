
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
expense_data = {'Monthly_Expenses': [320, 450, 510, 550, 600, 620, 640, 680, 720, 750, 
                                     780, 800, 850, 870, 900, 920, 940, 960, 980, 1000,
                                     1020, 1050, 1070, 1100, 1120, 1150, 1170, 1200, 1220, 
                                     1250, 1280, 1300, 1320, 1350, 1370, 1400, 1430, 1450, 
                                     1480, 1500, 1530, 1550, 1580, 1600, 1630, 1650, 1680, 
                                     1700, 1730, 1750, 1780, 1800, 1830, 1850, 1880, 1900, 
                                     1930, 1950, 1980, 2000, 2030, 2050, 2080, 2100, 2130, 
                                     2150, 2180, 2200, 2230, 2250, 2280, 2300, 2330, 2350, 
                                     2380, 2400, 2430, 2450, 2480, 2500, 2530, 2550, 2580, 
                                     2600, 2630, 2650, 2680, 2700, 2730, 2750, 2780, 2800, 
                                     2830, 2850, 2880, 2900, 2930, 2950, 2980, 3000]}
df = pd.DataFrame(expense_data)

# Set size of the figure
plt.figure(figsize=(10, 14))

# Plotting the histogram
sns.histplot(data=df, x='Monthly_Expenses', binwidth=300, color='#3498DB', edgecolor='#1F618D')

# Additional customizations
plt.title('Monthly Expenses Distribution', fontsize=16, loc='left')
plt.xlabel('Monthly Expenses', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.grid(True)

# Show the plot
plt.show()