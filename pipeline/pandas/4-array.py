#!/usr/bin/env python3
"""Convert the last ten rows of selected DataFrame columns to an array."""


def array(df):
    """Return the last ten rows of High and Close as a NumPy array."""
    return df[["High", "Close"]].tail(10).to_numpy()
