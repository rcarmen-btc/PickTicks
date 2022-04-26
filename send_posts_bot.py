import telepot
from pathlib import Path
import sys


def main():

    bot = telepot.Bot('5368170502:AAF0PWez1Jyg713jReowJ1RcQA7Yn7XwQjk')
    path = Path('/home/riser/Downloads/Uchkuch/result_htmls')
    files = [i for i in path.iterdir() if i.is_file() and i.suffix== '.png']

    for file in files:
        bot.sendPhoto('643096181', photo=open(file.as_posix(), 'rb'))


if __name__ == '__main__':
    main()