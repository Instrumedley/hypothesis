from datetime import datetime
from exceptions import AddTransactionError, InvalidNumberError, InvalidDateError
from utils import is_date

class Person:

    def __init__(self, name, initial_date, amount, payee, type):

        try:
            self._start_date = datetime.strptime(initial_date,'%Y-%m-%d %H:%M:%S')
            self._name = name
            self.transactions = {initial_date: [amount, payee, amount, type]}

            if not isinstance(amount, int) and not isinstance(amount, float):
                raise InvalidNumberError

        except ValueError:
            raise


    @property
    def start_date(self):
        return self._start_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def get_balance(self, desired_date):

        if not is_date(desired_date):
            raise InvalidDateError

        dates = list(self.transactions.keys())
        dates.sort()

        prior_date = None

        for date in dates:
            if date < desired_date:
                prior_date = date
            else:
                break

        if prior_date == None:
            return -1
        else:
            return float(self.transactions[prior_date][2])


    def add_transaction(self, date, amount, payee, type):

        if not is_date(date):
            raise InvalidDateError
        try:
            if datetime.strptime(date, '%Y-%m-%d %H:%M:%S') < self.start_date:
                raise AddTransactionError()

            if isinstance(amount, int) or isinstance(amount, float):
                self.transactions[date] = [amount, payee, self.get_balance(date) + amount, type]

            else:
                raise InvalidNumberError
        except TypeError:
            raise

