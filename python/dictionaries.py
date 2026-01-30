"""Demonstrates dictionaries.
From: https://qr.ae/TWCAvj:
Python uses dictionaries all over the place:
- the variables and functions in a module - stored in a dictionary  # can be shown using globals()
- the local variables in a function - stored in a dictionary        # can be shown using locals(); see functions.py
- the implementation of a function - a dictionary
- a class is a dictionary
- an instance of a class is another dictionary
- the modules your program has imported - you guessed it - another dictionary
- even Python set objects are implemented as modified dictionaries
To paraphrase Tim Peter's 'Zen of Python': "dictionaries are great - let's do more of them".
Read more at https://qr.ae/TWCAvj.
"""


#%%
def demonstrate_dictionaries():
    """Creating and using dictionaries.
    - create a blank (empty) dictionary
    - create a non-empty dictionary
    - access dictionary values by the corresponding keys (syntax: value = d[key])
    - print a non-empty dictionary
        - print all items using the items() function
        - print one item per line
    - pprint dictionary in one column
    - add/remove items to/from a dictionary
    - update a dictionary with the items from another dictionary or from an iterable of (k, v) pairs using dict.update()
    - using the keys() and values() functions
    """

    d0 = {}
    print(d0)
    print(type(d0))
    print()

    buffalo_springfield = {'name': 'Buffalo Springfield', 'place': 'Los Angeles, CA', 'year': 1966}
    print(buffalo_springfield)
    print(type(buffalo_springfield))
    print()

    print(buffalo_springfield['name'])
    print()

    print(buffalo_springfield)
    print()

    from pprint import pprint
    pprint(buffalo_springfield)
    print()

    buffalo_springfield['active'] = True
    print(buffalo_springfield)
    print()

    del buffalo_springfield['active']
    print(buffalo_springfield)
    print()

    print(buffalo_springfield.items())
    print()

    for k, v in buffalo_springfield.items():
        print(f'{k}: {v}')

    # buffalo_springfield.update({'active': False, 'members': 5})
    buffalo_springfield.update([('active', False), ('members', 5)])
    print(buffalo_springfield)
    print()

    print(buffalo_springfield.keys())
    print(buffalo_springfield.values())
    print()


#%%
# Test demonstrate_dictionaries()
demonstrate_dictionaries()


#%%
def sort_dictionary(d, by):
    """Sorting a dictionary by keys or by values.
    - using zip()
    - using operator.itemgetter()   Use dict comprehension in the return statement, otherwise the compiler complains.
    - using lambda
    """

    # if by == 'k' or by == 'K':
    #     return dict(sorted(zip(d.keys(), d.values())))
    # elif by == 'v' or by == 'V':
    #     return dict(sorted(zip(d.values(), d.keys())))
    # else:
    #     return d

    # from operator import itemgetter
    # if by == 'k' or by == 'K':
    #     # return dict(sorted(d.items(), key=itemgetter(0)))
    #     return {k: v for k, v in sorted(d.items(), key=itemgetter(0))}
    # elif by == 'v' or by == 'V':
    #     # return dict(sorted(d.items(), key=itemgetter(1)))
    #     return {k: v for k, v in sorted(d.items(), key=itemgetter(1))}
    # else:
    #     return d

    if by == 'k' or by == 'K':
        # return dict(sorted(d.items(), key=itemgetter(0)))
        return {k: v for k, v in sorted(d.items(), key=lambda x: x[0])}
    elif by == 'v' or by == 'V':
        # return dict(sorted(d.items(), key=itemgetter(1)))
        return {k: v for k, v in sorted(d.items(), key=lambda x: x[1])}
    else:
        return d



#%%
def demonstrate_dict_sorting():
    """Demonstrate sorting a dictionary.
    """

    # from pprint import pprint         # when sorting by values, pprint doesn't show the resulting dictionary correctly

    songs = {3: 'Expecting to Fly', 1: 'For What It\'s Worth', 2: 'Broken Arrow'}
    # buffalo_springfield = {'name': 'Buffalo Springfield', 'place': 'Los Angeles, CA', 'year': 1966}
    buffalo_springfield = {'name': 'Buffalo Springfield', 'place': 'Los Angeles, CA', 'year': '1966'}

    print(sort_dictionary(songs, by='v'))
    print(sort_dictionary(buffalo_springfield, by='k'))
    print()

    print(sort_dictionary(songs, by='k'))
    print(sort_dictionary(buffalo_springfield, by='v'))


#%%
# Test demonstrate_dict_sorting()
demonstrate_dict_sorting()


#%%
def dict_comprehension(l1, l2):
    """
    Demonstrate dict comprehension
    :param l1: a list (or another iterable) of dict keys
    :param l2: a list (or another iterable) of dict values
    :return: a dict created by dict comprehension
    """

    return {k: v for k, v in zip(l1, l2)}


#%%
# Test dict_comprehension(l1, l2)
print(dict_comprehension(['Richie Furay', 'Bruce Palmer', 'Neil Young', 'Stephen Stills', 'Dewey Martin'],
                         ['rhythm guitar', 'bass', 'lead guitar', 'lead guitar', 'drums'],))
