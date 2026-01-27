"""Demonstrates working with lists.
"""


#%%
def demonstrate_lists():
    """Using just the simplest operations with lists.
    - create a non-empty list with different kinds of elements
    - accessing/slicing a list
    - comparing 2 lists (== vs. is)
    - concatenating 2 lists (the + operator)
    - looping through a list
    """

    empty_list = []
    print(empty_list)
    print()

    buffalo_springfield = ['Buffalo Springfield', 1966, True, ]
    print(buffalo_springfield)
    print(buffalo_springfield[0])
    print(buffalo_springfield[1:])
    print()

    bs = buffalo_springfield[:]
    print(bs == buffalo_springfield)
    print(bs is buffalo_springfield)
    print()

    print(['Buffalo Sprinfield'] + buffalo_springfield[1:])
    print()

    for m in buffalo_springfield:
        print(m)

#%%
# Test demonstrate_lists()
demonstrate_lists()

#%%
def demonstrate_list_methods():
    """Using
    append()
    insert()
    remove()
    pop()
    extend()
    count()
    index()
    reverse()
    len()
    ...
    Also, "in" and "not in" operators can be used to search lists
    for the occurrence of a given element.
    """

    buffalo_springfield = ['Buffalo Springfield', 1966, True, ]
    buffalo_springfield.append('Broken Arrow')
    print(buffalo_springfield)
    buffalo_springfield.insert(1, 'LA')
    print(buffalo_springfield)
    buffalo_springfield.remove('LA')
    print(buffalo_springfield)
    buffalo_springfield.pop()
    print(buffalo_springfield)
    buffalo_springfield.extend(['LA', 1968])
    print(buffalo_springfield)
    print(buffalo_springfield.count('Buffalo Springfield'))
    print(buffalo_springfield.index(1968))
    buffalo_springfield.reverse()
    print(buffalo_springfield)
    print(len(buffalo_springfield))
    print('Buffalo Springfield' in buffalo_springfield)
    print('New York' in buffalo_springfield)


#%%
# Test demonstrate_list_methods()
demonstrate_list_methods()

#%%


def populate_empty_list():
    """Creating an empty list and populating it with random values
    using random.seed() and random.randint()
    """
    from random import seed, randint
    seed(12)
    l = []

    for i in range(10):
        l.append(randint(1, 100))
    print(l)


#%%
# Test populate_empty_list()
populate_empty_list()

#%%


def duplicate_list():
    """Duplicating lists (carefully :)).
    Don't use l2 = l1, but either of the following:
    - l2 = l1.copy()
    - l2 = l1 + []
    - l2 = l1[:]
    """

    buffalo_springfield = ['Buffalo Springfield', 1966, True, ]
    l2 = buffalo_springfield.copy()
    print(l2)
    print(buffalo_springfield == l2)
    print(buffalo_springfield is l2)
    print()

    l2 = buffalo_springfield + []
    print(l2)
    print(buffalo_springfield == l2)
    print(buffalo_springfield is l2)
    print()

    l2 = buffalo_springfield[:]
    print(l2)
    print(buffalo_springfield == l2)
    print(buffalo_springfield is l2)
    print()


#%%
# Test duplicate_list()
duplicate_list()

#%%


def demonstrate_list_comprehension():
    """Showing examples of list comprehension.
    - list comprehension over a list of strings
    - list comprehension with enumerate(), to find indices of all occurrences of an element in a list
    Using str() and join() in printing results.
    """

    songs = ['Sad Memory', 'Uno Mundo', 'Round and Round and Round', 'For What It\'s Worth', ]
    first_words = [title.split()[0] for title in songs]
    print(first_words)
    print(''.join([w[0] for w in first_words]).capitalize())
    print()

    print(''.join([title.split()[0][0] for title in songs]).capitalize())
    print()

    songs = ['Sad Memory', 'Uno Mundo', 'Round and Round and Round', 'For What It\'s Worth',
             'Round and Round and Round', 'For What It\'s Worth', ]
    print(', '.join([title for title in songs if not songs.count(title) > 1]))
    print(', '.join([title for title in set(songs)]))
    print(', '.join([str(i) for i, j in enumerate(songs) if songs.count(j) > 1]))



#%%
# Test demonstrate_list_comprehension()
demonstrate_list_comprehension()

