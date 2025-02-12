from .core import easy_speak

__all__ = ['easy_speak']

def __call__(*args, **kwargs):
    return easy_speak(*args, **kwargs)