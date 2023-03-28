"""Demonstrates details of writing Python functions: annotations, default args, kwargs.
"""


#%%
# Setup / Data
song = 'Here Comes the Sun'
year = 1969

john = 'John Lennon'
paul = 'Paul McCartney'
george = 'George Harrison'
ringo = 'Ringo Starr'
the_beatles = [john, paul, george, ringo]

j = the_beatles.pop(0)
j, p, g, *the_beatles
print(j)

# j, *the_beatles = [john, paul, george, ringo] # такая конструкция значит, что john = 'john', the_beatles = [john, paul, george, ringo]
#
# j = john
# print(*the_beatles)
#j, p, g, r = the_beatles #
# j, p, g, r, *the_beatles = [john, paul, george, ringo]
# j, p, g, *the_beatles
# print(j, p, g, r)
#%%
def demonstrate_annotations(title: str, year: int) -> str:
    """Demonstrates how to use annotations of
    function parameters/arguments (<arg>: <type>) and of function return type (def f(...) -> <type>:).
    - print the function parameters/arguments
    - print the value of the __annotations__ attribute of this function
    - print the name and the docstring of this function
    - return a formatted string (including function parameters/arguments)
    """
    print(title + ', ' + str(year))
    print(demonstrate_annotations.__annotations__)
    print(demonstrate_annotations.__doc__)
    return f'{demonstrate_annotations.__name__}(\'{title}\',{year}))'

#%%
# Test demonstrate_annotations(title, year)
print(demonstrate_annotations(song, year))


#%%
# def show_song(title, author='George Harrison', year: int = 1969):
def show_song(title, author='George Harrison', year=1969): # positional arguments (without default) must be in the beginning

    """Demonstrates default arguments/parameters.
    - print locals()
    - print the function arguments/parameters in one line
    """

    print(locals())


#%%
# Test show_song(title, author='George Harrison', year=1969)
show_song(song)# we'll have 3 values in output because we have default values in this function
show_song(song, 'GH')
show_song(song, year = 1970)
show_song('Jones', year = 2023, author = 'vianova')
show_song(year = 2023, author = 'vianova', title = 'Jones')


#%%
def use_flexible_arg_list(band: str, *members): # * means we can include 0 or more arguments
    """Demonstrates flexible number of arguments/parameters.
    - print the type of the 'members' argument
    - print the band name and the list of band members in one line
    """

    print(type(members))
    b = band + ':' if members else band
    print(f'{b}: {", ".join([m for m in members])}')

#%%
# Test use_flexible_arg_list(band: str, *members)

use_flexible_arg_list('The Beatles', *the_beatles) # * means the list will be unpacked, and puts them in order to the function
#use_flexible_arg_list('The Beatles')


#%%
def use_all_categories_of_args(band, *members, is_active=True, **details):
    """Demonstrates positional args, flexible args, keyword args, and kwargs (flexible keyword args).
    - print the type of the 'details' argument
    - print all arguments/parameters, including the keyword arguments/parameters, in one line
    """
    #print(type(details))

    b = band + ':' if members else band
    m = ", ".join([m for m in members])
    a = '(active)' if is_active else '(not active)'
    d = ', '.join([str(k) + ': ' + str(v) for k, v in details.items()])
    return f'{b}{m}{a}{d}'

#%%
# Test use_all_categories_of_args(band, *members, is_active=True, **details)
print(use_all_categories_of_args('The Beatles', is_active=False, start=1962, end=1970))
# use_all_categories_of_args('The Beatles', *the_beatles, is_active=False, start=1962, end=1970)
#%%
