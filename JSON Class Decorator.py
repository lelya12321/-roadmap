import json


def jsonattr(filepath):
    def decorator(cls):
        with open(filepath) as f:
            file = json.load(f)
            s = file.items()

        for k, v in s:
            setattr(cls, k, v)
        return cls

    return decorator