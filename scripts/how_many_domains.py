from itertools import combinations_with_replacement

def domain_generator(sequence, r):
	# Передаем функции последовательность символов, диапазон(длину)
	# Возвращает список полученных имен
	# 01234567890abcdefghijklmnopqrstuvwxyz
	dom_combinations = combinations_with_replacement(sequence, r)
	list_of_domains = [''.join(i) for i in dom_combinations]
	return list_of_domains


print(len(domain_generator('01234567890abcdefghijklmnopqrstuvwxyz',4)))