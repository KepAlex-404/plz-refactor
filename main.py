import json
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
        transactions = tuple(csv.reader(trans_file))
        # Read the prices
        prices = json.load(prices_file)
    return prices, transactions


def print_portfolio():
    """
    Print the stocks in the portfolio and their values
    """
    # Calculate the value for each transaction
    # print the stock, amount we hold, and the %-share of the total portfolio

    prices, transactions = get_data()

    # calculate proper total prices of our portfolio
    total_sum = sum(int(sublist[2]) * prices[sublist[1]] for sublist in transactions)
    for transaction in transactions:
        _, stock, quantity = transaction
        total_position_price = prices[stock] * int(quantity)
        print(f"{stock} - {total_position_price:.2f} - {total_position_price/total_sum*100:.2f}%")

    # Print the total amount
    print(f"Total - {total_sum:.2f} - 100.00%")


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
        "AAPL - 1876.05 - 100.00%\n"
        "Total - 1876.05 - 100.00%\n"
        )
    assert printed_output == expected_output


if __name__ == '__main__':
    print_portfolio()
