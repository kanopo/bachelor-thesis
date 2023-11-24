import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def print_hist(unique, counts, path, title):
    plt.hist(x=unique, weights=counts, bins=np.arange(min(unique), max(unique) + 1, 1))
    # plt.title(title)
    plt.xlabel("Pixel value")
    plt.ylabel("Pixel count")
    plt.savefig(path)
    plt.close()


path = "./"
results = pd.DataFrame(columns=["file", "mean", "std", "unique", "counts"])

for i in os.listdir(path):
    # Check if it's a file and ends with .csv
    if os.path.isfile(os.path.join(path, i)) and i.endswith(".csv"):
        data = pd.read_csv(os.path.join(path, i))

        array = data.values.flatten()  # Flatten in case it's not a 1D array
        mean = array.mean()
        std = array.std()

        unique, counts = np.unique(array, return_counts=True)

        results.loc[len(results)] = [i, mean, std, list(unique), list(counts)]

        # Print histogram
        print_hist(unique, counts, f"hist_{i}.png", title=i)

# After the loop, you can save the DataFrame to a CSV file
results.to_csv("results.csv", index=False)
