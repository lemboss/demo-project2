from enum import Enum

class WBCapitalizationEnum(str, Enum):
    in_warehouse: str = 'Всего находится на складах'
    to_client: str = "В пути до получателей"
    from_client: str = 'В пути возвраты на склад WB'