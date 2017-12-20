"""
La librería requests simplifica mucho el trabajo con llamadas
y respuestas http

http://docs.python-requests.org/en/master/
"""

import requests

response = requests.get('https://httpbin.org/ip')
ip = response.json()['origin']
print('Tu ip es', ip)

response = requests.get('https://swapi.co/api/people/')
people = response.json()['results']

for person in people:
    print(person['name'])
