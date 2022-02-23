#SOURCE CODE FOR PARSER
import random,os,time
import tkinter as tk
cl=[1,2,3,4,5,6,7,8,9,0,'q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','c','v','b','n','m',1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]
sl=[1,2,3,4,5,6,7,8,9,0,'_','-','/','x','X','0x','0xe']
l=0
files={}
infile=False
cfn=''
ecmd={}
rl=[]
css={}
infunc=False
#UNUSED FUNCTION
def write(v):
	for j in v:
		print(j,end='')
		time.sleep(0.2)
#INSTALL COOL THING
def install(module,filename):
	print(f">>> $pip install {module}")
	time.sleep(random.randint(1,200)/100)
	print(f"code <- {module} @/public/ccu/public-code/modules/{filename}")
	time.sleep(random.randint(1,200)/100)
	print(f"{module} installed")
#\033 RGB FUNCTION
def rgb(r,g,b):
	return f"\033[38;2;{r};{g};{b}m"
#TKINTER THING MODULE
win=tk.Tk()
inpIds=[]
inps=[]
def runD(cm):
	global rl,win,inpIds,inps
	for jj in inps:
		jj.pack()
	if cm=='/help display':
		print("/label <content> : creates a label\n/import ")
	elif cm[:6]=='/label':
		tk.Label(win,text=cm[7:]).pack()
	elif cm[:7]=='/button':
		gh=[]
		s=''
		for j in cm[8:]:
			if j==';':
				gh.append(s)
				s=''
				continue
			
			s=s+j
		gh.append(s)
		tk.Button(win,text=gh[0],onclick=print(gh[1])).pack()
	elif cm[:6]=='/input':
		inpIds.append(cm[7:])
		inps.append(tk.Entry(win))
	elif cm[:4]=='/get':
		rl.append(inps[inpIds.index(cm[5:])].get())
#EXTRA STYLES FOR STYLING MODULE
def css2(cm):
	global rl,css
	css['red']=rgb(255,0,0)
	css['underline']='\033[4m'
	css['bold']='\033[1m'
	css['italic']='\033[3m'
	css['strike']='\033[9m'
	css['green']=rgb(0,255,0)
	css['blue']=rgb(0,0,255)
	css['yellow']=rgb(255,255,0)
	css['cyan']=rgb(0,255,255)
	css['purple']=rgb(255,0,255)
	css['orange']=rgb(255,127,0)
	css['invisible']='\033[8m'
	if cm=='/help styling':
		#PRINT ALL STYLES
		print(f'adds new styles:\n{rgb(255,0,0)}red\033[0m\n{rgb(0,0,155)}blue\033[0m\n{rgb(0,255,0)}green\033[0m\n{rgb(255,255,0)}yellow\033[0m\n{rgb(255,0,255)}purple\033[0m\n{rgb(0,255,255)}cyan\033[0m\n{rgb(255,127,0)}orange\033[0m\n\033[4munderline\033[0m\n\033[1mbold\033[0m\n\033[3mitalic\033[0m\n\033[9mstrike\033[0m\ninvisible')
func={}
infunc=False
fcn=''
inloop=False
re=1
#OS MODULE
def osimp(cm,l):
	global files,infile,cfn,ecmd,rl,infunc,fcn,inloop,re,ll,func
	#PRINT ALL COMMANDS
	if cm=='/help os':
		print("/clear : clears screen\n/file : prints all extra commands and your position\n/read <filepath> : gets file\n/new <name> : starts new file\n/endf : ends current file\n/function <name> : makes callable function\n/endfunc : nds function")
	#NEW FILE
	elif cm[:4]=='/new':
		cfn=cm[5:]
		infile=True
		files[cfn]=[]
	#END FILE
	elif cm=='/endf':
		infile=False
	elif cm[:5]=='/read':
		if cm[6:] in files:
			for lii in files[cm[6:]]:
				rl.append(lii)
	elif cm=='/file':
		for k in ecmd:
			rl.append(k)
		rl.append(f"line:{l}")
	elif cm=='/clear':
		os.system('clear')
	elif cm[:9]=='/function':
		infunc=True
		fcn=cm[10:]
		func[fcn]=[]
	elif cm=='/endfunc':
		infunc=False
	elif cm[0]=='/':
		if cm[1:] in func:
			for k in func[cm[1:]]:
				cmd(k,0)
	if infile:
		files[cfn].append(cm)
	if infunc:
		func[fcn].append(cm)

inshell=False
def shell(l):
	global inshell
	if inshell:
		cm=input('/private/ccu/code/run.ccu> $')
		if cm=='endshell':
			inshell=False
			return
		elif cm=='line':
			print(l)

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
def gen(n):
	global cl
	r=''
	for i in range(n):
		if not random.randint(1,3)==1:
			x=random.choice(cl)
			if random.randint(1,100)>50:
				if type(x).__name__=='str':
					x=x.upper()
		else:
			x=random.choice(sl)
		r=r+str(x)
	return r
