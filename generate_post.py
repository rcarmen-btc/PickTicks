import sys
from pathlib import Path
import os

def replace_all(path_to_src_file: str, replace_dict: dict, res_path: str, url_to_ticket: str, ti: int, url: str):

    # path = Path('/home/riser/Downloads/Uchkuch/result_htmls')
    # files = [i.as_posix() + '.png' for i in path.iterdir() if i.is_file()]

    # png_file = os.path.splitext(res_path)[0]

    with open('urls_for_bot.txt', 'a') as file:
        file.write(f'{res_path}.png>>><<<{url}\n')

    with open('links.html', 'a') as li:
        if (ti == 0):
            li.write('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">')
        li.write(f"<li><a href='{res_path}'>{res_path}</a> | <a href='{url_to_ticket}'>Link to ticket</a></li> <br>")
    
    with open(path_to_src_file, 'r') as src:
        raw_data = src.read()

    for key, val in replace_dict.items():
        raw_data = raw_data.replace(key, val)
    
    src_file_name = path_to_src_file.split('/')[-1].split('.')[0]

    # res_dir = '/'.join(path_to_src_file.split('/')[:-1])
    # if len(res_dir) == 0:
    #     res_path = src_file_name + '.replace.html'
    # else:
    #     res_path = res_dir + '/' + src_file_name + '.replace.html'
    # print(src_file_name, res_dir, res_path)

    with open(res_path, 'w') as dest:
        dest.write(raw_data)
    
    


if __name__ == '__main__':
    
    replace_dict = {
        '{{COMP}}': 'S7 Ailinasdkfjasldkfjdsfasdlfkjsdklffes',
        '{{TIME_PLANE}}': '2',
        '{{FT}}': '3',
        '{{FCI}}': '4',
        '{{FDA}}': '5',
        '{{FAIR}}': '6',
        '{{LT}}': '7',
        '{{LCI}}': '8',
        '{{LDA}}': '9',
        '{{LAIR}}': '10',
        '{{HB}}': '11',
        '{{GB}}': '12',
        '{{PRICE}}': '13',
    }

    replace_all(sys.argv[1], replace_dict)
