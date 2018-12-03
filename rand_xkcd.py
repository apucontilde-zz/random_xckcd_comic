import json
import random
import os
import webbrowser

import requests

try:
  last_comic = requests.get('https://xkcd.com/info.0.json').json()['num']
except Exception:
  print('could not get latest comic index.')
  exit(1)

random.seed(a=os.urandom(256))
comic = 404
while comic == 404
    comic = random.randrange(1, last_comic)
url = f"https://xkcd.com/{comic}/"
print(url)
webbrowser.open(url)
