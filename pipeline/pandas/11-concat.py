#!/usr/bin/env python3
"""Concatenate selected rows from two cryptocurrency DataFrames."""

import pandas as pd

index = __import__('10-index').index


def concat(df1, df2):
    """Concatenate selected bitstamp rows above coinbase rows."""
    df1 = index(df1)
    df2 = index(df2)

    df2 = df2[df2.index <= 1417411920]

    return pd.concat([df2, df1], keys=['bitstamp', 'coinbase'])
