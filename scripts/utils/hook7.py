import scripts.utils.geometryDash as gd
import scripts.utils as utils

hooked = False

client = utils.client("hook7",1722,"dumbthing.py","hook7.py.git")

def hook(app: utils.exe):
    global hooked
    if app == "GeometryDash.exe at 1722":
        gd.hook(client)
        hooked = app

def run(func: function):
    if hooked!=False:
        hooked.run(func())
