"""
This module contains the CashRegister class.
"""

from decimal import Decimal

from .data import LineItem, Receipt
from .exceptions import DiscountError, NegativePriceError


class CashRegister:
    """
    A cash register that can scan items and calculate the total price.
    """

    def __init__(self) -> None:
        self.items = {}
        self.discount = 0

    def scan_item(self, sku: str, price: Decimal, qty: int = 1):
        """
        Scan an item and add it to the cash register.
        Args:
            sku: The stock keeping unit of the item.
            price: The price of the item.
            qty: The quantity of the item.
        Raises:
            NegativePriceError: If the price is negative.
        Returns:
            None
        """
        if price <= 0:
            raise NegativePriceError()

        # get the existing stock for the item
        existing_stock = self.items.get(sku, {})
        # we have supposed that a single sku can have multiple
        # variations each with a different price
        existing_qty = existing_stock.get(price, 0)
        existing_stock[price] = (
            existing_qty + qty
        )  # add the new quantity to the existing quantity
        self.items[sku] = existing_stock  # update the stock for the item

    def total(self) -> Decimal:
        """
        Calculate the total price of all items in the cash register.
        Returns:
            The total price of all items.
        """

        total = Decimal("0")
        for _, stock in self.items.items():
            total += sum(
                Decimal(str(price * qty)) for price, qty in stock.items()
            )
        return total

    def reset(self) -> None:
        """
        Reset the cash register.
        Returns:
            None
        """
        self.items.clear()

    def apply_discount(self, percent: Decimal):
        """
        Apply a discount to the total price.
        Args:
            percent: The percentage of the discount.
        Raises:
            DiscountError: If the discount is not in 0 - 100 range.
        Returns:
            None
        """
        if percent < 0 or percent > 100:
            raise DiscountError()

        self.discount = percent

    def get_discount(self) -> Decimal:
        """
        Get the discount percentage.
        Returns:
            The discount percentage.
        """
        if self.discount == 100:
            return Decimal("0")

        total = self.total()
        discount = Decimal(str(self.discount / 100))
        return total * discount

    def remove_discount(self):
        """
        Remove the discount from the total price.
        Returns:
            None
        """
        self.discount = 0

    def to_receipt(self) -> Receipt:
        """
        Convert the cash register to a receipt.
        Returns:
            A receipt object.
        """
        lignes = []
        for sku, stock in self.items.items():
            for price, qty in stock.items():
                lignes.append(LineItem(sku, price, qty))
        return Receipt(
            lignes=lignes,
            total_brut=self.total(),
            discount_pct=self.discount,
            total_due=self.total() - self.get_discount(),
        )
