import boto3
import argparse
import datetime
import requests
from bs4 import BeautifulSoup
from collections import Counter

class CountTags():
	def __init__(self, page):
		self.page = requests.get(page)
		self.soup = BeautifulSoup(self.page.text, 'lxml')
	
	def all_tags(self):
		count = 0
		for tag in self.soup.body.find_all():
			count += 1
		return count

	def tags(self):
		tags_list = [tag.name for tag in self.soup.body.find_all()]
		return repr(Counter(tags_list)).strip('Counter()')

	@property
	def result(self):
		return f"{datetime.datetime.today().strftime('%Y/%m/%d %H:%M:%S')} {self.page.url} {self.all_tags()} {self.tags()}"
	

	def write_log(self,log_name):
		self.log_name = log_name
		timestamp = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")
		with open(self.log_name, 'a') as f_write:
			log_string = f"{timestamp} {self.page.url} {self.all_tags()} {self.tags()}\n"
			f_write.write(log_string)
		return [self.log_name, log_string]

	@staticmethod
	def upload_file(file_name, bucket_name, object_name=None):
		if object_name is None:
			object_name = file_name

		s3_client = boto3.client('s3')
		try:
			response = s3_client.upload_file(file_name, bucket_name, object_name)
		except Exception as e:
			print(e)
		return True


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Подсчет кол-ва тегов')
	parser.add_argument('url', type=str, help='Страница для которой будет произведен подсчет')
	parser.add_argument('-w',  type=str, nargs='?', const=f'{parser.prog}.log', help='Записать в файл', metavar='FILENAME')
	parser.add_argument('-s3', type=str, nargs='+', help='Отправить файл в s3 bucket. Обязательно указать имя отправляемого файла и имя бакета. Также опционально можно указать новое имя под которым будет загружен файл в бакет', metavar=('FILE_TO_UPLOAD BUCKET_NAME', 'NEW_FILE_IN_BUCKET'))
	args = parser.parse_args()

	if args.s3 and len(args.s3) < 2:
		parser.print_help()
		exit()

	countTags = CountTags(args.url)
	print(countTags.result)

	if args.w and args.s3:
		countTags.write_log(args.w)
		try:
			args.s3[2]
		except IndexError:
			args.s3.append(args.s3[0])
		countTags.upload_file(args.s3[0],args.s3[1],args.s3[2])
	elif args.w:
		countTags.write_log(args.w)
	elif args.s3:
		try:
			args.s3[2]
		except IndexError:
			args.s3.append(args.s3[0])
		countTags.upload_file(args.s3[0],args.s3[1],args.s3[2])








#test = CountTags('https://webscraper.io/test-sites/e-commerce/allinone')
test = CountTags('https://python-scripts.com/import-collections')

#print(test.all_tags())
#print(test.tags())
#test.write_log('CountTags.log')
#test.upload_file('CountTags.log', 'simazu-bucket1', 'test_log.txt')
#print(test.result)