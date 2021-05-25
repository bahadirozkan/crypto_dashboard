from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
# import pandas as pd
# import time
# import pprint

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters = {
  'symbol':'BTC,ETH,ADA,BNB',
  'convert':'USD',
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'YOUR API KEY',
}

session = Session()
session.headers.update(headers)

try:
  # start = time.time()
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  ada = data['data']['ADA']['quote']['USD']['price']
  bnb = data['data']['BNB']['quote']['USD']['price']
  btc = data['data']['BTC']['quote']['USD']['price']
  eth = data['data']['ETH']['quote']['USD']['price']
  # end = time.time()

  # print(end-start)
  print('ADA:', ada)
  print('BNB:', bnb)
  print('BTC:', btc)
  print('ETH:', eth)
  # pprint.pprint(data)
  # print(data)

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)