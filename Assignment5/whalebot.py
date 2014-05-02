from random import randint
from time import sleep
from common import Model
################### CONTROLLER #############################
def get_x(box):
    x, y, w, h = box
    return x
def get_y(box):
    x, y, w, h = box
    return y

class Controller():
    def __init__(self, m):
        self.m = m
    
    def poll(self):
        cmd = None
        self.target = model.pellets[1]
        x = get_x(self.target)
        y = get_y(self.target)
        b = self.m.mybox
        myx = b[0]
        myy = b[1]
        if x < myx:
            cmd = 'left'
        elif x > myx:
            cmd = 'right'
        elif x == myx:
            if y < myy:
                cmd = 'up'
            elif y > myy:
                cmd = 'down'
        if cmd:
            self.m.do_cmd(cmd)

################### VIEW #############################

class View():
    def __init__(self, m):
        self.m = m
        
    def display(self):
        b= self.m.mybox
        x = b[0]
        y = b[1]
        print "Position:" , x, ", " , y
    
################### LOOP #############################

model = Model()
c = Controller(model)
v = View(model)
frame=1
while not model.game_over:
    sleep(0.02)
    c.poll()
    model.update()
    if model.bot_ate_pellet == 1:
        model.bot_ate_pellet = 0
        print "The bot ate a pellet"
    if frame == 50:
        v.display()
        frame = 1
    else:
        frame = frame + 1