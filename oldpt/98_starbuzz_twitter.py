import urllib.request
import time

def send_to_twitter(msg):
    password_manager = urllib.request.HTTPPasswordMgr()
    password_manager.add_password("Twitter API", "http://twitter.com/statuses", "gypsy_elder", "Cinnamo098;")
    http_handler = urllib.request.HTTPBasicAuthHandler(password_manager)
    page_opener = urllib.request.build_opener(http_handler)
    urllib.request.install_opener(page_opener)
    params = urllib.parse.urlencode( {'status': msg} )
    resp = urllib.request.urlopen("http://twitter.com/statuses/update.json", params)
    resp.read()

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
    send_to_twitter(get_price())
else:
    print("Else loop is working")
    price = 99.99
    while price > 4.74:
        time.sleep(9)
        price = get_price()
        send_to_twitter("Buy!")
    #print("Buy now!")    
        
    
    
