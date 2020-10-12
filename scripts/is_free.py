import whois, time
from itertools import combinations_with_replacement

def domain_generator(sequence, r):
	# Передаем функции последовательность символов, диапазон(длину)
	# Возвращает список полученных имен
	# 01234567890abcdefghijklmnopqrstuvwxyz
	dom_combinations = combinations_with_replacement(sequence, r)
	list_of_domains = [''.join(i) for i in dom_combinations]
	return list_of_domains


if __name__ == "__main__":
	dom_list = domain_generator('01234567890abcdefghijklmnopqrstuvwxyz', 2)
	for dom in dom_list:
		with open('2_char_domains', 'a', encoding='utf-8') as f:
			domain = whois.query(dom + '.ru')
			if not domain:
				print(f"{dom}.ru Expiration date: FREE")
				f.write(f"{dom}.ru Expiration date: FREE\n")
			else:
				print(f"{domain.__dict__['name']} Expiration date: {domain.__dict__['expiration_date']}")
				f.write(f"{domain.__dict__['name']} Expiration date: {domain.__dict__['expiration_date']}\n")
			time.sleep(0.5)