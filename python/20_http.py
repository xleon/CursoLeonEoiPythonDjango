"""
Ejemplo de llamadas http
"""

from urllib import request

def load_url(url):
    req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with request.urlopen(req) as response:
        return response.read()

people = load_url('https://swapi.co/api/people/')
print(people)