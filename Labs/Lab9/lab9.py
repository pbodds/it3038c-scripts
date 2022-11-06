import json
import requests

r = requests.get('http://localhost:3000')
data = r.json()

for w in data:
    print(w['name'], "is", w['color'], "\n")