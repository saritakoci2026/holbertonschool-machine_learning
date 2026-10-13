#!/usr/bin/env python3
"""Fill missing values in a DataFrame."""


def fill(df):
    """Remove Weighted_Price and fill missing values."""
    df = df.drop(columns=['Weighted_Price'])
    df['Close'] = df['Close'].ffill()

    for column in ['High', 'Low', 'Open']:
        df[column] = df[column].fillna(df['Close'])

    df[['Volume_(BTC)', 'Volume_(Currency)']] = (
        df[['Volume_(BTC)', 'Volume_(Currency)']].fillna(0)
    )

    return df
