from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium import webdriver
import requests, io, pdb, pdb, time


def InstanceApi(users, driver):
    list_req = list()
    for user in users:
        req = requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={user}')
        content = req.json
        content_instance = content()
        users_unique = content_instance['users']
        for user in users_unique:
            print(user['user']['username'])
            follow(user['user']['username'], 'https://instagram.com', driver)

def follow(user, url_base, driver):
    get = driver.get(f'{url_base}/{user}')
    try:    
        time.sleep(1)
        btn_follow = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/div/div/span/span[1]/button')
        btn_follow.send_keys(Keys.ENTER)
    except Exception as err:
        print('[------------ERRO--------------]')
        print('Houve um erro ao seguir',err)
        print('[------------ERRO--------------]')
        pass