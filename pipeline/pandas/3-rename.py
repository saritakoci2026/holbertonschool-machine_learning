#!/usr/bin/env python3
"""Rename and convert the Timestamp column in a DataFrame."""

import pandas as pd


def rename(df):
    """Rename Timestamp and keep Datetime and Close columns."""
    df = df.rename(columns={"Timestamp": "Datetime"})
    df["Datetime"] = pd.to_datetime(df["Datetime"], unit="s")
    return df[["Datetime", "Close"]]
