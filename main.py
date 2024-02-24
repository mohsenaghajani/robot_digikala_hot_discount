from answer_question import final_answer
from concurrent.futures import ThreadPoolExecutor
from headers import header_final
from get_config import get_id
from send_answer_get_gift import send_answer, thread_for_gift
from calculator import calculate_captcha


def thread_for_answer(url_id, item_id, captcha_question):
    executor = ThreadPoolExecutor(max_workers=15)
    try:
        for header in header_final:
            # in final_header we have a list of dicts and to dicts we have header with
            # some header with different cookie and default answer for each user
            # ( if question is how many scale in image this answers help us  )

            answer = final_answer(header['answer'], captcha_question)
            executor.submit(send_answer, header['header'], url_id, answer, item_id)
            # executor.shutdown()
    except:
        print('we have problem in thread')
    executor.shutdown()


if __name__ == '__main__':
    url_id, item_id, captcha_question = get_id()
    thread_for_answer(url_id, item_id, captcha_question)
    # if  answers are wrong do this for enter answer from user
    # (for example when question is sum of two number or three number)
    # question is shown in chrome
    user_answer = calculate_captcha()
    thread_for_gift(url_id, user_answer, item_id)