# csearch
Search craigslist listings from the terminal. 

Dependencies:   requests, bs4, sys; from termcolor import colored

usage:    python csearch.py "item"

i.e.      python csearch.py "iphone"


This script will return all listings shown on craigslist along with 
their respective links, and then calculates the highest, lowest, 
and average prices.


Not included in this script:

*exception handling -> the only error I have encountered is if the listing does not exist.
