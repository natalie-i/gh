""" 3. Написати функцiю season, яка приймає один аргумент — номер мiсяця
(вiд 1 до 12), яка буде повертати пору року,
якiй цей мiсяць належить (зима, весна, лiто або осiнь)
"""
def season(m):
        if (m>0 and m<3) or m==12:
                print("Winter")
                return("Winter")
        elif m>2 and m<6:
                print("Spring")
                return("Spring")
        elif m>5 and m<9:
                print("Summer")
                return("Summer")
        elif m>8 and m<12:
                print("Autumn")
                return("Autumn")
        else:
                print(m,"- It's not a number of the month:(")
                return(m,"- It's not a number of the month:(")
season(int(input()))
