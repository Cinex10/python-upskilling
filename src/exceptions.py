"""
This module contains the exceptions for the cash register.
"""


class NegativePriceError(Exception):
    """
    Raised when a negative price is provided.
    """


class DiscountError(Exception):
    """
    Raised when a discount is applied that is not in 0 - 100 range.
    """
