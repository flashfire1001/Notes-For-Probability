import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from PIL import Image

# Parameters
r_values = list(range(1, 80, 2))  # Increasing r values to observe convergence

# List to store image filenames
filenames = []

for r in r_values:
    k_values = np.arange(0, r + 1)  # Possible outcomes of Binomial(r, 0.5)
    binomial_pmf = binom.pmf(k_values, r, 0.5)  # Compute PMF

    # Plot the PMF
    plt.figure(figsize=(6, 4))
    plt.stem(k_values, binomial_pmf, basefmt=" ", linefmt='b-', markerfmt='bo')  # Removed use_line_collection
    plt.xlabel("k")
    plt.ylabel("Probability")
    plt.title(f"Binomial PMF (r={r}, p=0.5)")
    plt.ylim(0, max(binomial_pmf) * 1.2)  # Adjust y-axis for better visibility

    # Save image for GIF
    filename = f"binomial_r{r}.png"
    plt.savefig(filename)
    filenames.append(filename)
    plt.close()

# Create GIF
gif_filename = "binomial_to_gaussian.gif"
frames = [Image.open(f) for f in filenames]
frames[0].save(gif_filename, save_all=True, append_images=frames[1:], duration=500, loop=0)

print(f"GIF saved as {gif_filename}")