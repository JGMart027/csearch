# csearch
Dependencies:   requests, bs4, sys; from termcolor import colored

usage:    python csearch.py "item"
i.e.      python csearch.py "iphone"

Search craigslist listings from the terminal. 

This script will return all listings shown on craigslist along with 
their respective links, and then calculates the highest, lowest, 
and average prices.

*This is a small script I wrote for fun when I was automating Craigslist listings. 
I used this script to help determine how much to sell things for online. 
Could be used to completely automate online listings in a way so that you don't even 
have to set the price yourself.*

Not included in this script:

*exception handling -> the only error I have encountered is if the listing does not exist.



