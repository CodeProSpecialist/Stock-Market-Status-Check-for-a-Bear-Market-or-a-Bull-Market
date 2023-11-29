#!/bin/bash

# Update package list
sudo apt-get update

# Install Python3
sudo apt-get install -y python3

# Install pip3
sudo apt-get install -y python3-pip

# Install yfinance
pip3 install yfinance

# Install pytz
pip3 install pytz
