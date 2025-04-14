import numpy as np
import matplotlib.pyplot as plt
import imageio.v3 as iio  # Use imageio v3 for better compatibility
from PIL import Image

# Parameters
lambda_ = 0.5  # Rate parameter
r_values = list(range(1, 25, 1))  # Increasing r values to observe convergence
x = np.linspace(0, 80, 1000)  # Range of x values

# List to store image filenames
filenames = []

for r in r_values:
    # Compute Erlang PDF
    erlang_pdf = (lambda_ ** r * x ** (r - 1) * np.exp(-lambda_ * x)) / np.math.factorial(r - 1)

    # Plot the distribution
    plt.figure(figsize=(6, 4))
    plt.plot(x, erlang_pdf, label=f"Erlang (r={r}, λ={lambda_})", color='b')
    plt.xlabel("x")
    plt.ylabel("Density")
    plt.title(f"Erlang Distribution (r={r})")
    plt.legend()

    # Save image for GIF
    filename = f"erlang_r{r}.png"
    plt.savefig(filename)
    filenames.append(filename)
    plt.close()

# Read images and create GIF
gif_filename = "erlang_to_gaussian.gif"

# Alternative method to ensure compatibility
frames = [Image.open(f) for f in filenames]  # Use PIL to read images
frames[0].save(gif_filename, save_all=True, append_images=frames[1:], duration=500, loop=0)

print(f"GIF saved as {gif_filename}")