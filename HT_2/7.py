""" 7. Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи -
один з яких операцiя, яку зробити!
"""
def calculator_1 (a,c,b):
	if c=="*":
		print(a,"*",b,"=",a*b)
	elif c=="-":
		print(a,"-",b,"=",a-b)
	elif c=="+":
		print(a,"+",b,"=",a+b)
	elif c=="/":
		print(a,"/",b,"=",a//b)
calculator_1(int(input()),input(),int(input()))
