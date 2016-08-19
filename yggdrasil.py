import requests
import json

data = json.dumps({"agent":{"name":"Minecraft","version":1}, "username":"abcd","password":"abcd"})
headers = {'Content-Type': 'application/json'}
r = requests.post('https://authserver.mojang.com/authenticate', data=data, headers=headers)
print (r.text)
