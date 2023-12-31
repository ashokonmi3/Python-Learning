# filename = __file__
# import pdb; pdb.set_trace()
# print(f'path = {filename}')

# =============================
# import os
# def get_path(filename):
#     """Return file's path or empty string if no path."""
#     head, tail = os.path.split(filename)
#     import pdb; pdb.set_trace()
#     return head


# filename = __file__
# print(f'path = {get_path(filename)}')
# =================================

# import os

# def get_path(filename):
#     """Return file's path or empty string if no path."""
#     head, tail = os.path.split(filename)
#     return head

# filename = __file__
# import pdb; pdb.set_trace()
# filename_path = get_path(filename)
# print(f'path = {filename_path}')

# =================================
# import util

# filename = __file__
# import pdb; pdb.set_trace()
# filename_path = util.get_path(filename)
# print(f'path = {filename_path}')

# =================================
import os

def get_path(fname):
    """Return file's path or empty string if no path."""
    import pdb; pdb.set_trace()
    head, tail = os.path.split(fname)
    for char in tail:
        pass  # Check filename char
    return head


filename = __file__
filename_path = get_path(filename)
print(f'path = {filename_path}')

# ======================

# num_list = [500, 600, 700]
# alpha_list = ['x', 'y', 'z']

# def nested_loop():
#     for number in num_list:
#         print(number)
#         for letter in alpha_list:
#             print(letter)

# if __name__ == '__main__':
#     nested_loop()