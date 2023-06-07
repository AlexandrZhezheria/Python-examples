# Напиши функцію discover_original_price яка приймає discounted_price та sale_percentage,
# і повертає оригінальну ціну продукту, тип значення, що повертається повинен бути типом float
# а число має бути округлено до двох знаків після коми.
# Приклади:

Discover_original_price(75.00, 25.00) # повертає 100.00
Discover_original_price(2.00, 50.00) # повертає 4.00
Discover_original_price(55.00, 21.30) # повертає 69.89
Discover_original_price(458.20, 17.13) # повертає 552.91

def discover_original_price(
    discounted_price: float, sale_percentage: float
) -> float:
    original_price = discounted_price / (1 - sale_percentage / 100)
    return round(original_price, 2)
