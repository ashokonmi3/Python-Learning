class SimpleTaxCalculator:
    def income_tax(self, income: float) -> float:
        """
        Calculates the income tax based on the given income.

        :param income: The amount of income.
        :return: The amount of income tax.
        """
        threshold = 85528
        lower_rate = 0.17
        upper_rate = 0.32
        lower_tax = threshold * lower_rate

        if income <= threshold:
            return round(income * lower_rate, 2)
        else:
            upper_tax = (income - threshold) * upper_rate
            return round(lower_tax + upper_tax, 2)

    def vat_tax(self, price: float) -> float:
        """
        Calculates the VAT (Value Added Tax) based on the given price.

        :param price: The price of the item.
        :return: The amount of VAT.
        :raises TypeError: If the price is not a float or int.
        """
        vat_rate = 0.23  # Example VAT rate of 23%

        if not isinstance(price, (float, int)):
            raise TypeError('The price must be a number.')

        return price * vat_rate

    def capital_gains_tax(self, profit: float) -> float:
        """
        Calculates the capital gains tax based on the given profit.

        :param profit: The amount of profit.
        :return: The amount of capital gains tax.
        :raises TypeError: If the profit is not a float or int.
        """
        tax_rate = 0.19  # Example capital gains tax rate of 19%

        if not isinstance(profit, (float, int)):
            raise TypeError('The profit must be a number.')

        if profit <= 0:
            return 0.0

        return profit * tax_rate


def income_tax(income: float) -> float:
    """
    Calculates the income tax based on the given income.

    :param income: The amount of income.
    :return: The amount of income tax.
    """
    threshold = 85528
    lower_rate = 0.17
    upper_rate = 0.32
    lower_tax = threshold * lower_rate

    if income <= threshold:
        return round(income * lower_rate, 2)
    else:
        upper_tax = (income - threshold) * upper_rate
        return round(lower_tax + upper_tax, 2)


def vat_tax(price: float) -> float:
    """
    Calculates the VAT (Value Added Tax) based on the given price.

    :param price: The price of the item.
    :return: The amount of VAT.
    :raises TypeError: If the price is not a float or int.
    """
    vat_rate = 0.23  # Example VAT rate of 23%

    if not isinstance(price, (float, int)):
        raise TypeError('The price must be a number.')

    return price * vat_rate


def capital_gains_tax(profit: float) -> float:
    """
    Calculates the capital gains tax based on the given profit.

    :param profit: The amount of profit.
    :return: The amount of capital gains tax.
    :raises TypeError: If the profit is not a float or int.
    """
    tax_rate = 0.19  # Example capital gains tax rate of 19%

    if not isinstance(profit, (float, int)):
        raise TypeError('The profit must be a number.')

    if profit <= 0:
        return 0.0

    return profit * tax_rate


def calculate_tax(amount, tax_rate, age):
    """
    Calculates the income tax based on the given amount, tax rate, and age.

    :param amount: The amount of income.
    :param tax_rate: The tax rate as a decimal.
    :param age: The age of the taxpayer.
    :return: The amount of income tax.
    """
    if age <= 18:
        return min(amount * tax_rate, 5000)
    elif age <= 65:
        return amount * tax_rate
    else:
        return min(amount * tax_rate, 8000)
