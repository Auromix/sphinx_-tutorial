class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations.

    Attributes
    ----------
    name : str
        The name of the calculator.
    """

    def __init__(self, name="Simple Calculator"):
        """
        Initialize the Calculator with a given name.

        Parameters
        ----------
        name : str, optional
            The name of the calculator (default is "Simple Calculator").
        """
        self.name = name

    def add(self, a, b):
        """
        Return the sum of two numbers.

        Parameters
        ----------
        a : float
            The first number.
        b : float
            The second number.

        Returns
        -------
        float
            The sum of a and b.
        """
        return a + b

    def subtract(self, a, b):
        """
        Return the difference between two numbers.

        Parameters
        ----------
        a : float
            The first number.
        b : float
            The second number.

        Returns
        -------
        float
            The difference of a and b.
        """
        return a - b

    def multiply(self, a, b):
        """
        Return the product of two numbers.

        Parameters
        ----------
        a : float
            The first number.
        b : float
            The second number.

        Returns
        -------
        float
            The product of a and b.
        """
        return a * b

    def divide(self, a, b):
        """
        Return the division of two numbers.

        Parameters
        ----------
        a : float
            The numerator.
        b : float
            The denominator.

        Returns
        -------
        float
            The quotient of a divided by b.

        Raises
        ------
        ValueError
            If the denominator is zero.
        """
        if b == 0:
            raise ValueError("Denominator cannot be zero.")
        return a / b

