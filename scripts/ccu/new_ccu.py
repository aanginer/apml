import sys,random,os
LETTERS = "abcdefghijklmnopqrstuvwxyz"
LETTERS += LETTERS.upper()
DIGITS = "0123456789"
LETTERS_DIGITS = LETTERS + DIGITS
ERROR = "\033[31m"
ENDC = "\033[0m"
SINGLEQ = "'"
DOUBLEQ = '"'
LANGNAME = "new_ccu"
KEYWORDS = [
    "print"
]

def liststr(l: list):
  string = ""
  for i in l:
    string += str(i)

  return string

def subVars(var: dict,expr):
    for v in var:
        if type(var[v]).__name__ == 'Token':
            expr = expr.replace(v,var[v].value)
        else:
            expr = expr.replace(v,var[v])
    return expr
    
class Token:
    def __init__(self,name="TOKEN",value=False):
        self.name = name
        self.value = value
        if self.name == 'INT' and self.value == False:
            self.value = 0

    def __repr__(self):

        if self.value != False:
            return f"[{self.name}:{self.value}]"
        else:
            return f"[{self.name}]"

    def fromStr(self,s):
        l = s.split(':')

class Constant:
    def __init__(self,name):
        self.name = name
        self.num = random.randint(1000,9999)

    def __repr__(self):
        return LANGNAME + '.const.' + self.name

    def get_val(self):
        return "<stdin>" + self.name + self.num

########################################################################
###########################LEXER########################################
########################################################################


class Lex:
    def __init__(self):
        self.tokens = []
        self.col = 0
        self.cmd = ''
        self.info = {
            'inStr':False,
            'Str':[],
            'StrId':-1,
            'exit':False,
            'inMathExpr': False,
            'mathExpr':[],
            'mathExprId':-1,
            'inVar':False,
            'gotVar':{},
            'waiting':{}
        }
    
    def lex(self,cmd):
        self.cmd = cmd
        if '=' in self.cmd:
            self.info
        for self.col,l in enumerate(list(self.cmd)):

            self.checkVar(cmd)

            if self.info['inMathExpr'] and self.cmd[self.col - 1] == '<':
                self.info['mathExprId']+=1
                self.info['mathExpr'].append('')    
                
            if self.info['inMathExpr']:
                if l == '>':
                    self.T_Mathexpr()
                    self.info["inMathExpr"] = False

                else:
                    self.info['mathExpr'][self.info['mathExprId']] += l

            if not self.info['inStr'] and l == '"':
                self.info['inStr'] = True
                continue

            if self.info['inStr'] and l == '"':
                self.info['inStr'] = False
                self.T_Str()

            if self.info['inStr'] and self.cmd[self.col - 1] == '"':
                self.info['StrId'] += 1
                self.info['Str'].append('')     

            if self.info['inStr']:
                self.info['Str'][self.info['StrId']] += l

            if l == '=':
                self.T_EQ()

            if l == '$' and self.cmd[self.col + 1] == 'r' and self.cmd[self.col + 2] == 'u' and self.cmd[self.col + 3] == 'n':
                self.T_EOF()

            if l == '<':
                self.info['inMathExpr'] = True

            if l in LETTERS:
                if l == 'p' and self.cmd[self.col + 1] == 'r' and self.cmd[self.col + 2] == 'i' and self.cmd[self.col + 3] == 'n' and self.cmd[self.col + 4] == 't':
                    self.T_print()

                if l == 'v' and self.cmd[self.col + 1] == 'a' and self.cmd[self.col + 2] == 'r':
                    self.T_PeVar()


            if len(self.cmd) - 1 == self.col:
                if self.info['inMathExpr']:
                    self.raiseError("SyntaxError","Expression not ended")

                elif self.info['inStr']:
                    self.raiseError("SyntaxError","Expression not ended")

                else:
                    self.T_EOL()

    ########################################################################
    ########################################################################

    def T_print(self):
        self.tokens.append(Token("PRINT"))

    def T_EOF(self):
        self.tokens.append(Token("EOF"))

    def T_Mathexpr(self):
        self.info['mathExpr'][self.info['mathExprId']] = self.info['mathExpr'][self.info['mathExprId']].replace('^','**')
        self.info['mathExpr'][self.info['mathExprId']] = subVars(globalDict['vars'],self.info['mathExpr'][self.info['mathExprId']])
        self.info['mathExpr'][self.info['mathExprId']] = subVars(globalDict['consts'],self.info['mathExpr'][self.info['mathExprId']])
        try:
            exprEval = eval(self.info['mathExpr'][self.info['mathExprId']])
        except:
            self.raiseError("IllegalExprError","Illegal character or expression")

        self.tokens.append(Token("INT",exprEval))

    def T_Str(self):
        self.tokens.append(Token("STR",self.info['Str'][self.info['StrId']]))

    def T_EOL(self):
        self.tokens.append(Token('EOL'))
    
    def T_PeVar(self):
        self.tokens.append(Token("NEW_VAR"))

    def T_EQ(self):
        self.tokens.append(Token("ASSIGN"))



    def checkVar(self,cmd):
        args = cmd.split()
        for idx,arg in enumerate(args):
            if arg in KEYWORDS:
                self.info['gotVar'][arg] = True
            if arg[0] in LETTERS_DIGITS:
                if arg in globalDict['vars'] or arg in globalDict['consts']:
                    if not arg in self.info['gotVar']:
                        self.info['waiting'][Token("VAR_ACCESS",arg)] = idx
                        self.info['gotVar'][arg] = True
                else:
                    if not arg in self.info['gotVar']:
                        self.info['waiting'][Token("VALUE",arg)] = idx
                        self.info['gotVar'][arg] = True


    def raiseError(self,name,reason):
        print(f"{ERROR}File {globalDict['file']}\n\t{self.cmd}\n{name}: {reason}{ENDC}")
        self.info['exit'] = True
        sys.exit()

    def getTokens(self):
        for wt in self.info['waiting']:
            self.tokens.insert(self.info['waiting'][wt],wt)

        return self.tokens

