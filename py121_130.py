import requests

btc =requests.get("https://api.bithumb.com/public/ticker/").json()['data']

variation = int(btc['max_price'])-int(btc['min_price'])
res = variation+int(btc['opening_price'])

if res>int(btc['max_price']):
    print("up")
else:
    print("down")