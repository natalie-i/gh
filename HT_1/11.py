""" 11. Write a script to remove duplicates from Dictionary.
"""
a={1:10,2:20,3:30,4:40,1:10,2:20}
b={}
for key,value in a.items():
    if value not in b.values():
        b[key] = value
print(b)
