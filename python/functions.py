"""Demonstrates details of writing Python functions: annotations, default args, kwargs.
Also demonstrates functions as parameters of other functions and
functions as return values of other functions
"""


#%%
# Setup / Data
song = 'For What It\'s Worth'
year = 1966

neil = 'Neil Young'
stephen = 'Stephen Stills'
richie = 'Richie Furray'
dewey = 'Dewey Martin'
bruce = 'Bruce Palmer'

buffalo_springfield = [neil, stephen, richie, dewey, bruce]


#%%
# def demonstrate_annotations(title, year):
def demonstrate_annotations(title: str, year: int) -> str:

    """Demonstrates how to use annotations of
    function parameters/arguments (<arg>: <type>) and of function return type (def f(...) -> <type>:).
    - print the function parameters/arguments
    - print the value of the __annotations__ attribute of this function
    - print the name and the docstring of this function
    - return a formatted string (including function parameters/arguments)
    """

    print(title + ',', year)
    print(demonstrate_annotations.__annotations__)
    print(demonstrate_annotations.__name__ + '\n' + demonstrate_annotations.__doc__)

    return f'{demonstrate_annotations.__name__}(\'{title}\', {year})'


#%%
# Test demonstrate_annotations(title, year)
print(demonstrate_annotations(song, year))


#%%
def show_song(title, author=stephen, year: int = 1966):

    """Demonstrates default arguments/parameters.
    - print locals()
    - print the function arguments/parameters in one line
    """

    print(locals())

    print(f'{title}, by {author} ({year})')


#%%
# Test def show_song(title, author=stephen, year: int = 1966):
show_song(song)
print()
show_song('Expecting to Fly', author=neil)


#%%
def use_flexible_arg_list(band: str, *members):
    """Demonstrates flexible number of arguments/parameters.
    - print the band name and the list of band members in one line
    """

    print(members)
    print(*members)
    print()

    print(band + ': ' + ', '.join(members))
    print(f'{band}: {", ".join(members)}')


#%%
# Test use_flexible_arg_list(band: str, *members)
use_flexible_arg_list('Buffalo Springfield', *buffalo_springfield)
use_flexible_arg_list('Buffalo Springfield')


#%%
def use_all_categories_of_args(band, *members, is_active=True, **details):
    """Demonstrates positional args, flexible args, keyword args, and kwargs (flexible keyword args).
    - print all arguments/parameters, including the keyword arguments/parameters, in one line
    """

    print(details)
    print(*details)
    # print(**details)

    b = band
    m = ', '.join(members) if members else ''
    a = 'active' if is_active else 'inactive'
    d = 'formed: ' + str(details.get('start', 'unknown')) if details.get('start') else ''
    d = d + '; disbanded: ' + str(details.get('end', 'unknown')) if details.get('end') else d

    if m and d:
        print(f'{b}: {m} ({a}); {d}')
    elif m:
        print(f'{b}: {m} ({a})')
    elif d:
        print(f'{b} ({a}); {d}')
    else:
        print(f'{b} ({a})')


#%%
# Test use_all_categories_of_args(band, *members, is_active=True, **details)
use_all_categories_of_args('Buffalo Springfield', is_active=False, start=1966, end=1968)
print()
use_all_categories_of_args('Buffalo Springfield', *buffalo_springfield, is_active=False,
                           start=1966, end=1968)


