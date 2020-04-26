def bold(func):
    def wrapper(*args, **kwargs):
        return '<b>' + func(*args, **kwargs) + '</b>'
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        return '<i>' + func(*args, **kwargs) + '</i>'
    return wrapper

def underline(func):
    def wrapper(*args, **kwargs):
        return '<u>' + func(*args, **kwargs) + '</u>'
    return wrapper
