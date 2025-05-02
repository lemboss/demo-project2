from babel.numbers import format_decimal

def beautify_number(number: int, currency = None) -> str:
    res = format_decimal(number, locale='ru_RU', decimal_quantization=False)
    if currency:
        res += f" {currency}"
    return res