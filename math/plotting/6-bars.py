#!/usr/bin/env python3
"""Module for plotting a stacked bar graph of fruit per person."""

import numpy as np
import matplotlib.pyplot as plt


def bars():
    """Plot a stacked bar graph of fruit per person."""
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))
    plt.figure(figsize=(6.4, 4.8))

    # your code here
    persons = ['Farrah', 'Fred', 'Felicia']
    apples = fruit[0]
    bananas = fruit[1]
    oranges = fruit[2]
    peaches = fruit[3]

    plt.bar(persons, apples, width=0.5, color='red', label='apples')
    plt.bar(persons, bananas, width=0.5, color='yellow',
            bottom=apples, label='bananas')
    plt.bar(persons, oranges, width=0.5, color='#ff8000',
            bottom=apples + bananas, label='oranges')
    plt.bar(persons, peaches, width=0.5, color='#ffe5b4',
            bottom=apples + bananas + oranges, label='peaches')

    plt.ylabel('Quantity of Fruit')
    plt.title('Number of Fruit per Person')
    plt.yticks(range(0, 81, 10))
    plt.ylim(0, 80)
    plt.legend()

    plt.show()
