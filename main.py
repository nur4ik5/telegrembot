import requests 
from bs4 import BeautifulSoup as bs







def get_html(url):
	resp = requests.get(url)
	return resp.text

def get_soup(html):
	# получаем щбьект bs4, в котором будем искать 
	soup = bs(html,'lxml')
	return soup

def get_date(soup):
			# код html и название парсера
	date = soup.find('div', class_ ='row hidden-xs').find('h3').get_text()
	return date 

def get_titles():
	url = 'https://www.ts.kg/'
	# print(get_html(url))
	html = get_html(url) 
	soup = get_soup(html)
	soup = bs(html, 'lxml')
	# находим нужный div и забираем все div, в которых лежат сериалы
	items = soup.find('div', class_='col-xs-8').find_all('div', class_='show')
	titles = []
	for item in items:
		title = item.find('p', class_= 'show-title').get_text()
		print(title)
		titles.append(title)
	return titles


def main():
	url = 'https://www.ts.kg/'
	# print(get_html(url))
	html = get_html(url) # получаем исходный html
	soup = get_soup(html) # получаем обьект bs
	date = get_date(soup) # парсии дату со страницы
	titles = get_titles(soup) # парсии названия сериала
	print(date)
	print(*titles, sep ='\n')
	# print(get_date(get_html(url)))
	# get_titles(get_html(url))

if __name__ == '__main__':
	main()


