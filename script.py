import requests
from pprint import PrettyPrinter
pp = PrettyPrinter()
apiKey = 'cf6d4ac5'
data_URL = 'http://www.omdbapi.com/?apikey='+apiKey
year = ''
movieTitle = input()
params = {
    's': movieTitle,
    'type': 'movie',
    'y': year
}
response = requests.get(data_URL, params=params).json()

pp.pprint(response)
