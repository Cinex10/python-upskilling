from decimal import Decimal

from exceptions import NegativePriceError
class CashRegister:
    def __init__(self) -> None:
        self.items = {}
    
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

        existing_stock = self.items.get(sku, {}) # get the existing stock for the item
        existing_qty = existing_stock.get(price, 0) # we have supposed that a single sku can have multiple variations each with a different price
        existing_stock[price] = existing_qty + qty # add the new quantity to the existing quantity
        self.items[sku] = existing_stock # update the stock for the item
    
    
    def total(self) -> Decimal:
        """
        Calculate the total price of all items in the cash register.
        Returns:
            The total price of all items.
        """
        total = Decimal(0)
        for sku, stock in self.items.items():
            total += Decimal(sum(price * qty for price, qty in stock.items()))
        return total
    
    
    def reset(self) -> None:
        """
        Reset the cash register.
        Returns:
            None
        """
        self.items.clear()