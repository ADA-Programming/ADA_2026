"""Demonstrates working with strings in Python.
"""


#%%
def demonstrate_formatting():
    """Demonstrating details of string formatting.
    - \n is the new line char
    - r'...' - raw formatting
    - using \"\"\"...\"\"\" for multi-line formatting
    - string "multiplication"
    - substrings / slicing
    - str() vs. repr() (usually the same, but with whitespace there is a difference)
    """

    print('Buffalo' + '\n' + 'Springfield')
    print('C:\now')
    print(r'C:\now')
    print()

    print("""
    This is 
    a multi-line string.
    """)
    print()

    print('Buffalo Springfield\n' * 3)
    print()

    print('Buffalo Springfield'[0:7])
    print('Buffalo Springfield'[-7:-1])
    print('Buffalo Springfield'[-11:])
    print()

    print('\tBuffalo Springfield')
    print(repr('\tBuffalo Springfield'))


#%%
# Test demonstrate_formatting()
demonstrate_formatting()


#%%

def demonstrate_fancy_formatting_with_f_strings():
    """Using f-strings in formatting.
    - format strings like f'Some text {some var}, more text {another var}...', etc.
    """

    name = 'Buffalo Springfield'
    lowest = 1
    highest = 10
    print(f'Hello, {name}, on the scale from {lowest} to {highest} you are {highest}!')


#%%
# Test demonstrate_fancy_formatting_with_f_strings()
demonstrate_fancy_formatting_with_f_strings()

#%%


def demonstrate_string_operations():
    """Using different string operations.
    - endswith(), split(), center(), in (aka contains()), == (aka equals()), len(), ..., strip() (lstrip(), rstrip())
    """

    s = 'Buffalo Springfield'
    print(s.endswith('field'))
    print(s.split())
    print(s.center(20))
    print('Springfield' in s)
    print(s == 'Buffalo Springfield')
    print(len(s))
    s = '          Buffalo Springfield      '
    print(s.strip())
    print(s.rstrip())
    print(repr(s.lstrip()))


#%%
# Test demonstrate_string_operations()
demonstrate_string_operations()