#%%
def pass_simple_function_as_parameter():
    """Demonstrates using another function as a parameter. It works because functions are objects.
    If a call to f includes positional arguments, then they are part of the *args argument of this function.
    The same holds for optional *args in the call to f.
    """

    # Try something like this in Python Console:
    #     p = *[1,2,3]        # generates an error;
    #                           asterisk * isn't simply unary operator,
    #                           it's argument-unpacking operator for function definitions and function calls;
    #                           heuristics: use it "inside of something else", like inside (), [] and constructors
    #     p = *[1,2,3],       # generates a tuple, because of the comma (* is actually "inside creating a tuple")
    #     p = 44, *[1,2,3]    # generates another tuple
    #     print(p)
    #     print(*p)

    # # Case 1: 0 or more arguments
    # def f(*members):
    #     if members:
    #         print(', '.join(members))
    #     else:
    #         print('No members')
    #
    # def g(f, *members):
    #     f(*members)
    #
    # g(f, *buffalo_springfield)
    # g(f)

    # Try also this in Python Console:
    #     def f(*args):
    #         return sum(args)      # it must be sum(args), not sum(*args); e.g. in Python Console sum((1, 2)) is OK
    #     def g(f, *args):
    #         return f(*args)       # heuristics: if *args is in a f. signature, use *args in the f. body as well
    #     g(f, *(1, 2, 3))          # result: 6
    #     g(f, *[1, 2, 3])          # result: 6

    # Case 2: 1 or more arguments (the first one is positional)
    def f(band, *members):
        if members:
            print(band + ':', ', '.join(members))
        else:
            print(band + ': no members specified')

    def g(f, band, *members):
        f(band, *members)

    g(f, 'Buffalo Springfield', *buffalo_springfield)
    print()
    g(f, 'Buffalo Springfield', )
    print()
    g(f, *buffalo_springfield)


#%%
# Test pass_simple_function_as_parameter()
pass_simple_function_as_parameter()


#%%
def pass_function_as_parameter(f, *args, **kwargs):
    """Demonstrates using another function as a parameter. It works because functions are objects.
    The argument/parameter list specified as in this function is a fairly general one -
    it works regardless of the number of *args and **kwargs in the function call (both can be 0).
    However, if f includes positional arguments, they must be passed in the call to this function.
    In that case, they are treated as part of the *args argument of this function,
    but must be passed explicitly in the call to this function.
    Optional *args of f may or may not be passed in the call to this function (just like in the call to f).
    Likewise, if f is called with default arguments,
    they are included in the **kwargs argument of this function.
    In other words, from https://stackoverflow.com/a/3394898/1899061:
    You can use *args and **kwargs along with named arguments too. The explicit arguments get values first
    and then everything else is passed to *args and **kwargs. The named arguments come first in the list. For example:
        def table_things(titlestring, **kwargs)
    If f has default arguments, they can be included in **kwargs in the beginning of f
    (e.g., if f has a default arg d=4, then the first line of f would be kwargs['d'] = d),
    and then f is called as f(*args, **kwargs), just as if d=4 was always part of **kwargs:
    -------
    def f(*args, year=1966, **kwargs):
        kwargs['year'] = year

        print(args)             # result: a tuple of args
        print(*args)            # result: a sequence of args, 'untupled'
        print(kwargs)

    def g(h, *args, **kwargs):
        return h(*args, **kwargs)

    g(f, 'Neil', 'Young', True, birth=1945)
    -------
    See https://stackoverflow.com/a/34206138/1899061 for further details.
    """

    f(*args, **kwargs)


#%%
# Test pass_function_as_parameter(f, *args, **kwargs)
pass_function_as_parameter(use_all_categories_of_args, 'Buffalo Springfield', *buffalo_springfield, is_active=False,
                           start=1962, end=1970)


#%%
def return_function(full_name, first_name_flag):
    """Demonstrates using a function as the return value from another function.
    In this example, depending on the first_name_flag, return_function() returns one of the following functions:
    - a function that returns a person's first name
    - a function that returns a person's family name
    """

    def first():
        return full_name.split()[0]

    def last():
        return full_name.split()[1]

    return first if first_name_flag else last


#%%
# Test return_function(full_name, first_name_flag)
f = return_function('Stephen Stills', False)
print(f())


#%%
def return_function_with_args(*args):
    """Demonstrates using a function as the return value from another function.
    The returned function has parameters/arguments.
    In this example, depending on len(args), return_function_with_args() returns one of the following functions:
    - a function that returns an empty tuple (or an empty list)
    - a function that returns a tuple of args (or a list of args, or...)
    """

    def empty_tuple():
        return ()

    def tuple_of_args(*p):
        return p

    return empty_tuple if not args else tuple_of_args


#%%
# Test return_function_with_args(*args)
f = return_function_with_args()
print(f())
f = return_function_with_args(1)
print(f('Stephen', 'Stills', 1945))

