""" 2. Написати функцію < bank > , яка працює за наступною логікою: користувач робить вклад у
розмірі < a > одиниць строком на < years > років під < percents > відсотків
(кожен рік сума вкладу збільшується на цей відсоток, ці гроші додаються до суми вкладу і в наступному
році на них також нараховуються відсотки). Параметр < percents > є необов'язковим і має
значення по замовчуванню < 10 > (10%).
Функція повинна принтануть і вернуть суму, яка буде на рахунку.
"""

def bank (b,years,percents=10):
	if (b*10)%10==0:
		a=int(b)
	else:
		a=b
	if a and years>0:
		z=a
		for i in range(years):
			perc=(z/100)*percents
			z+=perc
		
		if years%10==1 and years!=11:
			s="рік"
		elif years%10==2 or years%10==3 or years%10==4:	
			s='роки'
		elif years>4:	
			s='років'
	else:
		print('Сума вкладу та кількість років повинні бути більше 0')
	print('Сума, що буде на рахунку через',years, s, 'під',percents, '%', 'із початкового вкладу',a,'дорівнює:',z)
	return(z)
bank(float(input('Введіть суму вкладу:')),int(input('Введіть кількість років, напротязі яких будуть нараховані відсотки (у числовій формі):')))
