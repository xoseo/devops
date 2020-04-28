import csv

class CsvParser():
	def __init__(self, file_name):
		self.file_name = file_name

	def proper_sell_over(self, item_type: str, threshold: int):
		self.item_type = str(item_type)
		self.threshold = int(threshold)
		with open(self.file_name, 'r') as f_read:
			csv_reader = csv.DictReader(f_read)
			country_list = []
			country_dict = {}
			for line in csv_reader:
				if line['Item Type'] == item_type:
					if line['Country'] not in country_dict:
						country_dict[line['Country']] = float(line['Units Sold'])
					else:
						country_dict[line['Country']] += float(line['Units Sold'])
			for k, v in country_dict.items():
				if v > threshold:
					country_list.append(k)
		return country_list

	def sell_over(self, item_type: str, threshold: int):
		"""
		Данный метод, кажется работает неверно с точки зрения поставленного задания.
		Метод ищет строки у которых Units Sold больше threshold, хотя по идее должен искать 
		все строки с нужным Item Type и суммировать Units Sold и в том случае если значение
		выходит больше threshold, выводить. Например этот метод не покажет Sweden, если
		threshold = 8000, хотя у этой страны:
		Sweden Baby Food 7963
		Sweden Baby Food 5949
		т.е. суммарно больше 8000
		Метод proper_sell_over считает верно
		"""
		self.item_type = str(item_type)
		self.threshold = int(threshold)
		with open(self.file_name, 'r') as f_read:
			csv_reader = csv.DictReader(f_read)
			country_list = []
			country_dict = {}
			for line in csv_reader:
				if line["Item Type"] == self.item_type and float(line["Units Sold"]) > self.threshold:
					country_list.append(line["Country"])
		return sorted(set(country_list))

	def get_country_profit(self, country):
		self.country = country
		with open(self.file_name, 'r') as f_read:
			reader = csv.reader(f_read)
			total_profit = 0
			for line in reader:
				if line[1] == self.country:
					total_profit = total_profit + float(line[13])
			return round(total_profit, 2)

	def save_as(self, new_file_name, delimiter):
		self.new_file_name = new_file_name
		self.delimiter = delimiter
		with open(self.file_name, 'r') as f_read:
			with open(self.new_file_name, 'w') as f_write:
				reader = csv.reader(f_read)
				writer = csv.writer(f_write, delimiter=self.delimiter)
				for line in reader:
					writer.writerow(line)


#csv_test = CsvParser('1000_Sales_Records.csv')

#csv_test.save_as('1000_Sales_Records_new_delimiter.csv', '#')
#print(csv_test.get_country_profit('Japan'))
#print(csv_test.sell_over('Baby Food', 8000))


