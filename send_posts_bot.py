from pprint import pprint
from re import M
from tkinter.messagebox import NO
import telepot
from pathlib import Path
import urllib.request as urllib2
 
def main():

    bot = telepot.Bot('5368170502:AAF0PWez1Jyg713jReowJ1RcQA7Yn7XwQjk')
    path = Path('/home/riser/Downloads/Uchkuch/result_htmls')
    files = [i for i in path.iterdir() if i.is_file() and i.suffix== '.png']
    files.sort()
    # files = sorted(files)
    pprint(files)
    # quit()

    num = 1
    tmp = None
    
    curr_price = 0
    prev_price = 0

    prices = []
    flag = -1
    min_price = None
    min_date = None

    lines = []
    with open('urls_for_bot.txt', 'r') as urls_file:

        for line in urls_file:
            lines.append(line)

    for file in files:



        tmp = num

        num = int(file.as_posix().split()[0].split('/')[-1])

        if min_price is not None and tmp != num:
            bot.sendMessage('643096181', f"Дата - {min_date}\nСамый дешёвый вариат - {min_price} ₽\n")
            print('Helllo')
            min_price = None



        price = int(file.as_posix().split('|')[1].split()[0].strip())
        date = file.as_posix().split('/')[-1].split('|')[0]

        if min_price is None:
            min_price = price
            min_date = date
        elif min_price > price:
            min_price = price
            min_date = date

        print(file.as_posix())

        if tmp is None or tmp != num:
            if flag == -1:
                flag = 0
            num = int(file.as_posix().split()[0].split('/')[-1])
            print('send--->', file.as_posix())
            bot.sendMessage('643096181', file.as_posix().split('/')[-1])

        bot.sendPhoto('643096181', photo=open(file.as_posix(), 'rb'))
            
        for line in lines:
            png_file = line.split('>>><<<')[0]
            if png_file == file.as_posix():
                print('~~~~~~~~~~~~~~~hello~~~~~~url')

                fetcher = urllib2.urlopen(
                    'https://clck.ru/--?url='+
                    line.split('>>><<<')[1])
                
                bot.sendMessage('643096181', line.split('>>><<<')[1])




                    

if __name__ == '__main__':
    main()