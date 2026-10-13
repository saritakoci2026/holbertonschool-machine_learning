#!/usr/bin/env python3
"""Remove rows with missing Close values."""


def prune(df):
    """Remove rows where Close contains NaN values."""
    return df.dropna(subset=['Close'])
