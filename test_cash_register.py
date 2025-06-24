import pytest
from decimal import Decimal
from cash_register import CashRegister
from exceptions import NegativePriceError

def test_accumulated_total():
    cash_register = CashRegister()
    cash_register.scan_item("123", 10.00, 3)
    cash_register.scan_item("123", 10.00 , 4)
    cash_register.scan_item("123", 15.00 , 2)
    cash_register.scan_item("456", 24.00 , 10)
    
    total = cash_register.total()
    
    assert total == Decimal("340.00")
    
    
def test_reset():
    cash_register = CashRegister()
    cash_register.scan_item("123", 10.00, 3)
    cash_register.scan_item("123", 10.00 , 4)
    cash_register.scan_item("123", 15.00 , 2)
    cash_register.scan_item("456", 24.00 , 10)
    
    cash_register.reset()
    
    assert cash_register.items == {}

def test_negative_price():
    cash_register = CashRegister()
    with pytest.raises(NegativePriceError):
        cash_register.scan_item("123", -10.00, 3)