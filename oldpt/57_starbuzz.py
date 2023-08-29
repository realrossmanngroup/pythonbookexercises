import urllib.request

page = urllib.request.urlopen("https://beans.itcarlow.ie/prices-loyalty.html")
text = page.read().decode("utf8")
indexvalue = text.find('>$')
price = text[indexvalue+2:indexvalue+6]
int(price)
while price > 4.74:
    print(price)
