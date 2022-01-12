import base64

def to_base_64(string):
    a = string.encode('ascii')
    b = base64.b64encode(a)
    c = b.decode('ascii')
    return c


def from_base_64(string):
    a = string.encode('ascii')
    b = base64.b64decode(a)
    return b.decode('ascii')