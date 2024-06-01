class box:
    def __init__(self, x, y, pc, c, id, pos):
        self.x = x
        self.y = y
        self.passive_color = pc
        self.color = c
        self.active = False
        self.id = id
        self.pointer = pos
        self.text = ''
        self.solved = False
    
    def __str__(self): # print magic method
        return f'box {self.id} ({self.pointer}) - solved status [{self.solved}]'