class Account:
    def __init__(self, name: str) -> None:
        """
        Juts setting the account up with the name and balance
        :param name:setting the name of the account
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:

        """
        the method for deposting in the account
        :param amount: the amount set one wants to deposit
        :return: True if it works and false if the amount was 0 or negative
        """

        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        This is the method for withdrawls
        :param amount: the amount someone wants to take out of the account
        :return: True if it works and false if it does not because of a negative number or inssuficient funds
        """

        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        return self.__account_balance

    def get_name(self) -> str:
        return self.__account_name
