class UnexpectedTypeException(Exception):
    def __init__(self, text):
        self.txt = text


def expected_type(return_types):
    def real_decorator(function):
        def wrapper(*args):

            w = args[0] if type(args) is tuple else args

            class Eq_():
                def __init__(self, some_type):
                    self.some_type = some_type

                def __eq__(self, other):
                    if isinstance(other, Eq_):
                        return self.some_type == other.some_type
                    return NotImplemented

            a = Eq_(return_types[0])
            b = Eq_(type(w))

            if a == b:
                return w
            else:
                raise UnexpectedTypeException('UnexpectedTypeException')

        return wrapper
    return real_decorator