
p = '9 191 ₽'
p = p.split()
print(int(p[0] + p[1]) + 700)



with open('urls_for_bot.txt', 'r') as urls_file:
    for i in urls_file:
        print(i)

import pyshorteners as sh

print(sh.Shortener().tinyurl.short('https://medium.com/analytics-vidhya/create-url-shortner-with-python-50129714f044'))

from tkinter import Tk

root = Tk()
root.withdraw()

print(root.clipboard_get())