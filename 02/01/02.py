class Money:
    def __init__(self, money):
        self.__money = money

    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money

    def get_money(self):
        return self.__money

    def add_money(self, mn):
        self.__money += mn.__money

    @staticmethod
    def __check_money(money):
        return type(money) is int and money >= 0
