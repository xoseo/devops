import whois, time, os
from itertools import permutations

def domain_generator(sequence, r):
	# Передаем функции последовательность символов, диапазон(длину)
	# Возвращает список полученных имен
	# -0123456789abcdefghijklmnopqrstuvwxyz
	dom_combinations = permutations(sequence, r)
	list_of_domains = [''.join(i) for i in dom_combinations]
	return list_of_domains

def domain_checker(dom_list, log_file):
	if os.path.exists(log_file):
		with open(log_file, "rb") as file:
			file.seek(-2, os.SEEK_END)
			while file.read(1) != b'\n':
				file.seek(-2, os.SEEK_CUR)
			dom = file.readline().decode().split()[0].strip('.ru')
			start_from = dom_list.index(dom)+1
	for dom in dom_list[start_from:]:
		domain = whois.query(dom + '.ru')
		with open(log_file, 'a', encoding='utf-8') as f:
			if not domain:
				print(f"{dom}.ru Expiration date: FREE")
				f.write(f"{dom}.ru Expiration date: FREE\n")
			else:
				print(f"{domain.__dict__['name']} Expiration date: {domain.__dict__['expiration_date']}")
				f.write(f"{domain.__dict__['name']} Expiration date: {domain.__dict__['expiration_date']}\n")
			time.sleep(0.5)


if __name__ == "__main__":
	dom_list = domain_generator('-0123456789abcdefghijklmnopqrstuvwxyz', 4)
	domain_checker(dom_list, '/home/konta/4_char_domains')
