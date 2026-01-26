"""The very first Python script - main.py.
"""
from blankscripts.functionsblank import buffalo_springfield

#%%
# # Hello world: the print() built-in function and the + operator.
# print('Buffalo Springfield')
# print('Buffalo Springfield' + ' Again')
# print('Buffalo Springfield', 'Again')
#
#
# #%%
# # The input() built-in function
# bs = input('Band name: ')
# print(bs)
#
#
# #%%
# # A simple function and function call
# def bs():
#     bs = input('Band name: ')
#     print(bs)
#
# bs()
#
#
# #%%
# # A simple loop and the range() built-in function
# for i in range(5):
#     print(i)
#
#
# #%%
# # A simple list, accessing list elements, printing lists
# buffalo_springfield = ['Neil Young', 'Stephen Stills', 'Bruce Palmer', 'Dewey Martin', 'Richie Furay']
# print(buffalo_springfield)
# print(buffalo_springfield[1])
#
#
# #%%
# # Looping through list elements - for and enumerate()
# for m in buffalo_springfield:
#     print(m)
# print()
#
# for i in range(len(buffalo_springfield)):
#     print(buffalo_springfield[i])
# print()
#
# for i, m in enumerate(buffalo_springfield):
#     # print(i+1, m)
#     print(str(i+1) + ':', m)
#
#
# #%%
# # Global variables: __name__, __file__, __doc__,...
# print(__name__)
# print(__file__)     # works only with running the entire script from Run, not with Run Cell
# print(__doc__)      # works correctly only with running the entire script from Run, not with Run Cell

#%%
# Importing from another script
from inception import bs            # works only with running the entire script from Run, not with Run Cell;
                                    # prints None first, because the value of from ... import ... is None
bs()
