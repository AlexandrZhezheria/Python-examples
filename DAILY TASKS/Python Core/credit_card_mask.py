# Зазвичай під час оплати покупок буває таке, що тобі потрібно ввести номер картки.
# Але оскільки хтось може підгледіти твій номер, давай замаскуємо його.
# Твоя задача - створити функцію credit_card_mask, яка змінюватиме усі символи, окрім останніх чотирьох, на #.
# Приклади:
# python_credit_card_mask("4556364607935616") == "############5616"
# python_credit_card_mask("64607935616") == "#######5616"
# python_credit_card_mask("55556") == "#5556"
# python_credit_card_mask("1") == "1"
# python_credit_card_mask("") == ""


def credit_card_mask(card_number: str) -> str:
    if len(card_number) <= 4:
        # If the card number has 4 digits or less, there's nothing to mask
        return card_number
    else:
        # Mask all characters except the last 4 with "#"
        return "#" * (len(card_number) - 4) + card_number[-4:]
