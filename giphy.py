import requests

API_KEY = '7MoBjO3FZ056uWr0Y3cx1RuA08EfMC34'
LIMIT = '1'
OFFSET = '0'
RATING = 'g'
LANG = 'en'
BUNDLE = 'messagin_non_clips'


def compose_search_url(search_request: str):
    url = 'https://api.giphy.com/v1/gifs/search?api_key=' + API_KEY
    url += '&q=' + search_request
    url += '&limit=' + LIMIT
    url += '&offset=' + OFFSET
    url += '&rating=' + RATING
    url += '&lang=' + LANG
    url += '&bundle=' + BUNDLE
    return url


def get_image_url(search_request: str) -> str:
    response = requests.get(compose_search_url(search_request))
    if response.status_code == 200:
        return response.json()['data'][0]['url']
    else:
        return 'Sorry, API isn`t working'
