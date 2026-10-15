#!/usr/bin/env python3
"""Module for plotting a histogram of student grades."""

import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """Plot a histogram of student scores for Project A."""
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    # Histogram me bins çdo 10 njësi (0, 10, 20, ..., 100)
    plt.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')

    # Boshti X: nga 0 në 100, me hap 10
    plt.xticks(range(0, 101, 10))

    # Boshti Y: nga 0 në 30, me hap 5
    plt.yticks(range(0, 31, 5))

    # Etiketat dhe titulli
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Project A')

    # Kufijtë e boshteve
    plt.xlim(0, 100)
    plt.ylim(0, 30)

    plt.show()
