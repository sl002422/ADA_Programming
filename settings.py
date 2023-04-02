"""Project configuration settings (PROJECT_DIR, format strings, etc.).
"""


from pathlib import Path

PREFERRED_DATE_FORMAT = '%b %d, %Y'

# Define PROJECT_DIR as Path(__file__).parent

PROJECT_DIR = Path(__file__).parent
# print(PROJECT_DIR)
DATA_DIR = PROJECT_DIR / 'data' # we give it directory with 'data' in it, but it's not exist yet, but it's just a
# PATH so nothing to complain on # here we can add segments to the path, the result is also a path object
# print(DATA_DIR)

# # Demonstrate __file__, type(__file__), Path(__file__), Path(__file__).parent and Path.cwd()
# print(__file__)
# print(Path(__file__))
# print(type(Path(__file__)))
# f = Path(__file__)
# print(f.parent)
# print(Path(__file__).parent)
