# Cash-Register

A simple Python library that models a basic cash register for a shop.


## Setup

### 1. Create Virtual environement
```bash
python -m venv venv
```
### 2. Activate Virtual environement

* On Linux/MacOS

```bash
source venv/bin/activate
```

* On Windows

```bash
venv\Scripts\activate
```

### 2. Install poetry

* On Linux/MacOS

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

* On Windows

```bash
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

* Or directly with `pip`

```bash
pip install poetry
```

### 3. Install cash-register package (with dependencies)

```bash
poetry install
```

## Usage

```python
from cash_register import CashRegister

cash_register = CashRegister()

cash_register.scan_item("123", 10.00, 3) # Add new product with sku="123", price="10.00" and quantity=3
cash_register.scan_item("123", 10.00, 4)
cash_register.scan_item("123", 15.00, 2)
cash_register.scan_item("456", 24.00, 10)

total = cash_register.total() # 340.00

cash_register.apply_discount(10) # Apply a 10% discount to the total price

cash_register.remove_discount() # Remove discount

cash_register.apply_discount(150) # Raise DiscountError : discount must be in 0-100%

cash_register.reset() # Reset the cash register

cash_register.scan_item("123", -10.00, 3) # Raise NegativePriceError exception
```

## Testing

* Testing only

```bash
poetry run test 
```

* Testing with coverage

```bash
poetry run cov 
```

## Linting

* Using pylint

```bash
poetry run pylint src/
```

* Applying code formating using black (PEP 8 compliant)

```bash
poetry run black src/
```

