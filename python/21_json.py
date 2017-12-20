"""
Ejemplo de llamada http y parseo de json
"""

from libs.urlloader import load_url
import json

people_api_result = load_url('https://swapi.co/api/people/')
result_json = json.loads(people_api_result)
people = result_json['results']

for person in people:
    print(person['name'])