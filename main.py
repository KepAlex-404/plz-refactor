def print_portfolio():
    """ Print the stocks in the portfolio and their values
    """
    # Read the transactions
    trans_file = open('transactions.txt')
    transactions = []
    for t in trans_file.readlines():
        transactions.append(t.split(','))
    
    # Read the prices
    prices = eval(open('prices.txt').read())

    # Calculate the value for each transaction
    total = 0
    for i in range(len(transactions)):
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
