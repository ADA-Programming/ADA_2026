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


#%%
def demonstrate_dict_sorting():
    """Demonstrate sorting a dictionary.
    """

    # from pprint import pprint         # when sorting by values, pprint doesn't show the resulting dictionary correctly

    songs = {3: 'Expecting to Fly', 1: 'For What It\'s Worth', 2: 'Broken Arrow'}
    buffalo_springfield = {'name': 'Buffalo Springfield', 'place': 'Los Angeles, CA', 'year': 1966}


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


#%%
# Test dict_comprehension(l1, l2)
# print(dict_comprehension(['rhythm guitar', 'bass', 'lead guitar', 'lead guitar', 'drums'],
#                          ['Richie Furay', 'Bruce Palmer', 'Neil Young', 'Stephen Stills', 'Dewey Martin']))
print(dict_comprehension(['Richie Furay', 'Bruce Palmer', 'Neil Young', 'Stephen Stills', 'Dewey Martin'],
                         ['rhythm guitar', 'bass', 'lead guitar', 'lead guitar', 'drums'],))
