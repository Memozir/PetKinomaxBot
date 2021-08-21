import requests
from bs4 import BeautifulSoup
import re

LINK = 'https://admin.kinomax.ru/vladimir/'

# def get_dig(href):

# 	href_digit = ''
# 	count = 0

# 	for i in href:
# 		if i == '/':
# 			if count == 2:
# 				href_digit += i
# 			else:
# 				count += 1
# 				continue
# 		else:
# 			continue
# 	return href_digit


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
		href = str(title.get('href'))	#href
		href = re.split(r'/', href)[2]


		info = text.find('div', class_='d-flex fs-08 pt-3 text-main')
		info = str(info.find('div', class_='w-70').text) 	#info


		result.append(
				{
					'title': title.text,
					'buy': BUY_LINK + href
				}
			)

	return result



if __name__ == '__main__':

	a = result()

	for i in a:
		print(i['title'])

	
