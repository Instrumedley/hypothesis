import argparse
from datetime import datetime
from transaction_batch import TransactionBatch
from exceptions import AddTransactionError, InvalidNumberError, InvalidDateError

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ledger", type=str,
                        help="The path to the ledger file ( file must be .txt )")
    parser.add_argument("party_name", type=str,
                        help="The party's name for which you would like to check the balance")
    parser.add_argument("--date", type=str,
                        help="(Optional) The date on which you would like to see the balance ( format: YYYY-MM-DD )"
                             "If not given, the current balance(today) will be printed")

    args = parser.parse_args()
    ledger = args.ledger
    name = args.party_name

    if(args.date):
        date = args.date
    else:
        date = str(datetime.today().strftime('%Y-%m-%d'))

    try:
        transaction = TransactionBatch(ledger)
        transaction.process_batch()
        total = transaction.get_customer_balance(name, date)
        if total == -1:
            print("Customer {} did not have an account by {}: ".format(name, date))
        else:
            print("Current balance for {} on {}: ".format(name, date))
            print(total)

    except FileNotFoundError:
        print("Error! Ledger file not found. Make sure you input the correct path")
    except ValueError:
        print("Error! Incorrect input provided when creating User's account ")
    except InvalidDateError:
        print("Error! You entered an invalid date parameter")
    except InvalidNumberError:
        print("Error! Incorrect format for number. Please use only integers and floats")



