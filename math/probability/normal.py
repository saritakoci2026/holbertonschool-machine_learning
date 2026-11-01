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

    def z_score(self, x):
        """Calculate the z-score of a given x-value."""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculate the x-value of a given z-score."""
        return z * self.stddev + self.mean

    def cdf(self, x):
        """Calculate the CDF at a given x-value."""
        pi = 3.1415926536

        z = (x - self.mean) / (self.stddev * 2 ** 0.5)

        term = z
        total = term

        for n in range(1, 100):
            term *= -(z ** 2) / n
            total += term / (2 * n + 1)

        erf = (2 / (pi ** 0.5)) * total

        return 0.5 * (1 + erf)
