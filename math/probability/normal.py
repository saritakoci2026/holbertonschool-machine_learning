#!/usr/bin/env python3
"""Normal distribution."""


class Normal:
    """Represent a normal distribution."""

    def __init__(self, data=None, mean=0., stddev=1.):
        """Initialize a normal distribution."""
        if data is None:
            self.mean = float(mean)
            self.stddev = float(stddev)

            if self.stddev <= 0:
                raise ValueError("stddev must be a positive value")
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")

            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            self.mean = float(sum(data) / len(data))

            variance = sum(
                (x - self.mean) ** 2 for x in data
            ) / len(data)

            self.stddev = float(variance ** 0.5)

    def pdf(self, x):
        """Calculate the PDF at a given x-value."""
        pi = 3.1415926536
        e = 2.7182818285

        exponent = -0.5 * ((x - self.mean) / self.stddev) ** 2

        return (e ** exponent) / (
            self.stddev * (2 * pi) ** 0.5
        )
