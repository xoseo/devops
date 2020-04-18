import random
import sys

digit = random.randint(1,100)

while True:
	user_digit = input("Я загадал число от 1 до 100. Угадаешь? ")

	if not user_digit.isdigit():
		print("Нужно ввести число")
		continue
	else:
		user_digit = int(user_digit)

	if user_digit > digit:
		print("Слишком большое")
	elif user_digit < digit:
		print("Слишком маленькое")
	else:
		sys.exit("Угадал!")
