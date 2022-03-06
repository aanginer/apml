import scripts.utils.gdpy
import scripts.utils.hook7

app = gdpy.gd

def code():
    print("hi")

hook7.hook(app)
hook7.run(code)
