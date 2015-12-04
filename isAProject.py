#Global variable names
register = dict()
accumulator = 0
opcode_list = ["ADD", "SUBT", "MULT", "DIV", "LOAD", "OUTPUT"]
register = dict()

#def add(inst):
    #print(int(inst[1]) + int(inst[2]))
    
def addToRegister(inst):
    
    register[inst[1]]
    
def loadVar(inst):
    varKey = inst[1]
    
    register["var1"] = 2
    
    if inst[1] in register.keys():
        accumulator = register[inst[1]]
        print accumulator
    else:
        print "FALLAS Variable " + varKey + " was not declared."

def outputVar(inst):
    print(inst[1]

def subt(inst):
    print(int(inst[1]) - int(inst[2]))

def mult(inst):
    print(int(inst[1]) * int(inst[2]))

def div(inst):
    print(float(inst[1]) / float(inst[2]))

# Checking the format of the opcodes
def checkInst(inst):
    opcode = inst[0]
    
    if len(inst) == 2:
        if opcode in opcode_list:
            if opcode == "LOAD":
                loadVar(inst)
            if opcode == "OUTPUT":
                outputVar(inst)
    
    elif len(inst) == 3:
        if opcode in opcode_list:
            if opcode == "ADD":
                add(inst)
                
    elif len(isnt) == 4:
        

#Addition function
#Takes in a list which is an instruction then determines if the left and right operations are variables or values.
def add(inst):
    left_num = 0;
    right_num = 0;
    
    try:
        left_num = int(inst[1])
    except:
        if inst[1] in register.keys():
            left_num = register(inst[1])
        else:
            var1 = inst[1]
            print "FALLAS: Variable " + var1 + "was not declared."
        
    try:
        right_num = int(inst[2])
    except:
        if inst[2] in register.keys():
            right_num = register[inst[2]]
        else:
            var2 = inst[2]
            print "FALLAS: Variable " + var2 + "was not declared."
            
    accumalator = left_num + right_num
    
    print accumalator

#Main function of the program
def main():
    
    bencounter = 0 
    print "Welcome!"
    
    fin = open("TestingFile.txt", "r")
    
    for line in fin.readlines():
        inst = line.split()
        
        if len(inst) == 0:
            continue
        
        checkInst(inst)
main()


