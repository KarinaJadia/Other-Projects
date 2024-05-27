class box:
    def __init__(self, x, y, pc, c, id, pos):
        self.x = x
        self.y = y
        self.passive_color = pc
        self.color = c
        self.active = False
        self.id = id
        self.position = pos
        self.text = ''