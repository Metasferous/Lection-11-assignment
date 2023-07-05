import requests

api_key = '7MoBjO3FZ056uWr0Y3cx1RuA08EfMC34'
query = 'hello'
limit = '1'
offset = '0'
rating = 'g'
lang = 'en'
bundle = 'messagin_non_clips'


def compose_search_url(search_request: str):
    url = 'https://api.giphy.com/v1/gifs/search?api_key=' + api_key
    url += '&q=' + search_request
    url += '&limit=' + limit
    url += '&offset=' + offset
    url += '&rating=' + rating
    url += '&lang=' + lang
    url += '&bundle=' + bundle
    return url


def get_image_url(search_request: str) -> str:
    response = requests.get(compose_search_url(search_request))
    return response.json()['data'][0]['url']
