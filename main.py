import requests
from requests.exceptions import HTTPError

_HEADERS = {'x-parse-application-id': 'unAFkcaNDeXajurGB7LChj8SgQYS2ptm'}  
_URL= 'https://xx9p7hp1p7.execute-api.us-east-1.amazonaws.com/prod/PortalGeral'

def download_request(url, headers):
  """
  This function get a json file with params for new requests to get data files url.
  This return a *requests* object.
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

def get_url(data_params, type):
  file_extension = type
  file = data_params.json()['results'][0]

  if type == 'csv':
    file_url = file['arquivo_srag']['url']
  else:
    file_url = file['arquivo']['url']

  return file_url

def download_file(file_url, headers):

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



