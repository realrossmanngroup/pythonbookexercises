import urllib.request

page = urllib.request.urlopen("https://beans.itcarlow.ie/prices.html")
text = page.read().decode("utf8")
price = text[234:238]
print(price)
