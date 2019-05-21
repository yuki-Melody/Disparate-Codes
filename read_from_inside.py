class Read:
    def __init__(self, test = True, s=None):
        self.test = test
        self.s = s
        self.i = 0
        if(s != None and test == True):
            line = s.split('\n')
            line = list(filter(lambda x:len(x)>0, line))
            self.line = line
    def read(self):
        if(self.test == False):
            return input() #从键盘输入
        i = self.i
        line = self.line
        if i == len(line):
            print('Warn: relocate i')
            self.i = 0
            return self.read()
        self.i = i + 1
        return line[i]

read = Read(True, """
3
1 2 2
2 3 1
""").read  #delegate,将对象的方法委托给read

# read = input

# use read instead of input