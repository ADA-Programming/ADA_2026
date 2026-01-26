"""Demonstrates how operators and expressions work in Python.
"""

from settings import *


#%%
def demonstrate_arithmetic_operators():
    """Working with arithmetic operators.
    Arithmetic operators in Python are pretty much the same as in other programming languages.
    The integer division operator: //
    """

    print( 10 // 3 - 14 % 12 * 3)


#%%
# Test demonstrate_arithmetic_operators()
demonstrate_arithmetic_operators()

#%%


def demonstrate_relational_operators():
    """Working with relational operators.
    - simple comparisons
    - comparing dates (== vs. is)
    - is compares id()'s, == compares contents
    - id()'s are the same for equal strings and numbers, but not for lists, user class instances,...
    - comparing dates (>, <, etc. with dates)
    - None in comparisons, type(None)
    """

    print(2 > 3)
    print()

    from datetime import date
    d1 = date(1966, 4, 11)
    d2 = date(1968, 5, 5)
    d3 = date(1966, 4, 11)
    print(d1 > d2)
    print(d3 == d1)
    print(d3 is d1)
    print()

    print(id(d1) == id(d3))
    print()

    s1 = 'Buffalo Springfield'
    s2 = 'Buffalo Springfield'
    print(s1 == s2)
    print(id(s1) == id(s2))
    print()

    l1 = [1, 2, 3]
    l2 = [1, 2, 3]
    print(l1 == l2)
    print(id(l1) == id(l2))
    print()

    print(type(None))
    # print(d1 > None)
    print(not None is d1)
    print(not None == d1)


#%%
# Test demonstrate_relational_operators()
demonstrate_relational_operators()

#%%


def demonstrate_logical_operators():
    """Working with logical operators.
    - logical operations with True, False and None
    - logical operations with dates
        - make sure to read this: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not !!!
          (or just this: https://stackoverflow.com/questions/44612144/logical-operators-in-python)
    - logical operations with None (incl. None and int, None and date, etc.)
    - None and date vs. None > date
    """

    print((2 > 3) and True)
    print((2 > 3) or True)
    print(not (2 > 3) or False)
    print()

    print(None and True)
    print(None or True)
    print(not (None or False))
    print(1 and True)
    print(1 or False)
    print(True and 2)
    print()

    from datetime import date
    d1 = date(1966, 4, 11)
    d2 = date(1968, 5, 5)
    print(d1 > d2 and d1 < d2)
    print(d2 and d1)
    print(None and d1)
    print(d1 and None)
    # print(d1 > None)


#%%
# Test demonstrate_logical_operators()
demonstrate_logical_operators()

