
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
revenue = [15000, 18000, 17000, 22000, 21000, 25000, 24000, 26000, 23000, 20000, 21000, 22000]

# Colors for each bar
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#955251', '#B565A7', '#009B77', '#DD4124', '#45B8AC', '#EFC050', '#5B5EA6']

# Create a vertical bar chart
plt.figure(figsize=(12, 7))
plt.bar(months, revenue, color=colors, width=0.5)

# Modify the ticks, labels, and title
plt.ylabel('Revenue ($)')
plt.title('Monthly Revenue for the Year', pad=20)
plt.ylim(10000, 30000)

# Display the plot
plt.show()