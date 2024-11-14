class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations.

    This class provides methods for basic arithmetic operations including
    addition, subtraction, multiplication, and division.

    Attributes
    ----------
    name : str
        The name of the calculator.

    Examples
    --------
    >>> calc = Calculator("My Calculator")
    >>> calc.add(5, 3)
    8.0
    >>> calc.divide(10, 2)
    5.0
    """

    def __init__(self, name: str = "Simple Calculator") -> None:
        """
        Initialize the Calculator with a given name.

        :param name: The name of the calculator (default is "Simple Calculator").
        :type name: str, optional

        Examples
        --------
        >>> calc = Calculator("Advanced Calculator")
        >>> calc.name
        'Advanced Calculator'
        """
        self.name = name

    def add(self, a: float, b: float) -> float:
        """
        Return the sum of two numbers.

        :param a: The first number.
        :type a: float
        :param b: The second number.
        :type b: float
        :return: The sum of a and b.
        :rtype: float

        Examples
        --------
        >>> calc = Calculator()
        >>> calc.add(2, 3)
        5.0
        """
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """
        Return the difference between two numbers.

        :param a: The first number.
        :type a: float
        :param b: The second number.
        :type b: float
        :return: The difference of a and b.
        :rtype: float

        Examples
        --------
        >>> calc = Calculator()
        >>> calc.subtract(10, 5)
        5.0
        """
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """
        Return the product of two numbers.

        :param a: The first number.
        :type a: float
        :param b: The second number.
        :type b: float
        :return: The product of a and b.
        :rtype: float

        Examples
        --------
        >>> calc = Calculator()
        >>> calc.multiply(4, 2.5)
        10.0
        """
        return a * b

    def divide(self, a: float, b: float) -> float:
        """
        Return the division of two numbers.

        :param a: The numerator.
        :type a: float
        :param b: The denominator.
        :type b: float
        :return: The quotient of a divided by b.
        :rtype: float
        :raises ValueError: If the denominator is zero.

        Examples
        --------
        >>> calc = Calculator()
        >>> calc.divide(8, 2)
        4.0
        >>> calc.divide(5, 0)
        Traceback (most recent call last):
            ...
        ValueError: Denominator cannot be zero.
        """
        if b == 0:
            raise ValueError("Denominator cannot be zero.")
        return a / b
