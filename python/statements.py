"""Demonstrates peculiarities of if, for, while and other statements.
"""


#%%
def demonstrate_branching():
    """Details and peculiarities of if statements.
    - is compares id()'s, == compares contents
    - id()'s are the same for equal strings and numbers, but not for lists, user class instances,...
    - the condition of an if-statement need not necessarily be a boolean
    - there can be more than one elif after if (no switch statement, use multiple elif instead)
    """

    x = 1
    if x == 1:
        print('x = 1')
    elif x == 2:
        print('x = 2')
    else:
        print('x is neither 1 nor 2')
    print()

    y = [1, 2, 3]
    # if y == [1, 2, 3]:
    if y is [1, 2, 3]:
        # print('y = [1, 2, 3]')
        print('y is [1, 2, 3]')
    else:
        print('y is not [1, 2, 3]')
    print()

    if 0.0:
        print(True)
    else:
        print(False)


#%%
# Test demonstrate_branching()
demonstrate_branching()

#%%


def demonstrate_loops():
    """Different kinds of loops. Also break and continue.
    - it is not necessary to iterate through all elements of an iterable
    - step in range()
    - unimportant counter (_)
    - break and continue
    - while loop
    """
    for i in range(10, 0, -1):
        print(i)
    print()
    for i in range(10, 0, -2):
        print(i)
    print()

    for i in range(10):
        if i == 5:
            break
            # continue
        print(i)
    print()

    i = 0
    while i < 5:
        print(i)
        i += 1
    print()

    for _ in range(5):
        print('Buffalo Springfield')

#%%
# Test demonstrate_loops()
demonstrate_loops()
