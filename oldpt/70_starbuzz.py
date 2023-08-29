import urllib.request
import time

price = 99.99
floatprice = float(price)
while floatprice > 4.74:
    page = urllib.request.urlopen("https://beans.itcarlow.ie/prices-loyalty.html")
    text = page.read().decode("utf8")
    indexvalue = text.find('>$')
    price = text[indexvalue+2:indexvalue+6]
    floatprice = float(price)
    print("The price of beans is $",(floatprice), ", buy!")
    time.sleep(900)
    
