from termcolor import colored
import requests, bs4, sys

query = sys.argv[1]
site = str("https://miami.craigslist.org/search/sss?query=" + str(query) + "&sort=rel&bundleDuplicates=1&srchType=T&min_price=5").replace(" ", "+")
res = requests.get(site)
res.raise_for_status()
craigslist = bs4.BeautifulSoup(res.text, "lxml")

title = craigslist.select('.result-title')
price = craigslist.select('span > span[class="result-price"]')
link = craigslist.select('.result-image')
date = craigslist.select('.result-date')

total = 10
if len(sys.argv) == 3:
    total = int(sys.argv[2])

print( colored('----------------------------------------------------------------', 'red'))

shown=0
shownIndex = []
shownPrices = []
notIncluded = 0
for i in range( 0, len(title)):

    if price[i].getText() not in shownPrices and price[i].getText() != "$1":
        shown = shown + 1
        shownIndex.append(i)
        shownPrices.append(price[i].getText())
        print(shown, str(title[i].getText()))
        print(" = "+ str(price[i].getText()))
        print(link[i].get('href'))
        print( colored('----------------------------------------------------------------', 'red'))
    else:
        notIncluded = notIncluded + 1
    
    if shown == total:
        break

average = 0
r = 0
lowest = 0
highest = 0

for i in shownIndex:
    number = int(price[i].getText().replace("$",""))
    average = average + number  
    
    if r == 0:
        lowest = int(str(price[i].getText().replace("$","")))
        highest = int(str(price[i].getText().replace("$","")))

    r = r + 1

    if int(price[i].getText().replace("$","")) < lowest:
        lowest = int(str(price[i].getText().replace("$","")))


    if int(price[i].getText().replace("$","")) > highest:
        highest = int(str(price[i].getText().replace("$","")))

    
average = average / r

print( colored('\nResults', 'green'), site)

print( "\n" + colored('Average', 'green') + " $" +  str(int(average)) + " " + colored('High', 'green') + " $" + str(highest) + " " + colored('Low', 'green') + " $" + str(lowest), "\n")

