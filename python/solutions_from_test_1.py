#TASK 1
def check_palindrome(s: str) -> bool:
    alphabetic = ''.join([c.lower() for c in s if c.isalpha()])
    return alphabetic == ''.join(list(reversed(alphabetic)))

check_palindrome('Nurses, run!')

#TASK 2
from datetime import date

birthdays = {'John': date(1940,10,2),
             'Max': date(1945,10,2)}

while True:
    person = input()
    if person not in birthdays:
        print('not it')
    else:
        break
# -||-

#TASK 3
def review_album(reviewer: str, review: str, artist: str, title: str, *songs, score = 5, )
    ratings = {1:'Poor', 5: 'Great'}
    r= f'Review:\t {review}'
    # -||-