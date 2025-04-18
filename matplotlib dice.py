import numpy as np
import matplotlib.pyplot as plt

# Sample sizes to use
sample_sizes = [500, 1000, 2000]

for n in sample_sizes:
    # Simulate throwing of two dice n times
    s = np.random.randint(1, 7, size=(n, 2)).sum(axis=1)

    # Compute histogram
    h, h2 = np.histogram(s, bins=range(2, 14))

    # Plot histogram
    plt.bar(h2[:-1], h / n, color='deepskyblue')
    plt.xlabel('Sum of two dice')
    plt.ylabel('Frequency')
    plt.title(f'Histogram of sums of two dice for n={n}')
    plt.show()