globalDict = {
    'rl':[]
}
globalDict['consts'] = {
    'RESULT':str(globalDict['rl']),
    'NULL':str(Constant("NULL"))
}
globalDict['vars'] = {
    '__name__':'<stdin>'
}
globalDict['modules'] = {
    
}


########################################################################
###########################PARSER#######################################
########################################################################

class Parse:
    def __init__(self,lexer: Lex):
        self.tokens = []
        self.info = {
            'exit':False
        }
        self.lexer = lexer
        self.cmd = self.lexer.cmd
    
    def raiseError(self,name,reason):
        print(f"{ERROR}File {globalDict['file']}\n\t{self.cmd}\n{name}: {reason}{ENDC}")
        self.info['exit'] = True
        sys.exit()

    def parse(self,tokens):
        global globalDict
        self.tokens = tokens
        for idx,tok in enumerate(tokens):
            
            if tok.name == 'VALUE':
                try:
                    v = int(tok.value)
                    tok.name = 'INT'
                except:
                    v = tok.value

                tok.value = v
                

            if tok.name == 'PRINT':
                addT = []
                for t in tokens:
                    if t.name == "INT" or t.name == "STR" or t.name == "EOF":
                        if t.name == "EOF":
                            self.raiseError("ParseError","Unexpected EOF while parsing")
                        if t.value != False:
                            addT.append(t.value)

                    if t.name == "VAR_ACCESS":
                        try:
                            addT.append(globalDict['vars'][t.value])
                        except KeyError:
                            try:
                                addT.append(globalDict['consts'][t.value])
                            except KeyError:
                                addT.append(Token("VAR_ACCESS","NULL"))

                    if t.name == "VALUE":
                        if t.value in DIGITS:
                            addT.append(Token("INT",t.value))
                        else:
                            self.raiseError("NameError",f"name '{t.value}' is not defined")

                globalDict['rl'].append(liststr(addT))
            

            if tok.name == 'VALUE' or tok.name == 'VAR_ACCESS':
                if tokens[idx+1].name == "ASSIGN":
                    if tokens[idx+2].name != 'EOL':
                        if tokens[idx+2].value != False:
                            globalDict['vars'][tok.value] = tokens[idx+2].value
                        else:
                            globalDict['vars'][tok.value] = globalDict['consts']['NULL']
                    else:
                        self.raiseError("SyntaxError","Empty variable assignment")
                else:
                    if not tok.name == "VAR_ACCESS":
                        self.raiseError('ValueError','Unexpected value')

            if tok.name == 'EOF':
                for line in globalDict['rl']:
                    print(line)



def run(cmd):
    lexer = Lex()
    lexer.lex(cmd)
    tokens = lexer.getTokens()
    #print(tokens)
    parser = Parse(lexer)
    parser.parse(tokens)
    
globalDict['file'] = "<stdin>"
while True:
    cm = input(">>> ")
    try:
        run(cm)
    except Exception as err:
        print(f"{ERROR}PythonError: {err}{ENDC}")

# dir = input("directory to file\n")
# globalDict['file'] = dir
# f = open('c:/python scripts/projects/' + dir,'r')
# lines = f.readlines()
# os.system('cls')
# for line in lines:
#     run(line)
