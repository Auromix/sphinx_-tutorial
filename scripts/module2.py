
# Google Docstring

class BankAccount:
    """
    A simple bank account class to manage balance and transactions.

    Attributes:
        account_number (str): The account number of the bank account.
        balance (float): The current balance of the bank account.

    Example:
        >>> account = BankAccount('123456789', 1000.0)
        >>> account.deposit(500.0)
        >>> account.get_balance()
        1500.0
        >>> account.withdraw(200.0)
        >>> account.get_balance()
        1300.0
        >>> account.withdraw(2000.0)  # Raises ValueError: Insufficient balance.
    """

    def __init__(self, account_number: str, initial_balance: float = 0.0):
        """
        Initializes a new bank account with an account number and an optional initial balance.

        Args:
            account_number (str): The account number for the bank account.
            initial_balance (float, optional): The initial balance of the bank account. Defaults to 0.0.

        Example:
            >>> account = BankAccount('987654321', 500.0)
            >>> account.account_number
            '987654321'
            >>> account.balance
            500.0
        """
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount: float) -> None:
        """
        Deposits a specified amount into the bank account.

        Args:
            amount (float): The amount to deposit. Must be positive.

        Raises:
            ValueError: If the deposit amount is not positive.

        Example:
            >>> account = BankAccount('123456789', 1000.0)
            >>> account.deposit(500.0)
            >>> account.get_balance()
            1500.0
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Withdraws a specified amount from the bank account.

        Args:
            amount (float): The amount to withdraw. Must be positive and less than or equal to the current balance.

        Raises:
            ValueError: If the withdrawal amount is not positive or exceeds the current balance.

        Example:
            >>> account = BankAccount('123456789', 1000.0)
            >>> account.withdraw(200.0)
            >>> account.get_balance()
            800.0
            >>> account.withdraw(2000.0)  # Raises ValueError: Insufficient balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount

    def get_balance(self) -> float:
        """
        Retrieves the current balance of the bank account.

        Returns:
            float: The current balance of the account.

        Example:
            >>> account = BankAccount('123456789', 1000.0)
            >>> account.get_balance()
            1000.0
        """
        return self.balance
