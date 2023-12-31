
def module_funct(arg1, arg2 = 'default', *args):
    """This is a module-level function."""
    local_var = arg1 * 3
    return local_var

class X(object):
    """Definition for X class."""

    def __init__(self, name):
        self.name = name

    def get_name(self):
        "Returns the name of the instance."
        return self.name

x_obj = X('sample_instance')

class Y(X):
    """This is the Y class, 
    child of X class.
    """

    # This method is not part of X class.
    def do_something(self):
        """Anything can be done here."""

    def get_name(self):
        "Overrides version from X"
        return 'Y(' + self.name + ')'
