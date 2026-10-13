#!/usr/bin/env python3
"""Slice selected columns of a DataFrame."""


def slice(df):
    """Return every 60th row of the selected columns."""
    columns = ["High", "Low", "Close", "Volume_(BTC)"]
    return df[columns].iloc[::60]
