from pathlib import Path

FILE_DIR = Path(__file__).parent


def get_file_dir():
    return FILE_DIR


def get_any_dir(any):
    return get_file_dir().parent / any


#                   ---


# Demonstrate creating and removing directories
# - new dir: <newDir> = <path> / '<subdir1>/<subdir2>/.../<subdirN>'
#            <newDir>.mkdir(parents=True, exist_ok=True)
# - remove dir: <dir>.rmdir()                                           # requires the <dir> to be empty
# - project dir: settings.PROJECT_DIR

# new_dir = get_file_dir() / 'bruh'
# new_dir_2 = Path.cwd() / 'bruh2'
# new_dir_3 = Path(__file__).parent / 'bruh3'
# print('NEW DIRS: ', new_dir, ' ', new_dir_2, ' ', new_dir_3)
# new_dir.mkdir(parents=True, exist_ok=True)
# new_dir.rmdir()
#                                 # removes only the "deepest" dir (d2)
# new_dir = Path.cwd() / 'bruh/d1'
# new_dir.mkdir(parents=True, exist_ok=True)
# new_dir.rmdir()                                  # removes only the "deepest" dir (d1)


# Writing to a text file - <outfile>.write(str(<obj>), <outfile>.writelines([str(<obj>)+'\n' for <obj> in <objs>])
# bands = [theBeatles, theRollingStones, pinkFloyd]
# file = get_project_dir() / 'data/bands.txt'
# with open(file, 'w') as f:
#     # for band in bands:
#     #     f.write(str(band) + '\n')
#     f.writelines([str(b) + '\n' for b in bands])
# print('Done')

# vianova = ['member_1', 'member_2']
# the_offspring = ['offspring_1', 'offspring_2']
# max_corzh = ['podkidish']
#
# bands = [vianova, the_offspring, max_corzh]
#
# file = get_file_dir() / '2deleteTXT/bands.txt'
# with open(file, 'w') as f:
#     for band in bands:
#         f.write(str(band) + '\n')
#     f.writelines([str(b) + '\n' for b in bands])
# print('Done')

# --------------

# def burger_wrapper(meals):
#     return ['bread above', meals, 'bread below']
#
# def choose_meals(meals):
#     return


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()

    return inner


@make_pretty
def ordinary():
    print("I am ordinary")


# ordinary()

# def burgered(func):
#     def inner(x):
#         print('bread')
#         func(x)
#         print('bread')
#     return inner
#
# @burgered
# def meals(x):
#     print(x)
#
# meals('ml')

# def smart_divide(func):
#     def inner(a, b):
#         print("I am going to divide", a, "and", b)
#         if b == 0:
#             print("Whoops! cannot divide")
#             return
#
#         return func(a, b)
#     return inner
#
# @smart_divide
# def divide(a, b):
#     print(a/b)
#
# divide(2,5)
# divide(2,0)

# def universal_ramo4ka(self):
#     def inner(*args):
#         print('----------------------')
#         self(*args)
#         print('----------------------')
#
#     return inner
#
#
# @universal_ramo4ka
# def brg(a, b, dct, ff=True):
#     print(a + b, ff)
#     [print(dct[i]) for i in dct]
#
#
# brg(4, 5, {'max': 'l', 'tom': 's'})


class Musician:
    def __init__(self, name, is_band_member=True):
        self.name = name
        self.is_band_member = is_band_member
        self.__immutable_property = 'I am not immutable'

    def __str__(self):
        b = 'band member' if self.is_band_member else 'solo musician'
        return f'{self.name}, {b}'

    def __eq__(self, other):
        ii = isinstance(other, Musician)
        a = self.name == other.name if ii else False
        b = self.is_band_member == other.is_band_member if ii else False
        return ii and a and b
        # return isinstance(other, Musician) and self.name == other.name and self.is_band_member == other.is_band_member

    @property  # getter
    def name(self):
        return self.__name

    @name.setter  # setter
    def name(self, name):
        self.__name = name if isinstance(name, str) else 'unknown type of [other] object (not string)'

    @property  # Add an immutable property (no setter for it)
    def immutable_property(self):
        return self.__immutable_property

    def play(self, song_title, *args, **kwargs):
        n = self.name
        s = f'"{song_title}"'
        r = kwargs['rhythm_count'] if 'rhythm_count' in kwargs.keys() else ''
        g = ' '.join([a for a in args]) if args else ''
        m = ' '.join([v for v in list(kwargs.values())[1:]]) if list(kwargs.values())[1:] else ''

        return f'{n} playing {s}: {r} ...playing... {g} {m}'

    def play_song(self, song_title, *args, **kwargs):
        return self.play(song_title, *args, **kwargs)

    @classmethod
    def from_str(cls, musician_string):
        # b = '(band member)' if self.is_band_member else '(solo musician)'
        # return f'{self.name} {b}'
        n = musician_string.split(' (')[0]
        bm = True if musician_string.split(' (')[1].startswith('b') else False
        return cls(n, bm)


george = Musician('George Harrison', True)


# print(george._Musician__name)
#
# george.city = 'Liverpool'
# print(george.city)
# george.__setattr__('test_attr', 1337)
# print(george.__getattribute__('test_attr'))
# setattr(george, 'newone', 1488)
# print(getattr(george, 'newone'))

# print(george.play_song('Don\'t Bother Me', 'Thank you!', 'Thanks!', rhythm_count='One, two, three, four!', great='Great!'))

class Singer(Musician):
    def __init__(self, vocals=Vocals.LEAD_VOCALS, **kwargs):
        super().__init__(**kwargs)
        self.vocals = vocals if isinstance(vocals, Vocals) else None

    def __str__(self):
        v = f', {self.vocals.value}' if isinstance(self.vocals, Vocals) else ''
        return super().__str__() + v























