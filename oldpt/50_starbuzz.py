import urllib.request

page = urllib.request.urlopen("https://beans.itcarlow.ie/prices-loyalty.html")
text = page.read().decode("utf8")
price = text[251:255]
print(price)
