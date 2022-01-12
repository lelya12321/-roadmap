class NewClass(object):
    def __init__(self, genereator):
        self.generator = genereator

    def __enter__(self):
        return next(self.generator)


    def __exit__(self, *args):
        return self.generator.close()

def contextmanager(f):
    def wrapper(*args, **kwargs):
        return NewClass(f(*args, **kwargs))
    return wrapper