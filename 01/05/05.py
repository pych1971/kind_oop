# здесь объявляются все необходимые классы
class Graph:
    def __init__(self, data, is_show=True):
        self.data = data[:]
        self.is_show = is_show

    def set_data(self, data):
        self.data = data

    def show_table(self):
        if not self.is_show:
            print('Отображение данных закрыто')
        else:
            print(*self.data)

    def show_graph(self):
        if not self.is_show:
            print('Отображение данных закрыто')
        else:
            print('Графическое отображение данных:', *self.data)

    def show_bar(self):
        if not self.is_show:
            print('Отображение данных закрыто')
        else:
            print('Столбчатая диаграмма:', *self.data)

    def set_show(self, fl_show):
        self.is_show = fl_show


# считывание списка из входного потока (эту строку не менять)
data_graph = list(map(int, input().split()))

# здесь создаются объекты классов и вызываются нужные методы
gr = Graph(data_graph)
# gr.show_table()
gr.show_bar()
gr.set_show(False)
gr.show_table()
