from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        res = ''
        for i in number:
            if i in digits:
                res += 'X'
            else:
                res += i
        return res == 'XXXX-XXXX-XXXX-XXXX'

    @classmethod
    def check_name(cls, name):
        return all(i in cls.CHARS_FOR_NAME + ' ' for i in name) and len(name.split()) == 2
