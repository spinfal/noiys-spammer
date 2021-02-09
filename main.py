import requests as r
import time as t
import random
from fake_useragent import UserAgent
ua = UserAgent()

#nouns = ["puppy", "car", "rabbit", "girl", "monkey"]
#verbs = ["runs", "hits", "jumps", "drives", "barfs"]
#adv = ["crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally."]
#adj = ["adorable", "clueless", "dirty", "odd", "stupid"]

msg = input('message: ')

while True:
  
  #num = random.randrange(0,5)
  
  #msg = f'{nouns[num]} {verbs[num]} {adv[num]} {adj[num]}'
  
  agent = ua.random
  
  headers = {
    'User-Agent': agent,
    'Content-Type': 'application/json'
  }

  json = {
    'text': msg
  }

  res = r.post('http://www.noiys.com/status', headers=headers, json=json)
  print(f'{agent}\n{msg}\n')
  print(str(res.status_code))
  t.sleep(0) # change delay here (in seconds)
