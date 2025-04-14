import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial
from scipy.special import comb
from PIL import Image

# Parameters
r_values = list(range(1, 25, 1))  # Increasing r values to observe convergence
x = np.linspace(0, max(r_values), 1000)  # Adjust range of x values based on max r

# List to store image filenames
filenames = []


def irwin_hall_pdf(x, r):
    """Compute the PDF of the sum of r independent Uniform(0,1) variables (Irwin-Hall distribution)."""
    pdf = np.zeros_like(x)

    if r == 1:
        # Uniform(0,1) PDF is simply 1 in [0,1], and 0 elsewhere
        pdf = np.where((x >= 0) & (x <= 1), 1, 0)
    else:
        for k in range(r + 1):
            pdf += (-1) ** k * comb(r, k) * np.maximum(0, x - k) ** (r - 1)
        pdf *= (1 / factorial(r - 1))

    return pdf


for r in r_values:
    # Compute the PDF of the sum of r i.i.d. uniform(0,1) distributions
    uniform_sum_pdf = irwin_hall_pdf(x, r)

    # Plot the distribution
    plt.figure(figsize=(6, 4))
    plt.plot(x, uniform_sum_pdf, label=f"Sum of {r} Uniform(0,1)", color='b')
    plt.xlabel("x")
    plt.ylabel("Density")
    plt.title(f"Sum of {r} Uniform Distributions")
    plt.legend()

    # Save image for GIF
    filename = f"uniform_r{r}.png"
    plt.savefig(filename)
    filenames.append(filename)
    plt.close()

# Read images and create GIF
gif_filename = "uniform_to_gaussian.gif"

# Use PIL to create GIF
frames = [Image.open(f) for f in filenames]
frames[0].save(gif_filename, save_all=True, append_images=frames[1:], duration=500, loop=0)

print(f"GIF saved as {gif_filename}")