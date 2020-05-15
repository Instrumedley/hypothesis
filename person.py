from datetime import datetime

class Person:

    def __init__(self, name, initial_date, amount, payee, type):
        print("\n\nCreated person: {}\n\n".format(name))
        self._name = name
        self.transactions = {initial_date: [amount, payee, amount, type] }

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value



    def get_balance(self, desired_date):
        # get a list of the dates and sort it
        dates = list(self.transactions.keys())

        dates.sort()

        prior_date = None
        for date in dates:
            if date < desired_date:
                prior_date = date
            else:
                break;

        print("\nPrior date: ")
        print(prior_date)
        if prior_date == None:
            return 0
        else:
            print("\nSelf.transactions:")
            print(self.transactions)
            print("\nPrevious balance of {} is: ".format(self._name))

            print(self.transactions[prior_date][2])
            return self.transactions[prior_date][2]



    def add_transaction(self, date, amount, payee, type):

        if type == "sent":
            print("{} is now paying: {}".format(self._name, amount))
        if type == "received":
            print("{} just received: {} ".format(self._name, amount))
        self.transactions[date] = [amount, payee, self.get_balance(date) + amount, type]



if __name__ == "__main__":
    rafael = Person("Rafael",'1985-03-06,100')
