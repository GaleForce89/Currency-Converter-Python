"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.
"""

import currency

src = input('3-letter code for original currency: ')
dst = input('3-letter code for the new currency: ')
amt = input('Amount of the original currency: ')

exchange = currency.exchange(src, dst, amt)

print('You can exchange {0} {1} for {2:.3f} {3}.'. format(
    amt, src, exchange, dst))
