from sel_aviasalse import main as upload_ticks
from html_to_png import main as handle_png
from send_posts_bot import main as send_to_me
import requests
import json
import telepot


def no_api():

    # month = '05'
    # for i in range(1, 10):
    #     print(i)
    #     upload_ticks('MOW', f'0{str(i)}{month}', 'OSS', 1)

    # for i in range(10, 32):
    #     print(i)
    #     upload_ticks('MOW', f'{str(i)}{month}', 'OSS', 1)

    handle_png()

    send_to_me()

def api(depart_date, return_date, origin, destination):
    
    url = "https://api.travelpayouts.com/v1/prices/calendar"

    querystring = {"depart_date": depart_date, "return_date": return_date, "origin": origin, "destination": destination, "calendar_type": "departure_date"}

    headers = {'x-access-token': '74e374ffbb7e61ea2155743ac6ca4e64'}

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)

    return data


def main():
    
    bot = telepot.Bot('5368170502:AAF0PWez1Jyg713jReowJ1RcQA7Yn7XwQjk')
    # no_api()

    data = api('2022-05-14', '2022-05-20', 'MOW', 'OSS')

    bot.sendMessage('643096181', f'{data}')


if __name__ == '__main__':
    main()
