from person import Person
from datetime import datetime

class TransactionBatch:

    def __init__(self, ledger_filepath):
        self.transactions = self.parse_ledger(ledger_filepath)
        self.balance = {}
        self.all_customers = []


    def parse_ledger(self, filepath):
        try:
            file = open(filepath, 'r')
            content = [line.rstrip() for line in file.readlines()]
            file.close()

            return content
        except FileNotFoundError:
            raise

    def process_batch(self):

        for transaction in self.transactions:
            parts = transaction.split(",")
            date = parts[0]
            name_payer = parts[1]
            name_payee = parts[2]
            amount = float(parts[3])
            payer_exists = False
            payee_exists = False

            if len(self.all_customers) > 0:
                for person in self.all_customers:
                    if person.name == name_payer:
                        payer_exists = True
                        person.add_transaction(date, amount*-1, name_payee, "sent")
                    if person.name == name_payee:
                        payee_exists = True
                        person.add_transaction(date, amount, name_payer, "received")

                if payer_exists == False:
                    person = Person(name_payer, date, amount*-1, name_payee, "payer")
                    self.all_customers.append(person)
                if payee_exists == False:
                    person = Person(name_payee, date, amount, name_payer, "payee")
                    self.all_customers.append(person)

            else:
                person = Person(name_payer, date, amount*-1, name_payee, "sent")
                self.all_customers.append(person)
                person = Person(name_payee, date, amount, name_payer, "received")
                self.all_customers.append(person)


        print("All customers in the batch have been processed!!")

    def get_customer_balance(self, customer_name, date):

        for customer in self.all_customers:
            if customer.name == customer_name:
                return customer.get_balance(date)

        return "Customer does not exist"




