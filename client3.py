################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    """ ------------- Update this function ------------- """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2 
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    if price_b != 0:
        return price_a / price_b
    else:
        return None  


if __name__ == "__main__":
    prices = {}  # Create a dictionary to store stock prices

    # Query the price once every N seconds.
    for _ in range(N):
        try:
            quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())
        except Exception as e:
            print(f"Error fetching quotes: {e}")
            continue  # Skip the current iteration if there's an error

        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price  # Store the price in the dictionary
            print(f"Quoted {stock} at (bid:{bid_price}, ask:{ask_price}, price:{price})")

        # Use the stored prices to calculate and print the ratio
        stock_a = 'ABC'
        stock_b = 'DEF'

        price_a = prices.get(stock_a)
        price_b = prices.get(stock_b)

        if price_a is not None and price_b is not None:
            ratio = getRatio(price_a, price_b)
            if ratio is not None:
                print(f"Ratio {ratio}")
            else:
                print("Cannot calculate ratio. Denominator is zero.")
        else:
            print(f"Cannot calculate ratio. One or both stock prices not found. Available stocks: {list(prices.keys())}")