#!/usr/bin/env python3
"""Module for plotting multiple plots in one figure."""

import numpy as np
import matplotlib.pyplot as plt


def all_in_one():
    """Plot all tasks in one figure with subplots."""
    # ============================================
    # Të dhënat
    # ============================================
    # 1. Kurbë kubike (0-10)
    x1 = np.linspace(0, 10, 100)
    y1 = x1 ** 3

    # 2. Men's Height vs Weight
    np.random.seed(5)
    height = np.random.normal(68, 5, 1000)
    weight = height * 2.5 + np.random.normal(0, 3, 1000)

    # 3. Exponential Decay C-14
    t_c14 = np.linspace(0, 28650, 1000)
    y_c14 = np.exp(-t_c14 / 8267)

    # 4. Exponential Decay of Radioactive Elements
    t_radio = np.linspace(0, 20000, 1000)
    c14 = np.exp(-t_radio / 8267)
    ra226 = np.exp(-t_radio / 1600)

    # 5. Project A (grades)
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)

    # ============================================
    # Figura me 5 subplot-e
    # ============================================
    fig = plt.figure(figsize=(12, 9))
    fig.suptitle('All in One', fontsize=20)

    # ---------- 1. Lart-majtas: Kurbë kubike ----------
    ax1 = plt.subplot(3, 2, 1)
    ax1.plot(x1, y1, color='red', linewidth=2)
    ax1.set_xlim(0, 10)

    # ---------- 2. Lart-djathtas: Men's Height vs Weight ----------
    ax2 = plt.subplot(3, 2, 2)
    ax2.scatter(height, weight, color='m', alpha=0.6, s=10)
    ax2.set_xlabel('Height (in)')
    ax2.set_ylabel('Weight (lbs)')
    ax2.set_title("Men's Height vs Weight")
    ax2.set_yticks([170, 180, 190])
    ax2.set_xticks([60, 70, 80])

    # ---------- 3. Mes-majtas: Exponential Decay of C-14 ----------
    ax3 = plt.subplot(3, 2, 3)
    ax3.plot(t_c14, y_c14, linewidth=2)
    ax3.set_yscale('log')
    ax3.set_xlabel('Time (years)')
    ax3.set_ylabel('Fraction Remaining')
    ax3.set_title('Exponential Decay of C-14')
    ax3.set_xticks([0, 10000, 20000])

    # ---------- 4. Mes-djathtas: Exponential Decay ----------
    # of Radioactive Elements
    ax4 = plt.subplot(3, 2, 4)
    ax4.plot(t_radio, c14, 'r--', linewidth=2, label='C-14')
    ax4.plot(t_radio, ra226, 'g-', linewidth=2, label='Ra-226')
    ax4.set_xlabel('Time (years)')
    ax4.set_ylabel('Fraction Remaining')
    ax4.set_title('Exponential Decay of Radioactive Elements')
    ax4.legend(loc='upper right')
    # Y-axis: 0, 0.5, 1  ← E REJA
    ax4.set_yticks([0, 0.5, 1])

    # ---------- 5. Poshtë: Project A ----------
    ax5 = plt.subplot(3, 1, 3)
    ax5.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')
    ax5.set_xlabel('Grades')
    ax5.set_ylabel('Number of Students')
    ax5.set_title('Project A')
    ax5.set_xlim(0, 100)
    ax5.set_xticks(range(0, 101, 10))
    ax5.set_yticks(range(0, 31, 5))
    ax5.set_ylim(0, 30)

    # Rregullo layout
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    all_in_one()
