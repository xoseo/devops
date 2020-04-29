import requests
import json
from bs4 import BeautifulSoup

def parse_top_250(file_to_write):
	url = 'https://imdb.com/chart/top'
	top250 = requests.get(url, headers={'Accept-Language': 'En-us'})
	soup = BeautifulSoup(top250.text, 'lxml')
	top250_list = []
	film_info = {}
	for child in soup.tbody.find_all('tr'):
		position = child.find('td', class_='posterColumn').span['data-value']
		film_name = child.find('td', class_='titleColumn').a.text
		year = child.find('td', class_='titleColumn').span.text.strip('()')
		team = child.find('td', class_='titleColumn').a['title'].split(', ')
		rating = child.find('td', class_='ratingColumn imdbRating').strong.text
		film_info = { film_name: { 'Position' : position,
									 'Year' : year,
									 'Director' : team[0].strip(' (dir.)'),
									 'Crew' : f"{team[1]}, {team[2]}",
									 'Rating' : rating,
									}
		}
		top250_list.append(film_info)
	with open(file_to_write, 'w') as f_write:
		f_write.write(json.dumps(top250_list))

