import yfinance as yf
from datetime import datetime, timedelta
import pytz
import time

# Function to check if pre-market prices show a bear or bull market
def check_market_trend(symbol):
    # Get historical data for the past 2 days, including pre-market
    end_date = datetime.now()
    start_date = end_date - timedelta(days=2)
    data = yf.download(symbol, start=start_date, end=end_date)

    # Convert data to Eastern Time
    eastern = pytz.timezone('US/Eastern')
    data.index = data.index.tz_localize('UTC').tz_convert(eastern)

    # Filter data for pre-market hours (4am to 9am Eastern Time)
    pre_market_data = data.between_time("04:00", "09:00")

    # Check if overall price decreased during pre-market
    if pre_market_data["Close"].pct_change().sum() < 0:
        return "The stock market is currently a Bear Market."
    else:
        return "The stock market is currently a Bull Market."

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
    display_current_time()
    result = check_market_trend(symbol)
    print(result)
    display_next_run_time()
    
    # Sleep for 24 hours
    time.sleep(24 * 60 * 60)
