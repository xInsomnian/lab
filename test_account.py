import pytest
from account import *


class Test:
    def setup_method(self):
        self.a1 = Account('Joe')
        self.a2 = Account('Jane')

    def teardown_method(self):
        del self.a1
        del self.a2

    def test_init(self):
        assert self.a1.get_name() == 'Joe'
        assert self.a2.get_name() == 'Jane'
        assert self.a1.get_balance == pytest.approx(0, abs=0.001)
        assert self.a2.get_balance == pytest.approx(0, abs=0.001)

    def test_deposit(self):
        assert self.a1.deposit(30) is True
        assert self.a1.get_balance == pytest.approx(30, abs=0.001)

        assert self.a1.deposit(-30) is False
        assert self.a1.get_balance == pytest.approx(30, abs=0.001)

        assert self.a1.deposit(30.5) is True
        assert self.a1.get_balance == pytest.approx(60.5, abs=0.001)

        assert self.a2.deposit(25.5) is True
        assert self.a2.get_balance == pytest.approx(25.5, abs=0.001)

        assert self.a2.deposit(-30.5) is False
        assert self.a2.get_balance == pytest.approx(25.5, abs=0.001)

        assert self.a2.deposit(0) is False
        assert self.a2.get_balance == pytest.approx(25.5, abs=0.001)

    def test_withdraw(self):
        assert self.a1.deposit(30) is True
        assert self.a1.get_balance == pytest.approx(30, abs=0.001)

        assert self.a1.withdraw(20) is True
        assert self.a1.get_balance == pytest.approx(10, abs=0.001)

        assert self.a1.withdraw(5.5) is True
        assert self.a1.get_balance == pytest.approx(4.5, abs=0.001)

        assert self.a1.withdraw(0) is False
        assert self.a1.get_balance == pytest.approx(4.5, abs=0.001)

        assert self.a1.withdraw(-15.5) is False
        assert self.a1.get_balance == pytest.approx(4.5, abs=0.001)

        assert self.a1.withdraw(10) is False
        assert self.a1.get_balance == pytest.approx(4.5, abs=0.001)
