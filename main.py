import json
import logging
import csv
from typing import Iterator, Union


def get_data(prices: str = 'prices.txt',
             transactions: str = 'transactions.txt') -> Union[dict, Iterator]:
    """
    get data from our sources
    """
    with open(prices, 'r') as prices_file, \
            open(transactions, 'r') as trans_file:
        # Read the transactions
        transactions = csv.reader(trans_file)
        # Read the prices
        prices = json.load(prices_file)
    return prices, transactions


def print_portfolio():
    """ Print the stocks in the portfolio and their values
    """
    prices, transactions = get_data()

    # Calculate the value for each transaction
    total = 0
    for i in transactions:
        d, s, q = transactions[i]
        total += int(q) * prices[s]
        # print the stock, amount we hold, and the %-share of the total portfolio
        try:
          print("%s  %.2f %.2f%%" % (s, prices[s] * int(q), prices[s] * int(q)/total * 100))
        except:
          pass

    # Print the total amount
    print("Total %.2f 100.00%%" % total)
    return


# This is for pytest
def test_print_portfolio(capsys):
    """ Test print_portfolio()
    """
    # Write some test data to the files to be read
    with open('transactions.txt', "w") as f:
        # CSV: List of transactions that shaped the porfolio:
        # Date,ticker,amount
        f.write("2023-01-03,AAPL,15\n")
    with open('prices.txt', 'w') as f:
        # JSON: Current price of each relevant stock
        f.write('{"AAPL": 125.07}\n')

    # Print the portfolio
    print_portfolio()

    # Collect the output
    printed_output = capsys.readouterr().out

    # Compare the output to the printed output
    expected_output = (
        "AAPL  1876.05 100.00%\n"
        "Total 1876.05 100.00%\n"
        )
    assert printed_output == expected_output


if __name__ == '__main__':
    print_portfolio()
