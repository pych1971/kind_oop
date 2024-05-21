class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, mem_slots, total_mem_slots=4):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = total_mem_slots
        self.mem_slots = mem_slots

    def get_config(self):
        config = [f'Материнская плата: {self.name}', f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
                  f'Слотов памяти: {self.total_mem_slots}']
        memory = 'Память: '
        for i in self.mem_slots:
            memory += f'{i.name} - {i.volume}; '
        memory = memory[:-2]
        config.append(memory)
        return config


proc = CPU('Intel', 1000)
mem1 = Memory('Hynix', 3333)
mem2 = Memory('Hynix', 3333)
mb = MotherBoard('MSI', proc, [mem1, mem2])
# print(mb.get_config())
