from sel_aviasalse import main as upload_ticks
from html_to_png import main as handle_png
from send_posts_bot import main as send_to_me


def main():
    
    upload_ticks()
    handle_png()
    send_to_me()


if __name__ == '__main__':
    main()