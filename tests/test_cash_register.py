"""
This module contains the tests for the cash register.
"""

from decimal import Decimal

import pytest

from src.cash_register import CashRegister
from src.data import LineItem
from src.exceptions import DiscountError, NegativePriceError


def test_accumulated_total():
    """
    Test the accumulated total.
    """
    cash_register = CashRegister()
    cash_register.scan_item("123", 10.00, 3)
    cash_register.scan_item("123", 10.00, 4)
    cash_register.scan_item("123", 15.00, 2)
    cash_register.scan_item("456", 24.00, 10)

    total = cash_register.total()

    assert total == Decimal("340.00")


def test_reset():
    """
    Test the reset method.
    """
    cash_register = CashRegister()
    cash_register.scan_item("123", 10.00, 3)
    cash_register.scan_item("123", 10.00, 4)
    cash_register.scan_item("123", 15.00, 2)
    cash_register.scan_item("456", 24.00, 10)

    cash_register.reset()

    assert not cash_register.items


def test_negative_price():
    """
    Test the negative price.
    """
    cash_register = CashRegister()
    with pytest.raises(NegativePriceError):
        cash_register.scan_item("123", -10.00, 3)


def test_discount():
    """
    Test the discount.
    """
    cash_register = CashRegister()
    cash_register.scan_item("123", 10.00, 3)
    cash_register.scan_item("123", 10.00, 4)
    cash_register.scan_item("123", 15.00, 2)
    cash_register.scan_item("456", 20.00, 10)

    cash_register.apply_discount(10)

    discount = cash_register.get_discount()

    assert discount == Decimal("30.00")

    cash_register.remove_discount()

    discount = cash_register.get_discount()

    assert discount == Decimal("0.00")


def test_invalid_discount():
    """
    Test the invalid discount.
    """
    cash_register = CashRegister()
    with pytest.raises(DiscountError):
        cash_register.apply_discount(150)


def test_to_receipt():
    """
    Test the to_receipt method.
    """
    cash_register = CashRegister()
    cash_register.scan_item("123", 20.00, 2)
    cash_register.scan_item("456", 15.00, 4)
    cash_register.scan_item("678", 50.00, 2)

    cash_register.apply_discount(20)

    receipt = cash_register.to_receipt()

    assert receipt.total_brut == Decimal("200.00")
    assert receipt.discount_pct == Decimal("20.00")
    assert receipt.total_due == Decimal("160.00")
    assert (
        LineItem(sku="123", unit_price=Decimal("20.00"), qty=2)
        in receipt.lignes
    )
    assert (
        LineItem(sku="456", unit_price=Decimal("15.00"), qty=4)
        in receipt.lignes
    )
    assert (
        LineItem(sku="678", unit_price=Decimal("50.00"), qty=2)
        in receipt.lignes
    )
    assert len(receipt.lignes) == 3
