
import matplotlib.pyplot as plt

# Data points for the Ages of 200 individuals
ages = [
    22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 23, 25, 27, 29,
    31, 33, 35, 37, 39, 41, 43, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 23,
    25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 44, 22, 24, 26, 28, 30, 32, 34, 36,
    38, 40, 42, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 23, 25, 27, 29, 31,
    33, 35, 37, 39, 41, 43, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 24, 26,
    28, 30, 32, 34, 36, 38, 40, 42, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43,
    44
]

plt.figure(figsize=(12, 6))
plt.hist(ages, bins=range(20, 46, 2), color='#FF5733', rwidth=0.7)
plt.title('Age Distribution in a Sample Group')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()