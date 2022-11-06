import json
import requests

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=12345,us&appid=6aa7c1d29786fcc9dc92be346207055a')
data = r.json()
print(data)