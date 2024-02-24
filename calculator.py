import ast


def calculate_captcha():
    while True:
        expression = input("enter numbers : ")
        try:
            parsed_expression = ast.parse(expression, mode='eval')
            result = eval(compile(parsed_expression, '<string>', 'eval'))
            print("result :", result)
            return result
        except:
            print("input is invalid try again!")