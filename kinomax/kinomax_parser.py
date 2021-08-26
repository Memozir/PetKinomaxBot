import requests
from bs4 import BeautifulSoup
import re

LINK = 'https://admin.kinomax.ru/vladimir/'


def result():

	BUY_LINK = "https://admin.kinomax.ru/films/"

	result = []

	headers = {
		'user-agent': 'choppa322'
	}

	get = requests.get(LINK, headers=headers)
	soup = BeautifulSoup(get.text, 'html.parser')

	films = soup.find_all('div', class_='film')

	for film in films:


		# Searching film`s title
		text = film.find('div', class_='d-flex flex-column w-90')
		title = text.find('div', class_='d-flex fs-09 pb-2')
		title = title.find('a') 	# Title


		# Get href
		href = str(title.get('href'))
		discription_link = href
		href = re.split(r'/', href)[2]


		# info = text.find('div', class_='d-flex fs-08 pt-3 text-main')
		# info = str(info.find('div', class_='w-70').text) 	#info


		# Get discription
		dis_link = 'https://admin.kinomax.ru' + discription_link
		get_discription = requests.get(dis_link, headers=headers)
		discription_soup = BeautifulSoup(get_discription.text, 'html.parser')

		discription_container = discription_soup.find_all('div', class_='container')[6]
		discription = discription_container.find('div', class_='pt-4').text

		# Creating an result
		result.append(
				{
					'title': title.text,
					'buy': BUY_LINK + href,
					'discription': discription
				}
			)

	return result


if __name__ == '__main__':

	a = result()

	# for i in a:
	# 	print(i['discription'])
