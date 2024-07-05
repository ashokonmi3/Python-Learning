s = "If Comrade Napoleon says it, it must be right."
a = [100, 200, 300]


def foo(arg):
    '''This is module and function is foo'''
    print(f'arg = {arg}')


class Foo:
    '''This is module and class is Foo'''
    name = "python"

    def get_name(self):
        "Returns the name of the instance."
#         self.name= "Python"
        return self.name


# When a .py file is imported as a module, Python sets the special dunder variable __name__ to the name of the module. However, if a file is run as a standalone script, __name__ is (creatively) set to the string '__main__'. Using this fact, you can discern which is the case at run-time and alter behavior accordingly:
if (__name__ == '__main__'):
    print('Executing as standalone script')
    print(s)
    print(a)
    foo('quux')
    x = Foo()
    print(x)
else:
    print('Executing as imported script')
