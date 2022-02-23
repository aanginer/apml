from apml.ccu import cm
def ccu(t):
    for i in range(int(t)):
        i+=1
        cm.cmd(input(''),i)
