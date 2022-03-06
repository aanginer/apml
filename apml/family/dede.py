import time
from apml.family import baba
def v(thing):
	for aa in range(len(thing)):
		print(thing[aa])
def turkce(dede):
	return dede+'gg'
def combine(item1,item2):
	return item1+item2
class dede(object):
	def install():
		return None
	def print():
		pass

def error(typee,reason,file,line,cm):
	print(baba.colored(255,0,0,f"File {file}, line {line}, in <BABACODE>"))
	print(baba.colored(255,0,0,f"{cm}"))
	print(baba.colored(255,0,0,f"{typee}: {reason}"))
