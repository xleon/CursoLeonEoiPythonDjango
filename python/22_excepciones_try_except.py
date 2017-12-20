from libs.urlloader import load_url
from urllib.error import HTTPError

try:
    raise Exception('esto no funciona ni con dinero')
    print('funcionará????')
except Exception as error:
    print('ha fallado:', repr(error))

try:
    load_url('https://swapi.co/api/peo')
except HTTPError as error:
    print('Error al cargar la url:', repr(error))
except Exception as ex:
    print('Error genérico:', repr(ex))