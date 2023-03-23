# Реалізуй клас Transaction. Його метод __init__ повинен приймати такі параметри:
# amount - суму на яку було здійснено транзакцію
# date - дату переказу
# currency - валюту в якій було зроблено переказ (за замовчуванням USD)
# usd_conversion_rate - курс цієї валюти до долара (за замовчуванням 1.0)
# description - опис транзакції (за дефолтом None)
# Усі параметри повинні бути записані в захищені однойменні атрибути, наприклад currency повинен бути записаний у self._currency, а date в self._date.
# Доступ до них повинен бути забезпечений лише на читання та за допомогою механізму property. При чому якщо description дорівнює None,
# то відповідне property має повертати рядок "No description provided".
# Додатково, реалізуйте властивість usd, що має повертати суму переказу у доларах. Її можна обчислити за такою формулою: amount * usd_conversion_rate.

class Transaction:
    def __init__(
        self,
        amount: int,
        date: str,
        currency: str = "USD",
        usd_conversion_rate: float = 1.0,
        description: None = None,
    ) -> None:
        self._amount = amount
        self._date = date
        self._currency = currency
        self._usd_conversion_rate = usd_conversion_rate
        self._description = description

    @property
    def amount(self) -> int:
        return self._amount

    @property
    def date(self) -> str:
        return self._date

    @property
    def currency(self) -> str:
        return self._currency

    @property
    def usd_conversion_rate(self) -> float:
        return self._usd_conversion_rate

    @property
    def description(self) -> str:
        return (
            self._description
            if self._description is not None
            else "No description provided"
        )

    @property
    def usd(self) -> float:
        return self._usd_conversion_rate * self._amount

transaction = Transaction(
    amount=2000,
    currency="UAH",
    usd_conversion_rate=0.035,
    date="17.08.2021",
    description="Some description"
)
print(
    transaction.date,                # 17.08.2021
    transaction.amount,              # 2000
    transaction.currency,            # UAH
    transaction.usd_conversion_rate, # 0.035
    transaction.usd,                 # 70.0 (2000 * 0.035)
    transaction.description,         # "Some description"
)
transaction.description = "new"      # AttributeError: can't set attribute

transaction = Transaction(
    amount=100,
    date="17.08.2021",
)
print(
    transaction.date,                # 17.08.2021
    transaction.amount,              # 100
    transaction.currency,            # USD
    transaction.usd_conversion_rate, # 1.0
    transaction.usd,                 # 100.0
    transaction.description,         # "No description provided"
)
transaction.description = "new"      # AttributeError: can't set
