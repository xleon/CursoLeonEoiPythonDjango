from libs import urlloader
from urllib.error import HTTPError
import json

class Swapi:
    base_url = 'https://swapi.co/api/'
    __people = None

    def __get_results(self, resource):
        try:
            api_result = urlloader.load_url(self.base_url + resource)
            result_json = json.loads(api_result)
            return result_json['results']
        except HTTPError as error:
            print('Error al cargar url:', repr(error))
            return None
        except Exception as ex:
            print('Eerror genérico:', repr(ex))
            return None

    def get_people(self):
        if self.__people:
            return self.__people

        results = self.__get_results('people/')
        self.__people = [(person['name'], person['gender']) for person in results]
        return self.__people
            