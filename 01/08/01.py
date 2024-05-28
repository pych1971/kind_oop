class Server:
    ip = 0

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls.ip += 1
        setattr(instance, 'ip', cls.ip)
        return instance

    def __init__(self):
        self.buffer = []
        self.link = False

    def send_data(self, data):
        if self.link:
            self.link.buffer.append(data)

    def get_data(self):
        out = self.buffer[:]
        self.buffer.clear()
        return out

    def get_ip(self):
        return self.ip


class Router:
    def __init__(self):
        self.buffer = []
        self.servers = {}

    def link(self, server):
        self.servers[server] = True
        server.link = self

    def unlink(self, server):
        self.servers[server] = False
        server.link = False

    def send_data(self):
        for i in self.buffer:
            for j in self.servers.keys():
                if i.ip == j.ip and self.servers[j]:
                    j.buffer.append(i)
                    break
        self.buffer.clear()


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
