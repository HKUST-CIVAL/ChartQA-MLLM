
import matplotlib.pyplot as plt

# Data
countries = [
    "China", "USA", "Germany", "India", "Japan", 
    "Brazil", "UK", "France", "Canada", "Italy", 
    "Spain", "Australia", "South Korea", "Mexico", "Russia",
    "Norway", "Sweden", "Finland", "Denmark", "Netherlands",
    "Belgium", "Switzerland", "Austria", "Portugal"
]
renewable_capacity = [850, 320, 160, 110, 85, 80, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 18, 16, 14, 12, 10, 8, 6, 4]

# Colors for each country
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FF8F33',
    '#8D33FF', '#33FFBD', '#FF3387', '#33FFF3', '#FF8F33',
    '#5733FF', '#33A6FF', '#8F33FF', '#57FF33', '#FF3357',
    '#FFB533', '#33FFB5', '#B533FF', '#33B5FF', '#FF5733',
    '#33FF57', '#3357FF', '#FF33A6', '#FF8F33'
]

# Plot
fig, ax = plt.subplots(figsize=(14, 10))
bars = ax.bar(countries, renewable_capacity, color=colors, width=0.6)

# Set the title and labels
ax.set_title('Top Countries by Renewable Energy Capacity (GW)', fontsize=16, pad=20)
ax.set_ylabel('Renewable Energy Capacity (GW)', fontsize=13)
ax.set_xlabel('Country', fontsize=13)

# Customize the tick labels
plt.xticks(fontsize=11, rotation=45)
plt.yticks(fontsize=11)

# Add the data values on the bars
for bar in bars:
    height = bar.get_height()
    label_y_pos = height + 10
    ax.text(bar.get_x() + bar.get_width()/2, label_y_pos, f'{height} GW', ha='center')

# Show the plot
plt.tight_layout()
plt.show()