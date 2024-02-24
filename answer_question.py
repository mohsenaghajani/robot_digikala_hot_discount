import re

# if  question is this 'count of scale in image plus some number ' this functions plus the default answer with number


def final_answer(user_answer, captcha_question):
    extra_q, op = question(captcha_question)
    answer = int(user_answer)
    if op == 0:
        final_answer = answer + extra_q
        print(final_answer)
        return final_answer
    elif op == 2:
        final_answer = answer * extra_q
        print(final_answer)
        return final_answer
    else:
        final_answer = answer - extra_q
        print(final_answer)
        return final_answer


def question(text):
    if 'منهای ' in text:
        operation = 1
    elif 'ضربدر' in text:
        operation = 2
    else:
        operation = 0
    # الگوی جدا کردن اعداد فارسی
    pattern = r'\d+'

    # جدا کردن اعداد
    numbers = re.findall(pattern, text)
    # تبدیل اعداد فارسی به اعداد انگلیسی
    if len(numbers) != 0:
        english_numbers = ["".join(farsi_to_english(num) for num in n) for n in numbers]
        print(english_numbers[0])
        return english_numbers[0], operation
    else:
        return 0


def farsi_to_english(number):
    persian_numbers = {
        '۰': '0', '۱': '1', '۲': '2', '۳': '3', '۴': '4', '۵': '5', '۶': '6', '۷': '7', '۸': '8', '۹': '9'
    }
    return persian_numbers.get(number, number)
