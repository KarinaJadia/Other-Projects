class box:
    def __init__(self, x, y, pc, c, id, pos):
        self.x = x
        self.y = y
        self.passive_color = pc
        self.color = c
        self.active = False
        self.id = id
        self.row = pos // 9 + 1
        self.col = pos % 9 + 1
        self.pointer = pos
        self.text = ''
        self.solved = False
        self.possibles = [1,2,3,4,5,6,7,8,9]
    
    def __str__(self): # print magic method
        return f'box {self.id} ({self.pointer}) - solved status [{self.solved}]'