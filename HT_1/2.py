""" 2. Write a script to print out a set containing all the colours from color_list_1 which are not present in color_list_2.
        Test Data :
        color_list_1 = set(["White", "Black", "Red"])
        color_list_2 = set(["Red", "Green"])
        Expected Output :
        {'Black', 'White'}

"""
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
c=set(color_list_1)-set(color_list_2)
print(c)
