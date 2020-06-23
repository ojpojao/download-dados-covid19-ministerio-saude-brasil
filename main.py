__author__ = "ojpojao"
__version__ = "1.0"
__email__ = "ojpojao@gmail.com"

import requests
from requests.exceptions import HTTPError

_HEADERS = {'x-parse-application-id': 'unAFkcaNDeXajurGB7LChj8SgQYS2ptm'}  
_URL= 'https://xx9p7hp1p7.execute-api.us-east-1.amazonaws.com/prod/PortalGeral'

def download_request(url: str, headers: dict):
  """
  This function get a json file with params for new requests to get data files url.
  This return a requests object: Response.

  Params:
  - url: url for request
  - headers: headers custom

  """
  try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
  except HTTPError as http_err:
    print(f'Error HTTP: {http_err}')
  except Exception as err:
    print(f'Error Code: {err}')
  else:
    # print('Getting File!')
    data_params = response
  return data_params

def get_url(data_params, type='csv') -> str:
  """
  Return a string with url to download file.

  Params:
  - data_params: response object from requests module
  - type: type of file. ['csv', 'xlsx']

  Default file type is csv.
  
  """

  file_extension = type
  file = data_params.json()['results'][0]

  if type == 'csv':
    file_url = file['arquivo_srag']['url']
  else:
    file_url = file['arquivo']['url']

  return file_url

def download_file(file_url: str, headers: dict):
  """
  Make a web request and save it to a file.

  Params:
  - file_url: url do download
  - headers: headers customizations
  """

  file = download_request(file_url, headers=headers)
  name_ext = file_url.split('.')[-1]

  date = data_params.json()['results'][0]['dt_atualizacao'].replace('/', '-')
  date = date.replace(' ', '-')
  date = date.replace(':', '')
  
  file_fullname = 'HIST_PAINEL_COVIDBR_' + date + 'H' + '.' + name_ext
  # print(file_fullname)
  with open(file_fullname, 'wb') as f:
    f.write(file.content)


data_params = download_request(_URL, _HEADERS)
file_url = get_url(data_params, 'csv')
download_file(file_url, _HEADERS)



