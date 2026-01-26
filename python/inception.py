"""The very first module in a more structured version of the project.
"""


#%%
# # Moving part of the code from main.py
# print('Buffalo Springfield')
# print('Buffalo Springfield' + ' Again')
# print(__name__)
#
#
# #%%
# # Printing with ' ' and printing without '\n'
# print('Buffalo Springfield', 'Again', end='; ')
# print(1967)


#%%
# A simple function and function call
def bs():
    """Prints the band name."""
    bs = input('Band name: ')
    print(bs)


# #%%
# # Printing docstrings
# print(bs.__doc__)
#
# #%%
# # break and continue
# for i in range(5):
#     if i == 3:
#         break
#     print(i)
#
# #%%
# # Importing from Standard Library
#
# # Date format strings
# # https://docs.python.org/3/library/datetime.html?highlight=date%20format%20strings#strftime-and-strptime-format-codes
#
# from datetime import date
# print(date.today())
# print(date.today().strftime('%B %d, %Y'))
# print(date(1966, 4, 11).strftime('%b %d, %Y'))
#
# #%%
# # Testing print(__file__)
#

#%%
# Taking care of the module __name__
if __name__ == '__main__':
    print('Buffalo Springfield')
    print('Buffalo Springfield' + ' Again')
    print()

    bs()
