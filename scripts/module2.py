def multiply(a, b):
    """
    Return the product of two numbers.

    :param a: First number.
    :param b: Second number.
    :return: Product of a and b.
    """
    return a * b


def divide(a, b):
    """
    Return the division of two numbers.

    :param a: Numerator.
    :param b: Denominator.
    :return: Quotient of a divided by b.
    :raises ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b

