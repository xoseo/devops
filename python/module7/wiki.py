import requests
from bs4 import BeautifulSoup

class WikiParser():
	def __init__(self, page):
		self.page = requests.get(page)
		self.soup = BeautifulSoup(self.page.text, 'lxml')

	def langs_list(self):
		lang_dict = {}
		for li in self.soup.body.find_all('li', class_='interlanguage-link'):
			lang_dict[li.a.text] = li.a['href']

		return lang_dict

	def tables_counter(self):
		count = 0
		for table in self.soup.body.find_all('table'):
			count += 1
		return count

	def tables_data(self):
		table_list = []
		for table in self.soup.body.find_all('table'):
			for tr in table.tbody.find_all('tr'):
				tr_list = []
				for td in tr.find_all("td"):
					if td.string is not None:
						tr_list.append(td.string)
				if tr_list:
					table_list.append(tr_list)
		return table_list

			







#test = WikiParser('https://en.wikipedia.org/wiki/Russia')

#print(test.langs_list())
#print(test.tables_counter())
print(test.tables_data())