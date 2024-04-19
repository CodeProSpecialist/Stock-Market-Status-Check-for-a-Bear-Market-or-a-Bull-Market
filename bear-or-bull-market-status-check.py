import yfinance as yf
from datetime import datetime, timedelta
import pytz
import time

# Function to check if pre-market prices show a bear or bull market
def check_market_trend(symbol):
    # Get historical data for the past 2 days, including pre-market
    end_date = datetime.now()
    start_date = end_date - timedelta(days=14)
    data = yf.download(symbol, start=start_date, end=end_date)

    # Convert data to Eastern Time
    eastern = pytz.timezone('US/Eastern')
    data.index = data.index.tz_localize('UTC').tz_convert(eastern)

    # Calculate percentage change in closing prices
    price_change = (data["Close"].iloc[-1] - data["Close"].iloc[0]) / data["Close"].iloc[0] * 100

    # Check if overall price increased or decreased
    if price_change > 0:
        return "The stock market is currently a Bull Market: +{:.2f}% during past 14 days.".format(price_change)
    elif price_change < 0:
        return "The stock market is currently a Bear Market: -{:.2f}% during past 14 days.".format(abs(price_change))
    else:
        return "The stock market prices remained unchanged."

# Function to display formatted date and time in Eastern Time
def display_current_time():
    eastern = pytz.timezone('US/Eastern')
    current_time = datetime.now(eastern)
    formatted_time = current_time.strftime("%A, %B %d, %Y %I:%M %p")
    print(f"Current Date and Time (Eastern Time): {formatted_time}")

# Function to calculate and display next run time
def display_next_run_time():
    eastern = pytz.timezone('US/Eastern')
    current_time = datetime.now(eastern)
    next_run_time = current_time + timedelta(days=1)
    formatted_time = next_run_time.strftime("%A, %B %d, %Y %I:%M %p")
    print(f"Next Run Time (Eastern Time): {formatted_time}")

# Example for SPY (S&P 500 ETF)
symbol = "SPY"

while True:

    print("\n")

    display_current_time()

    print("\n")

    result = check_market_trend(symbol)

    print("\n")

    print(result)

    print("\n")

    display_next_run_time()

    print("\n")

    # Sleep for 24 hours
    time.sleep(24 * 60 * 60)
