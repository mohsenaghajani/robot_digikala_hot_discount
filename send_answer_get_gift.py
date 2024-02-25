from concurrent.futures import ThreadPoolExecutor
import requests
from headers import header_correct


def get_gift(url_id, header, id):
    product_id = {"item_id": id}
    url = f'https://api.digikala.com/v1/hot-discount-assign/{url_id}/'
    response = requests.post(url, headers=header, json=product_id)
    get_status = response.json()
    init_url = 'https://api.digikala.com/v1/user/init/'
    get_user_winner = requests.get(init_url, headers=header)
    print(get_status['data'])
    user = get_user_winner.json()
    print(user['data']['user'])


def send_answer(header, url_id, answer, id):
    answer1 = {'answer': answer}
    response = requests.post(f'https://api.digikala.com/v1/hot-discount-captcha/{url_id}/',
                             json=answer1,
                             headers=header)
    check_answer = response.json()
    if check_answer['status'] == 200:
        if check_answer['data']['is_correct'] is True:
            print(f'answer = {answer}')
            thread_for_gift(url_id, header, id, answer)
    else:
        print(check_answer['message'])


def thread_for_gift(url_id, answer, items_id, product_num=0):
    count = product_num
    executor = ThreadPoolExecutor(max_workers=15)
    try:
        for header in header_correct:
            executor.submit(send_correct_answer, header['header'], url_id, items_id[count]['id'], answer)

    except:
        print('we have problem in thread')
    executor.shutdown()


def send_correct_answer(header, url_id, product_id, answer):
    answer1 = {'answer': answer}
    response = requests.post(f'https://api.digikala.com/v1/hot-discount-captcha/{url_id}/',
                             json=answer1,
                             headers=header)
    check_answer = response.json()
    if check_answer['status'] == 200:
        if check_answer['data']['is_correct'] is True:
            print(f'answer = {answer}')
            get_gift(url_id, header, product_id)
    else:
        print(check_answer['message'])
