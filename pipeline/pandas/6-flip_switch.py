#!/usr/bin/env python3
"""Sort a DataFrame in reverse chronological order and transpose it."""


def flip_switch(df):
    """Sort the DataFrame in reverse order and transpose it."""
    return df.sort_index(ascending=False).T
