import scripts.utils.geometryDash as gd
class client(object):
    def __init__(self,name,id,location,module):
        self.name = str(name) + '.client'
        self.id = id
        self.location = location
        self.module = module
    def __repr__(self):
        return f"{self.name};{self.id}"

    def client(self):
        return self.name

class exe(object):
    def __init__(self,name,id):
        self.name = name
        self.id = id
    
    def __repr__(self):
        return f"{self.name}.exe at {self.id}"

    def run(self,func):
        if self.id == 1722:
            gd.run(func())
