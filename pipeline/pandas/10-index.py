#!/usr/bin/env python3
"""Set the Timestamp column as the index of a DataFrame."""


def index(df):
    """Set Timestamp as the DataFrame index and return the DataFrame."""
    return df.set_index('Timestamp')
