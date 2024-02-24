from random import randrange
import requests
import webbrowser
from headers import headers

chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'


def get_headers():
    return headers[randrange(0, 5)]


def show_captcha_question(data):
    try:
        if 'captcha_data' in data['data']:
            print(data['data']['captcha_data']['captcha_question'])
            print(data['data']['captcha_data']['captcha_image']['url'])
            url_image = data['data']['captcha_data']['captcha_image']['url']
            # show image in chrome for when the question is Mathematical equation
            webbrowser.get(chrome_path).open(url_image)
            return
    except:
        print('we have problem image could not download')


def get_id():
    while True:
        url = 'https://api.digikala.com/v1/hot-discount/'
        response = requests.get(url, headers=get_headers())
        data = response.json()
        if data['status'] == 200:
            if 'id' in data['data']['active_hot_discount']:
                show_captcha_question(data)
                item_id = data['data']['active_hot_discount']['items']
                url_id = data['data']['active_hot_discount']['id']
                captcha_question = data['data']['captcha_data']['captcha_question']
                return url_id, item_id, captcha_question
            else:
                print('id has not found')
        else:
            print(data)
