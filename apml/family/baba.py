import time
from datetime import date
import random
var=""
li=[]
ids={}
clas={}
styles={}
cml=[]
cn=[]
rl=[]
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
def commandprompt(inp,times,newcm='{{command object}}',newcmt="babacode cm",nr=0,ng=255,nb=0,s=False):
	"""
	<BABACODE>
	gives command prompt to use commands
	"""
	print(f"BABACODE 1.9.3 python compiler")
	print(f"info: prompt:'{inp}' times:'{times}'")
	times=int(times)
	for i in range(times):
		cm = input(inp)
		if cm == "/cobble":
			rl.append('cobble')
		elif cm == "/day":
			rl.append(date.today())
		elif cm == "/pos":
			rl.append(f"File 'main.input', line {i+1}, in <BABACODE>")
		elif cm == "/convertflask":
			print(colored(255,0,0,f"File 'main.input', line {i+1}, in <BABACODE>"))
			print(colored(255,0,0,f"   {cm}"))
			print(colored(255,0,0,"File '/BABA/code/input/main.interpreter'"))
			print(colored(255,0,0,f"   convertflask!=valid, cm={cm}"))
			print(colored(255,0,0,f"TooBadError: {cm} is a command but too bad we dont support flask. hahahahahahahahahahahahahaha"))
		elif cm[:6]=="/print":
			if cm[7:13]=="@var":
				global var
				rl.append(var)
			elif cm[7:14]=="@list":
				rl.append(li)
			elif cm[7] == "#":
				rl.append(ids[cm[8:10]])
			elif cm[7]  == ".":
				rl.append(clas[cm[8:10]])
			elif cm[7]=="%":
				if cm[11:15]=="@var":
					css=styles[cm[8:10]]
					rl.append(colored(css[0],css[1],css[2],var))
				elif cm[11:16]=="@list":
					css=styles[cm[8:10]]
					rl.append(colored(css[0],css[1],css[2],li))
				elif cm[11] == "#":
					css=styles[cm[8:10]]
					rl.append(colored(css[0],css[1],css[2],ids[cm[12:14]]))
				elif cm[11]  == ".":
					css=styles[cm[8:10]]
					rl.append(colored(css[0],css[1],css[2],clas[cm[12:14]]))	
			else:
				print(cm[7:])
		elif cm[:4]=="/var":
			if cm[5:12]=="@input":
				rl.append('@input')
			else:
				var=cm[5:]
		elif cm[:5]=="/list":
			ll=input('how many items')
			for i in range(int(ll)):
				l=input('item')
				li.append(l)
		elif cm[:3]=="/id":
			if cm[7:13]=="@input":
				x=input('')
				ids[cm[4:6]]=x
			else:
				ids[cm[4:6]]=cm[7:]
		elif cm[:6] == "/class":
			list1=[]
			lis=input('how many items')
			lis=int(lis)
			for i in range(lis):
				l=input('item')
				list1.append(l)
			clas[cm[7:9]]=list1
		elif cm[:6] == "/style":
			r=int(input('red'))
			g=int(input('green'))
			b=int(input('blue'))
			styles[cm[7:9]]=[r,g,b]
		elif cm[:3]=="/if":
			cond = cm[4:]
			if cond[1] == '-':
				if int(cond[0])-int(cond[2])==int(cond[4]):
					cond=True
				else:
					cond=False
			elif cond[1] == '/':
				if int(cond[0])/int(cond[2])==int(cond[4]):
					cond=True
				else:
					cond=False
			elif cond[1] == '*':
				if int(cond[0])*int(cond[2])==int(cond[4]):
					cond=True
				else:
					cond=False
			elif cond[1] == '+':
				if int(cond[0])+int(cond[2])==int(cond[4]):
					cond=True
				else:
					cond=False
			elif '#' in cond:
				if cond[1:3] in ids.keys():
					idlol=ids[cond[1:3]]
					if idlol==cond[4:]:
						cond=True
					else:
						cond=False
				else: 
					cond=False
			elif '.' in cond:
				if cond[1:3] in clas.keys():
					global claslol
					claslol=clas[cond[1:3]]
					hh=cond[4]
					if claslol[int(hh)]==cond[7:]:
						cond=True
					else:
						cond=False
				else:
					cond=False
			else:
				cond=False
			if (cond):
				cml.append(i)
				cn.append(cond)
		elif cm=="execute":
			if i-1 in cml and cn[cml.index(i-1)]:
				l=commandprompt('execute  ',1)
		elif cm[:6]=="/error":
			print(colored(255,0,0,f"File 'main.input', line {i+1}, in <BABACODE>"))
			print(colored(255,0,0,f"  ERROR RAISED"))
			print(colored(255,0,0,f"RaisedError: {cm[7:]}"))
		elif cm[0]==';':
			print(colored(0,0,255,"new command name"))
			cmn=input()
			print(colored(0,0,255,"output"))
			cmt=input()
			print(colored(0,0,255,"r"))
			cr=input()
			print(colored(0,0,255,"g"))
			cg=input()
			print(colored(0,0,255,"b"))
			cb=input()
			s=input('sepertate?')
			if s=="y" or s=="yes":
				commandprompt('',10,newcm=cmn,newcmt=cmt,nr=cr,ng=cg,nb=cb,s=True)
			else:
				commandprompt('',10,newcm=cmn,newcmt=cmt,nr=cr,ng=cg,nb=cb)
		elif cm[:7]=="/random":
			if cm[8:]=='$math':
				m=""
				bo=0
				num=str(random.randint(1,9))
				m=m+num
				def lol():
					return
				while True:
					op=random.randint(1,100)
					num=str(random.randint(1,99))
					kpg=op=random.randint(1,100)
					ob=random.randint(1,100)
					if op<31:
						m=m+num+'*'+num
					elif op>31 and op<56:
						m=m+num+'+'+num
					elif op>56 and op<71:
						m=m+num+'/'+num
					elif op>71 and op<81:
						m=m+num+'-'+num
					elif op>81 and op<99:
						m=m+num+'^('+num+")"
					else:
						m=m+'sq('+num+")"
					if ob>50:
						ob=random.randint(1,100)
						if bo>=1:
							if ob>51:
								m=m+")+"
								bo-=1
							if ob>51 and ob<76:
								bo+=1
								m=m+"*("
								print(bo)
							else:
								lol()
						else:
							bo+=1
							print(bo)
							m=m+"+("
					
					if kpg>76:
						while bo>0:
							m=m+")"
							bo-=1
						print(m)
						break

					if len(m)>30:
						while bo>0:
							m=m+")"
							bo-=1
						rl.append(m)
						break	
		elif cm==newcm:
			if s!=True:
				rl.append(colored(0,255,0,f'<BABACODE created method "{newcm}" returns "{newcmt}" >'))	
			else:
				rl.append(colored(nr,ng,ng,f'{newcmt}'))
		elif cm[:2]=='//':
			rl.append(colored(99,99,99,cm[2:]))
			continue
		elif cm[0]!="/":
			print(colored(255,0,0,f"File 'main.input', line {i+1}, in <BABACODE>"))
			print(colored(255,0,0,f"  {cm}"))
			print(colored(255,0,0,f"SyntaxError: unexpected token {cm[0]} at pos 0"))
		elif cm=='/end':
			for line in rl:
				if line=="@input":
					x=input('input  ')
					line=rl
					print(line)
				else:
					print(line)
		else:
			print(colored(255,0,0,f"File 'main.input', line {i+1}, in <BABACODE>"))
			print(colored(255,0,0,f"  {cm}"))
			print(colored(255,0,0,f"SyntaxError: command {cm} not found"))
		#print(cm[:4],'lol',cm[4:11])
def endcode():
	print(colored(255,0,0,"..."))
	time.sleep(1)
	print(colored(255,0,0,"repl ended"))
	time.sleep(1)
	print(colored(255,0,0,"LOL U thought it woud end"))
	exit('JK IT WILL END')

def nationalholiday():
	print("its BABA DAY!")
  
class Baba:
  def hello():
    print("hi Baba")
  def setupRandomthing(times,thing,wait,thing2,looks,wut):
    global times,thing,wait,thing2,looks,wut
    times = times
    thing = thing
    wait = wait
    thing2 = thing2
    looks = looks
    wut = wut

  class randomThing(object):
    global thing,looks,wait,times,wut,thing2
    def __init__(self):
      self.thing = thing
      self.times = times
      self.wait = wait
      self.wut = wut
      self.looks = looks
      self.thing2 = thing2
      #run needed code here in init()
    def run(self):
      for i in range(int(times)+int(wut)):
        print(thing)
        time.sleep(wait)
        print("style.css:",looks)
        print(thing2)
