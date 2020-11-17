""" 3. Написати функцію < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000,
і яка вертатиме True, якщо це число просте, и False - якщо ні.
"""

def is_prime (a):
	if a in range(1001):
		if a<2:
			print('Введене число не є простим або складеним')
			return()
		else:
			n=0
			for i in range(1,a+1):
				if a%i==0:
					n+=1
	else:
		print('Треба було ввести число від 0 до 1000. Спробуйте ще раз')
	if n==2:
		print('True')
		return('True')
	else:
		print('False')
		return('False')

is_prime(int(input('Введіть число від 0 до 1000:')))
