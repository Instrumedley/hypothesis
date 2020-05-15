from person import Person
from datetime import datetime

class TransactionBatch:

    def __init__(self, ledger_filepath):
        self.transactions = self.parse_ledger(ledger_filepath)
        self.balance = {}
        self.all_customers = []


    def parse_ledger(self, filepath):
        file = open(filepath, 'r')
        content = [line.rstrip() for line in file.readlines()]
        file.close()

        return content

    def process_batch(self):

        print(self.transactions)

        for transaction in self.transactions:
            parts = transaction.split(",")
            date = datetime.strptime(parts[0], '%Y-%m-%d %H:%M:%S')
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



        print("\n\nAll processed:")
        print(self.all_customers)
        for processed_person in self.all_customers:
            print(processed_person.name)
            print(processed_person.transactions)

    def get_customer_balance(self, customer_name, date):

        date = datetime.strptime(date, '%Y-%m-%d')
        for customer in self.all_customers:
            if customer.name == customer_name:
                return customer.get_balance(date)
            else:
                return "Customer does not exist"









ledger = 'ledger.txt'
transaction = TransactionBatch(ledger)
transaction.process_batch()
print(transaction.get_customer_balance("john","2015-01-18"))


