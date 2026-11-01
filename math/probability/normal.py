#!/usr/bin/env python3
"""
Normal distribution class.
"""


class Normal:
    """
    Represents a normal distribution.
    """

    def __init__(self, data=None, mean=None, stddev=None):
        """
        Initializes a Normal distribution.
        """
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = float(sum(data) / len(data))
            variance = sum((x - self.mean) ** 2 for x in data) / len(data)
            self.stddev = float(variance ** 0.5)
        else:
            if mean is None:
                raise ValueError("mean is required if data is not provided")
            if stddev is None:
                raise ValueError("stddev is required if data is not provided")
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)

    def z_score(self, x):
        """
        Calculates the z-score of a given x-value.
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """
        Calculates the x-value of a given z-score.
        """
        return self.mean + z * self.stddev

    def pdf(self, x):
        """
        Calculates the PDF for a given x-value.
        """
        pi = 3.1415926536
        e = 2.7182818285
        return (1 / (self.stddev * (2 * pi) ** 0.5)) * \
            e ** (-0.5 * ((x - self.mean) / self.stddev) ** 2)

    def cdf(self, x):
        """
        Calculates the CDF for a given x-value.

        Args:
            x (float): The x-value.

        Returns:
            float: The CDF value for x.
        """
        return 0.5 * (1 + self._erf(
            (x - self.mean) / (self.stddev * 2 ** 0.5)))

    def _erf(self, x):
        """
        Approximates the error function erf(x) using Taylor series.

        Args:
            x (float): The input value.

        Returns:
            float: Approximation of erf(x).
        """
        pi = 3.1415926536
        result = x - (x ** 3) / 3 + (x ** 5) / 10 - (x ** 7) / 42 \
            + (x ** 9) / 216
        return (2 / (pi ** 0.5)) * result
