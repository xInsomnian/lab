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

    def test_deposit(self):

    def test_withdraw(self):
