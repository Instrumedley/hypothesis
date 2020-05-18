# THE MINI BANK TEST
For confidentiality purposes, the original specification is not described in this document as well as the company's name.


## Modifications/Improvements from the Original Specs

Instead of using a date format YYYY-MM-DD in the ledger I decided to use YYYY-MM-DD H:M:S .
My reasoning in doing that is that it would allow for multiple transactions in the same day for the same customer, allowing the user to retrieve the balance for a specific point in time in that day if wanted.

## Usage

You can run the program from the CLI with the following command

```bash
python main.py [ledger] [name] --[date]
```

where [ledger] is the path to the ledger file,
[name] is the party for which you would like to see the balance and
[date] is an optional argument if you wish to see the balance for a specific date. 

If [date] is not used, the program will output the current balance (current date).

If [date] is entered in the format YYYY-MM-DD H:M:S you will be able to see the current balance until that point.
 
If [date] is entered in the format YYYY-MM-DD you will see the final balance of that day , meaning his balance at YYYY-MM-DD 23:59:59


## Example

1) **Using the ledger.txt file provided in this repository and the following command**

```bash
python main.py ledger.txt adrienne --date="2015-01-20"
```

will output

```bash
All customers in the batch have been processed!!
Current balance for adrienne on 2015-01-20:
-40.0
```

2) **Using the ledger.txt file provided in this repository and the following command**

```bash
python main.py ledger.txt john --date="2015-01-18"
```

will output

```bash
All customers in the batch have been processed!!
Current balance for john on 2015-01-17: 
--245.0
```

3) **Using the ledger.txt file provided in this repository and the following command**

```bash
python main.py ledger.txt john --date="2015-01-17 15:30:00"
```

will output

```bash
All customers in the batch have been processed!!
Current balance for john on 2015-01-17 15:30:00: 
--145.0
```

## Unit Testing

Tests are provided for the classes Person and TransactionBatch.
You can run them by using the command

```bash
python -m unittest test_transaction_batch.py
python -m unittest test_person.py
```

These tests will work for the **ledger.txt** provided.
You can add your own tests in these files if you would like to test it with your own ledger file


## Comments

Since it was not specified, I decided to implement in a way that if the user enter a date e.g "2018-01-22" the outputted balance should be of 2018-01-22 23:59:59. I could also go for the other assumption that it should get the current balance up until 2018-01-21 23:59:59.
I picked the one I found less confusing to me, but in a real world scenario this is an example of a situation that you always check with your team/colleagues/manager :) . 
