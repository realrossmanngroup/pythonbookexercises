import urllib.request
import time

def get_price():
    page = urllib.request.urlopen("htthome/louis/Documents/success/pt/html/prices-loyalty.html")
    text = page.read().decode("utf8")
    indexvalue = text.find('>$')
    price = text[indexvalue+2:indexvalue+6]
    floatprice = float(price)
    print(floatprice)


price = 99.99
floatprice = float(price)
while floatprice > 4.74:
    get_price()
    time.sleep(60) 

print ("Buy!")


    
    
