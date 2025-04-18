import numpy as np
import matplotlib.pyplot as plt

# Sample sizes to use
sample_sizes = [500, 1000, 2000]

for n in sample_sizes:
    # Simulate throwing of two dice n times
    s = np.random.randint(1, 7, size=(n, 2)).sum(axis=1)

    # Compute histogram
    h, h2 = np.histogram(s, bins=range(2, 14))

    # Plot line graph
    plt.plot(h2[:-1], h / n, marker='o', linestyle='-', color='deepskyblue')
    plt.xlabel('Sum of two dice')
    plt.ylabel('Frequency')
    plt.title(f'Line graph of sums of two dice for n={n}')
    plt.xticks(range(2, 13))  # Ensure all x-axis ticks are visible
    plt.grid(True)  # Add grid for better readability
    plt.show()
