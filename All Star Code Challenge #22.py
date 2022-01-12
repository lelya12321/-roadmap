import time

def to_time(seconds):
    hour = seconds//3600
    sec = (seconds - hour*3600)//60
    return '{} hour(s) and {} minute(s)'.format(hour, sec)