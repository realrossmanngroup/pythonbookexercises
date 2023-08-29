import urllib.request
import time
import tweepy

from auth import (
    consumer_key2,
    consumer_secret2,
    access_token2,
    access_token_secret2
)

client = tweepy.Client(consumer_key=consumer_key2,
                    consumer_secret=consumer_secret2,
                    access_token=access_token2,
                    access_token_secret=access_token_secret2)
# Replace the text with whatever you want to Tweet about

def send_to_twitter(msg):
    client.create_tweet(text=msg)

def get_price():
    page = urllib.request.urlopen("https://beans.itcarlow.ie/prices-loyalty.html")
    text = page.read().decode("utf8")
    indexvalue = text.find('>$')
    price = text[indexvalue+2:indexvalue+6]
    return(float(price))

g = input("Is price needed immediately? ")
if g == 'y':
    send_to_twitter(str(get_price()))
    print("If you are reading this, I successfully spammed melly's twitter :)")
else:
    print("If you are reading this, we are before the while but into the else")
    price = 99.99
    while price > 4.74:
        time.sleep(9)
        price = get_price()
        send_to_twitter("Buy4!")
        print("If you're reading this, I just sent something to twitter inside while loop")
    #print("Buy now!")    
        
    
    
