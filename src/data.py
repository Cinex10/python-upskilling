"""
This module contains the data classes for the cash register.
"""

from dataclasses import dataclass
from decimal import Decimal
from typing import List


@dataclass
class LineItem:
    """
    A line item in a receipt.
    """

    sku: str
    unit_price: Decimal
    qty: int

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LineItem):
            return False
        return (
            self.sku == other.sku
            and self.unit_price == other.unit_price
            and self.qty == other.qty
        )


@dataclass
class Receipt:
    """
    A receipt for a purchase.
    """

    lignes: List[LineItem]
    total_brut: Decimal
    discount_pct: Decimal
    total_due: Decimal
