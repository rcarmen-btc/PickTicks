
p = '9 191 ₽'
p = p.split()
print(int(p[0] + p[1]) + 700)



with open('urls_for_bot.txt', 'r') as urls_file:
    for i in urls_file:
        print(i)