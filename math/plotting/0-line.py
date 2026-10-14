#!/usr/bin/env python3
"""Plot a cubic line graph using matplotlib."""
import numpy as np
import matplotlib.pyplot as plt


def line():
    """Plot y = x cubed as a solid red line."""
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))
    plt.plot(y, color='red', linestyle='-')
    plt.xlim(0, 10)
    plt.show()
