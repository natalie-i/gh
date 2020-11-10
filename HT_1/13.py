""" 13. Write a script to get the maximum and minimum value in a dictionary.
"""
a={1:10,2:20,3:30,4:40,5:50}
max=max(a.keys(),key=(lambda i:a[i]))
min=min(a.keys(),key=(lambda i:a[i]))
print("max:",a[max],"\nmin:",a[min])
