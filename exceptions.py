class NegativePriceError(Exception):
    """
    Raised when a negative price is provided.
    """
    pass


class DiscountError(Exception):
    """
    Raised when a discount is applied that is not in 0 - 100 range.
    """
    pass