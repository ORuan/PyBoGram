from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium import webdriver
from config import configuration
import requests, time, getpass
from requests_api import InstanceApi
import io, pdb

driver = configuration()

url_base = 'https://instagram.com'
driver.get(url_base)

time.sleep(4)

def input_credencials():
    perfil = input('Digite o perfil do insta:')
    password = getpass.getpass('Digite a senha do perfil:')
    return perfil, password
    
def save_credencials():
    with io.open('credencials/pass.txt', 'w') as passwd:
        passwd.write(str(getpass.getpass('Digite a senha a ser salva: ')))
        
    with io.open('credencials/username.txt', 'w') as username:
        username.write(input('Digite o seu username: '))

    passwd, username = read_credencial()
    return passwd.decode(), username.decode()


def read_credencial():
    with io.open('credencials/pass.txt', 'rb') as pass_file:
        password = pass_file.readline()
    with io.open('credencials/username.txt', 'rb') as user_file:
        perfil = user_file.readline()
    return perfil, password

def options():
    try:
        choose = int(input(
            '''
            1 - Save and use credencials
            2 - Use inputs
            3 - Use credencials saved
            '''
        ))
        if choose != 1 and choose != 2 and choose != 3:
            print('A escolha não é permitida')
        elif choose == 1:
            return save_credencials()
        elif choose == 2:
            return input_credencials()
        elif choose == 3:
            return read_credencial()
    except Exception as err:
        print(f'Houve um erro na digitação: {err}')


instance = options()
username_input = driver.find_element_by_name('username')
username_input.send_keys(instance[0].decode())

password_input = driver.find_element_by_name('password')
password_input.send_keys(instance[1].decode())

btn = driver.find_element_by_css_selector('button[type="submit"]')
btn.send_keys(Keys.ENTER)

time.sleep(2)

InstanceApi(['ruan.pb','ruanz'], driver)

driver.quit()