imported=[]
var={}
rl=[]
ll=[]
ecmd={
	'{{cm}}':['s',255,0,0,'hi']
}
print('type "/help" for command list')
it=[]
inshell=False
def cmd(cm,l):
	global files,ecmd,rl,imported,var,it,infunc,func,inshell
	#inshell=False
	if inshell:
		shell(l)
		return
	if 'os' in imported:
		osimp(cm,l)
	if 'styling' in imported:
		css2(cm)
	if 'display' in imported:
		runD(cm)

	if cm in ecmd.keys():
		c=ecmd[cm]
		if not c[0]=='s':
			rl.append(colored(c[1],c[2],c[3],f'<__init({cm})__ {gen(15)} at line {l} returns {c[4]}>'))
		else:
			rl.append(colored(c[1],c[2],c[3],c[4]))
	elif cm=='/help':
		print('/help <module:optional> : returns list of commands for module\n;<cm>;<r>;<g>;<b>;<returns>;<s> : creates new command\n/print <values> : prints values\n/var <varname>=<varcontent> : sets a variable\n/import <module> imports a module\n/style <name>: creates a style\n/css <033content> : set a 033 style\n/list : creates a list\n/if <op>=<cond> : checks if op = cond\nexecute <script> : executes script if if statement is true')
	elif cm=='/shell':
		inshell=True
	elif cm[0]==';':
		pn=0
		pc=[]
		s=''
		for jj in cm:
			if jj==';':
				pc.append(s)
				pn+=1
				s=''
				continue
			if pn>7:
				ecmd[pc[1]]=[pc[6],pc[2],pc[3],pc[4],pc[5]]
				break
			s=s+jj
		pc.append(s)
		ecmd[pc[1]]=[pc[6],pc[2],pc[3],pc[4],pc[5]]
	elif cm=='/end':
		for ll in rl:
			print(ll)
		rl=[]
	elif cm[:4]=='/var':
		vc=''
		vn=''
		pn=1
		for ljl in cm[5:]:
			if ljl=='=':
				pn+=1
				continue
			if pn==1:
				vn=vn+ljl
			else:
				vc=vc+ljl
		var[vn]=vc
	elif cm[:6]=='/print':
		if cm[7]=='%':
			pn=1
			s=''
			sl=[]
			for gj in cm[8:]:
				if gj=='&':
					pn+=1
					sl.append(s)
					s=''
					continue
				s=s+gj
			sl.append(s)
			if not infunc:
				rl.append(css[sl[0]]+sl[1]+'\033[0m')
		elif cm[7:] in var:
			if type(var[cm[7:]]).__name__=='list':
				ind=input('index')
				if ind=='all':
					rl.append(var[cm[7:]])	
				else:
					ind=int(ind)
					rl.append(var[cm[7:]][ind])
			else:
				rl.append(var[cm[7:]])
		else:
			rl.append(cm[7:])
	elif cm[:4]=='/css':
		css[cm[5:]]=f"\033[{cm[5:]}m"
	elif cm[:6]=='/style':
		r=input('r')
		g=input('g')
		b=input('b')
		css[cm[7:]]=f'\033[38;2;{r};{g};{b}m'
	elif cm[:5]=='/list':
		li=[]
		for ii in range(int(input('how many items'))):
			li.append(input(ii))
		var[cm[6:]]=li
	elif cm[:7]=='/import':
		imported.append(cm[8:])
		install(cm[8:],f"{cm[8:]}.ccu")
	elif cm[:3]=="/if":
		cond = cm[4:]
		if cond[1] == '-':
			if int(cond[0])-int(cond[2])==int(cond[4]):
				cond2=True
			else:
				cond2=False
		elif cond[1] == '/':
			if int(cond[0])/int(cond[2])==int(cond[4]):
				cond2=True
			else:
				cond2=False
		elif cond[1] == '*':
			if int(cond[0])*int(cond[2])==int(cond[4]):
				cond2=True
			else:
				cond2=False
		elif cond[1] == '+':
			if int(cond[0])+int(cond[2])==int(cond[4]):
				cond2=True
			else:
				cond2=False
		s=''
		o=-1
		k1=0
		ats=True
		for jk in cond:
			o+=1
			if jk=='=':
				t=o
				break
			if jk=='{':	
				k1=o
				ats=False
				continue
			if jk=='}':
				k2=o
				ats=False
				continue
			if ats:
				s=s+jk
		if s in var.keys():
			if type(var[s]).__name__=='list':
				if '{' in cond:
					if cond[k1+1:k2]==cond[t+1:]:
						cond2=True
					else:
						cond2=False
				else:
					cond2=False
			else:
				if var[s]==cond[t+1:]:
					cond2=True
				else:
					cond2=False
		if (cond2):
			it.append(l)
	elif cm[:7]=='execute':
		if l-1 in it:
			cmd(cm[8:],l+1)
	elif cm[:6]=='/debug':
		if cm[7:]=='commands':
			print(ecmd)
		elif cm[7:]=='functions':
			print(func)
