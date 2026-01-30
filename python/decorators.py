"""Demonstrates the concept of decorators and user-defined decorators
"""


#%%
# Setup / Data

import functools

from python.functions import *

# Setup / Data
neil = 'Neil Young'
stephen = 'Stephen Stills'
richie = 'Richie Furray'
dewey = 'Dewey Martin'
bruce = 'Bruce Palmer'

buffalo_springfield = [neil, stephen, richie, dewey, bruce]


#%%
def a_very_simple_decorator(f):
    """Illustrates the essential idea of decorators:
        - take a function (f) as a parameter of a decorator function (decorator)
        - use the parameter function f inside an inner wrapper function (g)
        - return the inner wrapper function g from the decorator function
    Then define f and run f = decorator(f) before calling f.
    Even better, just put @decorator before the definition of f. Each call to f will then actually run decorator(f).
    """

    # Examples (run them in Python Console):

    # def decorator(f):
    #     def g():
    #         return f('Stephen Stills')
    #     return g
    #
    # def something(x):
    #     return x
    # ...
    # >>> something(4)
    # 4
    # ...
    # >>> something = decorator(something)
    # >>> something
    # <function __main__.decorator.<locals>.g()>
    # >>> something()
    # Stephen Stills

    # def decorator(f, *args):
    #     def g():
    #         print('Stephen Stills')
    #         return f(*args)
    #     return g
    #
    # def something(x):
    #     return x
    # ...
    # >>> something(4)
    # 4
    # ...
    # >>> something = decorator(something, 'Stephen Stills')
    # >>> something
    # <function __main__.decorator.<locals>.g()>
    # >>> something()
    # Stephen Stills
    # Stephen Stills

    def decorator(*args, **kwargs):
        print('------')
        v = f(*args, **kwargs)
        print('------')
        return v
    return decorator


#%%
# Test a_very_simple_decorator(f)
def songs(*args):
    print(f'{", ".join([arg for arg in args])}')


#%%
songs('For What It\'s Worth', 'Black Queen')

#%%
f = a_very_simple_decorator(songs)
f('For What It\'s Worth', 'Black Queen')

#%%
songs = a_very_simple_decorator(songs)
songs('For What It\'s Worth', 'Black Queen')
print()
songs()


#%%
def band_details(f_to_decorate):
    """Demonstrates how to develop a decorator.
    Uses the decorator-writing pattern (https://stackoverflow.com/a/3394911/1899061):
    import functools
    def decorator(f_to_decorate):
        @functools.wraps(f_to_decorate)			        # preserves func's identity after it's decorated
        def wrapper_decorator(*args, **kwargs):         # see https://stackoverflow.com/a/309000/1899061 for details
            # Do something before
            value = f_to_decorate(*args, **kwargs)      # (*args, **kwargs) are wrapper_decorator's formal arguments!
            # Do something after
            return value
        return wrapper_decorator
    """

    @functools.wraps(f_to_decorate)
    def wrapper_decorator(*args, **kwargs):
        m = ', '.join(args[1:]) if args else ''
        m = 'Members: ' + m if m else ''
        start = str(kwargs['start']) if kwargs.get('start') else ''
        end = str(kwargs['end']) if kwargs.get('end') else ''
        a = f'Active: {start}-{end}' if start and end else ''
        v = f_to_decorate(*args, **kwargs)
        if m and a:
            m += '; '
            print(f'{m}{a}')
        elif m:
            print(f'{m}')
        elif a and not m:
            print(f'{a}')
        else:
            pass
        return v

    return wrapper_decorator


#%%
@band_details
def print_band(name, *members, **years_active):
    """If not decorated, just prints the name a band, assuming that the name is a string.
    The decorator before the function signature (@members) illustrates how to apply a decorator;
    omit it if decorating manually.
    """

    print(name)


#%%
# Test members(f_to_decorate)
# print(print_band('Buffalo Springfield', *buffalo_springfield, ))
# print(print_band('Buffalo Springfield', start=1962, end=1970))
# print(print_band('Buffalo Springfield', *buffalo_springfield, start=1962, end=1970))
print_band('Buffalo Springfield', *buffalo_springfield, )
print_band('Buffalo Springfield', start=1962, end=1970)
print_band('Buffalo Springfield', *buffalo_springfield, start=1962, end=1970)

#%%
# Demonstrating the purpose of @functools.wraps(f_to_decorate)
print(print_band.__name__)      # try it with and without @functools.wraps(f_to_decorate) in the decorator

