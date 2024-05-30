import string
import random


class EmailValidator:
    symbols = string.ascii_letters + string.digits + '_' + '.'

    def __new__(cls):
        return None

    @classmethod
    def get_random_email(cls):
        email = ''
        for i in range(10):
            email += random.choice(cls.symbols)
        return email + '@gmail.com'

    @classmethod
    def check_email(cls, email):
        if not EmailValidator.__is_email_str(email):
            return False
        split_email = email.split('@')
        return (all(i in cls.symbols + '@' for i in email) and len(split_email) == 2) and (
                len(split_email[0]) <= 100) and (len(split_email[1]) <= 50) and ('.' in split_email[1]) and (
                '..' not in email)

    @staticmethod
    def __is_email_str(email):
        return isinstance(email, str)


assert EmailValidator.check_email("sc_lib@list.ru") == True and EmailValidator.check_email(
    "sc_lib@list_ru") == False and EmailValidator.check_email("sc@lib@list_ru") == False and EmailValidator.check_email(
    "sc.lib@list_ru") == False and EmailValidator.check_email("sclib@list.ru") == True and EmailValidator.check_email(
    "sc.lib@listru") == False and EmailValidator.check_email(
    "sc..lib@list.ru") == False, "метод check_email отработал некорректно"

m = EmailValidator.get_random_email()
assert EmailValidator.check_email(
    m) == True, "метод check_email забраковал сгенерированный email методом get_random_email"

assert EmailValidator() is None, "при создании объекта класса EmailValidator возвратилось значение отличное от None"

assert EmailValidator._EmailValidator__is_email_str('abc'), "метод __is_email_str() вернул False для строки"
