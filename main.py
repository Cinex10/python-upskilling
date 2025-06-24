from cash_register import CashRegister

def main():
    cash_register = CashRegister()
    cash_register.scan_item("123", 10.00, 3)
    cash_register.scan_item("123", 10.00 , 4)
    cash_register.scan_item("123", 15.00 , 2)
    cash_register.scan_item("456", 24.00 , 10)
    print(cash_register.total())
    cash_register.reset()
    print(cash_register.total())


if __name__ == "__main__":
    main()