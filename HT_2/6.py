""" 6. Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345"
-> просто потицяв по клавi
   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
-  якщо довжина бульше 50 - > ваша фантазiя
"""
import re
def symbols (x):
	if len(x)<50 and len(x)>30:
		print("довжина",len(x))
		print("кількість букв:",len(re.findall(r"[a-z]",x)))
		print("кількість цифр:",len(re.findall(r"[0-9]",x)))
	elif len(x)<30:
		a=(re.findall(r"\d",x))
		b=[int(i) for i in a]
		c=sum(b)
		print("сума всіх чисел:",c)
		d=(re.findall(r"\w",x))
		e="".join(d)
		f=(re.findall(r"\D",e))
		print("рядок без цифр:","".join(f))
	elif len(x)>50:
		print(re.findall(r"[^gekhub]",x))
	return(x)
symbols(input())
