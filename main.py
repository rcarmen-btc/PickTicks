from sel_aviasalse import main as upload_ticks
from html_to_png import main as handle_png
from send_posts_bot import main as send_to_me


def main():
    
    # month = '04'
    # for i in range(27, 31):
    #     print(i)
    #     upload_ticks('MOW', f'{str(i)}{month}', 'OSS', 1)

    month = '05'
    for i in range(1, 10):
        print(i)
        upload_ticks('MOW', f'0{str(i)}{month}', 'OSS', 1)

    # for i in range(10, 11):
    #     print(i)
    #     upload_ticks('MOW', f'{str(i)}{month}', 'OSS', 1)

    handle_png()

    send_to_me()


if __name__ == '__main__':
    main()