from scripts import utils

def hook(hooker: utils.client):
    global hooked
    if hooker == 'hook7.client;1722':
        hooked = True


def respawn():
    print("respawn")

def run(func):
    func()
