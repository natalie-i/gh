""" 9. Write a script to remove an empty tuple(s) from a list of tuples.
        Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
        Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
"""
a=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
q=[i for i in a if i]
print(q)
