import urllib.request
import time

def get_price():
    page = urllib.request.urlopen("https://beans.itcarlow.ie/prices-loyalty.html")
    text = page.read().decode("utf8")
    indexvalue = text.find('>$')
    price2 = text[indexvalue+2:indexvalue+6]
    floatprice = float(price2)
#   print(floatprice)
    return(floatprice)

g = input("Is price needed immediately? ")
if g == 'y':
    print(get_price())
else:
    price = 99.99
    while price > 4.74:
        time.sleep(900)
        get_price()
    print("Buy now!")    
        
#discount = 0.9
#discountm = float(discount)
#print("The discounted price is: ")
#price = get_price()
#actual_price = price * discountm
#print(str(actual_price))




    
    
