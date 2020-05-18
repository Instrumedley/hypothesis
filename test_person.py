import unittest
from person import Person
from exceptions import AddTransactionError, InvalidNumberError, InvalidDateError

class TestPerson(unittest.TestCase):

    @classmethod
    def setUpClass(self) -> None:
        self.p = Person("Rafael", "1985-03-06 00:00:00", -100, "Hypothesis", "sent")


    def test_get_balance(self):

        self.assertEqual(self.p.get_balance("1985-03-04"), -1)
        self.assertEqual(self.p.get_balance("1985-03-06"), -1)
        self.assertEqual(self.p.get_balance("1985-03-07"), -100)
        self.assertEqual(self.p.get_balance("1985-03-09"), -100)

        # see if it calculates the balance correctly when we do a transaction of 200 to it
        date = "1985-03-09 00:00:00"
        self.p.add_transaction(date, 200, 'bla', 'bla')
        self.assertEqual(self.p.get_balance("1985-03-10"), 100)

        # check for incorrect input format on amount (only floats and ints)
        self.assertRaises(InvalidNumberError, lambda: self.p.add_transaction(date, "100", 'bla', 'bla'))

        # check for incorrect input format on date
        self.assertRaises(InvalidDateError, lambda: self.p.add_transaction("sdsfd", "100", 'bla', 'bla'))

    def test_add_transaction(self):
        desired_date = "1985-03-05 00:00:00"
        self.assertRaises(AddTransactionError, lambda: self.p.add_transaction(desired_date, 100, 'bla', 'bla'))
