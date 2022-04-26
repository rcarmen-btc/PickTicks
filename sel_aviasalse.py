# import pandas as pd
import re
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from tkinter import Tk
from generate_post import replace_all


def parse_whole_info(first_info='', second_info='', url_to_ticket='', price_text='', ticket_iter=0):

    sp_first_info = [el.strip() for el in first_info.strip().split('\n')]

    print(sp_first_info)

    sp_second_info = [el.strip() for el in second_info.strip().split('\n')]
    print(sp_second_info)


    if sp_second_info[sp_second_info.index('Ручная кладь') + 2] !='Сдаваемый багаж': 
        hb = sp_second_info[sp_second_info.index('Ручная кладь') + 1] # + sp_second_info[sp_second_info.index('Ручная кладь') + 2] 
    else: 
        hb = 'включена'

    if sp_second_info[sp_second_info.index('Сдаваемый багаж') + 1] !='1 место': 
        gb = sp_second_info[sp_second_info.index('Сдаваемый багаж') + 1] # + sp_second_info[sp_second_info.index('Сдаваемый багаж') + 2] 
    else: 
        gb = 'включён'

    replace_dict = {
        '{{DOTS}}': sp_first_info[0],
        '{{TCODE}}': sp_second_info[1],
        '{{COMP}}': sp_first_info[2],
        '{{TIME_PLANE}}': sp_second_info[2],
        '{{FT}}': sp_first_info[5],
        '{{FCI}}': sp_first_info[7],
        '{{FDA}}': sp_first_info[6],
        '{{FAIR}}': sp_first_info[8] + sp_first_info[9],
        '{{LT}}': sp_first_info[10],
        '{{LCI}}': sp_first_info[12],
        '{{LDA}}': sp_first_info[11],
        '{{LAIR}}': sp_first_info[13] + sp_first_info[14],
        '{{HB}}': hb,
        '{{GB}}': gb,
        '{{PRICE}}': price_text,
    }

    print(replace_dict)

    templates_dict = {
        'Уральские авиалинии': 'TemplatePostUral.html',
        'Аэрофлот': 'TemplatePostFlot.html',
        'Avia Traffic Company': 'TemplatePostTraf.html',
        'S7 Airlines': 'TemplatePostS7.html',
    }

    use_template = 'templates/' + templates_dict.get(replace_dict['{{COMP}}'], 'TemplatePost.html')

    replace_all(use_template, replace_dict, f'result_htmls/{replace_dict["{{PRICE}}"]} | {replace_dict["{{DOTS}}"]}-{replace_dict["{{FDA}}"]}-{replace_dict["{{COMP}}"]}.html', url_to_ticket, ticket_iter)


def main(leave_city, leave_date, come_city, passengers_count):

    tick_iter = 0
    # tkinter
    root = Tk()
    root.withdraw()

    # --- Load webdriver ---
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # --- Filters ---
    # leave_city = 'MOW'
    # leave_date = '0107' #DDMM
    # come_city = 'OSS'

    # leave_city = 'OSS'
    # leave_date = '0507' #DDMM
    # come_city = 'MOW'
    # passengers_count = '1'

    search_url = f'https://www.aviasales.ru/search/{leave_city}{leave_date}{come_city}{passengers_count}?payment_method=all'

    # --- Define actions --- 
    actions = ActionChains(driver)
    driver.get(search_url)
    time.sleep(6)

    # --- Click cookie button ---
    driver.find_element(By.CLASS_NAME, 'j6SdG_CNzTHR3lNJdcfl').find_element(By.TAG_NAME, 'button').click()

    # --- Side filters actions ---
    bag_checkbox = driver.find_element(By.XPATH, "//*[contains(text(), 'Багаж')]")
    actions = ActionChains(driver)
    bag_checkbox.click()
    driver.find_element(By.XPATH, "//*[contains(text(), 'Багаж включён')]").click()
    driver.find_element(By.XPATH, "//*[contains(text(), 'Без пересадок')]").click()
    time.sleep(2)

    # --- Find product list and itarete ---
    data = driver.find_elements(By.XPATH, "//div[@class='product-list__item fade-appear-done fade-enter-done']")
    data += [i for i in driver.find_elements(By.XPATH, "//div[@class='product-list__item fade-enter-done']") if i not in data]

    for d in data:
        print('I am here ------->')
        try:
            # --- Click select ticket ---
            actions.move_to_element(d)
            time.sleep(1)
            tmp = d.find_element(By.TAG_NAME, 'button')
            tmp.click()
        except:
            print('<<<SKIP>>>')
            print(d.text)
            print('<<<SKIP>>>')
            continue
        time.sleep(2)

        # Coast of ticket
        price_text = driver.find_element(By.XPATH, "//span[@class='price_5dd3743 price-info__text']").text

        # Save url to ticket
        driver.find_element(By.XPATH, "//*[contains(text(), 'Поделиться')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@class='button_cbf386f inline_cbf386f button_63ea4da copyLink_63ea4da ticket-sharing-mobile__share-btn']").click()
        time.sleep(1)
        url_to_ticket = root.clipboard_get()
        driver.execute_script("window.history.go(-1)")
        time.sleep(1)


        # First info, city, time, airport and so on
        first_el = driver.find_element(By.CLASS_NAME, 'ticket-main-modal__segment')
        first_info = first_el.text
        print('----->First:', first_info)
        print('=============')

        # Second section with information
        first_el.find_element(By.TAG_NAME, 'button').click()
        time.sleep(2)

        # Second info, baggage
        # second_info = driver.find_element(By.XPATH, "//div[starts-with(@class, 'window')]")
        second_el = driver.find_element(By.XPATH, "//div[@class='window_c3549a2 root_46e46bc content_46e46bc ticket-modal-bg-grey']")
        second_info = second_el.text
        print('----->Second:', second_info)
        print('=============')

        # Go back
        driver.execute_script("window.history.go(-1)")
        driver.execute_script("window.history.go(-1)")
        time.sleep(1)
        
        parse_whole_info(first_info, second_info, url_to_ticket, price_text, tick_iter)
        tick_iter += 1
        
    driver.quit()

if __name__ == '__main__':
    month = '04'
    for i in range(27, 31):
        main('MOW', f'{str(i)}{month}', 'OSS')
    print('=======================================================')
    print('=======================SUCCSESS========================')
    print('=======================================================')
