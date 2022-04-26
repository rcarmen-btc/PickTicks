import sys


def replace_all(path_to_src_file: str, replace_dict: dict, res_path: str, url_to_ticket: str):

    with open('links.html', 'a') as li:
        li.write(f"<a href='{res_path}'>{res_path}</a> | <a href='{url_to_ticket}'>Link to ticket</a>")
    
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
