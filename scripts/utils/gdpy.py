import scripts.utils.geometryDash as GD
import scripts.utils

gd = utils.exe('GeometryDash',1722)

class memory(object):
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.dead = False
    
    def respawn(self):
        GD.respawn()
