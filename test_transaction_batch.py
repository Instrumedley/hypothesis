import unittest
from transaction_batch import TransactionBatch
from unittest.mock import patch, mock_open


class TestTransactionCore(unittest.TestCase):

    @classmethod
    def setUpClass(self) -> None:
        self.t = TransactionBatch("ledger.txt")



    def test_read_file(self):

        with patch("builtins.open", mock_open(read_data="data")) as mock_file:
            assert open("ledger.txt").read() == "data"
            mock_file.assert_called_with("ledger.txt")
        self.assertRaises(FileNotFoundError, lambda: self.t.parse_ledger("ledger2.txt"))

    def test_get_customer_balance(self):
        self.t.process_batch()

        # testing scenarios for Adrienne

        adrienne = "adrienne"
        date1 = "2015-01-18"
        date2 = "2015-01-20"
        date3 = "2015-01-21"
        date4 = "2015-01-24"

        self.assertEqual(self.t.get_customer_balance(adrienne, date1), -1)
        self.assertEqual(self.t.get_customer_balance(adrienne, date2), -40)
        self.assertEqual(self.t.get_customer_balance(adrienne, date3), -15)
        self.assertEqual(self.t.get_customer_balance(adrienne, date4), -15)

        # testing scenarios for grocery

        grocery = "grocery"
        date1 = "2015-01-15"
        date2 = "2015-01-18"
        date3 = "2015-01-19"
        date4 = "2015-01-20"
        date5 = "2018-01-25"
        date6 = "2015-01-18 08:26:00"

        self.assertEqual(self.t.get_customer_balance(grocery, date1), -1)
        self.assertEqual(self.t.get_customer_balance(grocery, date2), 100)
        self.assertEqual(self.t.get_customer_balance(grocery, date3), 140)
        self.assertEqual(self.t.get_customer_balance(grocery, date4), 140)
        self.assertEqual(self.t.get_customer_balance(grocery, date5), 140)
        self.assertEqual(self.t.get_customer_balance(grocery, date6), 100)

        # testing scenarios for insurance

        insurance = "insurance"
        date1 = "2015-01-16"
        date2 = "2015-01-17"
        date3 = "2015-01-24"

        self.assertEqual(self.t.get_customer_balance(insurance, date1), -1)
        self.assertEqual(self.t.get_customer_balance(insurance, date2), 100)
        self.assertEqual(self.t.get_customer_balance(insurance, date3), 200)

