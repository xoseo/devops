from itertools import permutations

def domain_generator(sequence, r):
	# Передаем функции последовательность символов, диапазон(длину)
	# Возвращает список полученных имен
	# 0123456789abcdefghijklmnopqrstuvwxyz
	dom_combinations = permutations(sequence, r)
	list_of_domains = [''.join(i) for i in dom_combinations]
	return list_of_domains


print(len(domain_generator('0123456789abcdefghijklmnopqrstuvwxyz',4)))
