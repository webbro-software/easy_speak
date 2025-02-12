from .core import easy_speech

__all__ = ['easy_speech']

def __call__(*args, **kwargs):
    return easy_speech(*args, **kwargs)