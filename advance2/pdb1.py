# filename = __file__
# print(filename)
# import pdb; pdb.set_trace()
# print(f'path = {filename}')


# ==============================
# example 2
# import os

# def get_path(filename):
#     """Return file's path or empty string if no path."""
#     head, tail = os.path.split(filename)
#     # os.path.split() method in Python is used to Split the path name into a pair head and tail. Here, tail is the last path name component and head is everything leading up to that.
#     print("2"*5)
#     print(head)
#     print(tail)
#     import pdb; pdb.set_trace()
#     return head


# filename = __file__
# print("file name ",filename)
# print(f'path = {get_path(filename)}')
# ================================
# (Pdb) p filename will give the value of the filename
# ============================
# example 3 s step in

# import os


# def get_path(filename):
#     """Return file's path or empty string if no path."""
#     head, tail = os.path.split(filename)
#     return head


# filename = __file__
# import pdb; pdb.set_trace()
# filename_path = get_path(filename)
# print(f'path = {filename_path}')
# ---------------
# ./example3.py 
# > /code/example3.py(14)<module>()
# -> filename_path = get_path(filename)
# (Pdb) n
# > /code/example3.py(15)<module>()
# -> print(f'path = {filename_path}')
# (Pdb) 

# $ ./example3.py 
# > /code/example3.py(14)<module>()
# -> filename_path = get_path(filename)
# (Pdb) s
# --Call--
# > /code/example3.py(6)get_path()
# -> def get_path(filename):
# (Pdb) 


# ===========================
