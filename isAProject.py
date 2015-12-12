#Global variable names
register = dict()
accumulator = 0
opcode_list = ["ADD", "SUBT", "MULT", "DIV", "LOAD", "OUTPUT", "INPUT", "STORE"]
register = dict()

def addToArray():
    pass
    
def addToRegister(inst):
    varName = inst[1]
    varValue = inst[3]
    
    try:
        register[varName] = int(varValue)
    except:
        register[varName] = varValue
        
def loadVar(inst):
    varKey = inst[1]
    
    if varKey in register.keys():
        accumulator = register[varKey]
        print "LOAD: ", accumulator
    else:
        print "FALLAS Variable " + varKey + " was not declared."
        
def storeVal(inst):
    varName = inst[1]
    
    register[varName] = accumulator

# This function will output a variable 
# OUTPUT var
def outputVar(inst):
    varName = inst[1]
    varVal = None
    
    if varName in register.keys():
        varVal = register[varName]
        print "OUTPUT: ", varVal
    else:
        print "FALLAS: Variable " + varName + " was not declared."
    
## INPUT funcion
# # INPUT var
def inputVar(inst):
    # where would we be saving the inputed variable?
    userVal = raw_input()
    varName = inst[1]
    
    try:
        register[varName] = int(userVal)
    except:
        register[varName] = userVal
    

# Checking the format of the opcodes
def checkInst(inst):
    opcode = inst[0]
    
    if len(inst) == 2:
        if opcode in opcode_list:
            if opcode == "LOAD":
                loadVar(inst)
            elif opcode == "OUTPUT":
                outputVar(inst)
            elif opcode == "INPUT":
                inputVar(inst)
            elif opcode == "STORE":
                storeVal(inst)
    
    elif len(inst) == 3:
        if opcode in opcode_list:
            if opcode == "ADD":
                add(inst)
            elif opcode == "SUBT":
                subt(inst)
            elif opcode == "MULT":
                mult(inst)
            elif opcode == "DIV":
                div(inst)
           
    elif len(inst) == 4:
        if (inst[0] == "Str" or inst[0] == "Dec") and inst[2] == "=":
            addToRegister(inst)
        else:
            print "FALLAS: Invalid declaration."
    
    
#Addition function
#Takes in a list which is an instruction then determines if the left and right operations are variables or values.
def add(inst):
    left_num = 0
    right_num = 0
    
    try:
        left_num = int(inst[1])
    except:
        if inst[1] in register.keys():
            left_num = register(inst[1])
        else:
            var1 = inst[1]
            print "FALLAS: Variable " + var1 + " was not declared."
        
    try:
        right_num = int(inst[2])
    except:
        if inst[2] in register.keys():
            right_num = register[inst[2]]
        else:
            var2 = inst[2]
            print "FALLAS: Variable " + var2 + " was not declared."
            
    accumulator = left_num + right_num
    
    print accumulator
    
def subt(inst):
    left_num = 0
    right_num = 0
    
    try:
        left_num = int(inst[1])
    except:
        if inst[1] in register.keys():
            left_num = register(inst[1])
        else:
            var1 = inst[1]
            print "FALLAS: Variable " + var1 + " was not declared."
            
    try:
        right_num = int(inst[2])
    except:
        if inst[2] in register.keys():
            right_num = register[inst[2]]
        else:
            var2 = inst[2]
            print "FALLAS: Variable " + var2 + " was not declared."
            
    accumulator =  left_num - right_num
    
    print accumulator
        
            
def mult(inst):
    left_num = 0
    right_num = 0
    
    try:
        left_num = int(inst[1])
    except:
        if inst[1] in register.keys():
            left_num = register(inst[1])
        else:
            var1 = inst[1]
            print "FALLAS: Variable " + var1 + " was not declared."
            
    try:
        right_num = int(inst[2])
    except:
        if inst[2] in register.keys():
            right_num = register(inst[2])
        else:
            var2 = inst[2]
            print "FALLAS: Variable " + var2 + " was not declared."
            
    accumulator = left_num * right_num
    
    print accumulator
    
def div(inst):
    left_num = 0;
    right_num = 0;
    
    try:
        left_num = int(inst[1])
    except:
        if inst[1] in register.keys():
            left_num = register(inst[1])
        else:
            var1 = inst[1]
            print "FALLAS: Variable " + var1 + "vwas not declared."
        
    try:
        right_num = int(inst[2])
    except:
        if inst[2] in register.keys():
            right_num = register[inst[2]]
        else:
            var2 = inst[2]
            print "FALLAS: Variable " + var2 + " was not declared."
            
    if right_num != 0:
        accumulator = left_num / right_num
        print accumulator
    else:
        print "FALLAS: Cannot divide by 0."
        

#Main function of the program
def main():
    bencounter = 0 
    print "Welcome! to the world's most amazing ISA"
    
    fin = open("TestingFile.txt", "r")
    

    for line in fin.readlines():
        inst = line.split()
        
        if len(inst) == 0:
            continue
    
        checkInst(inst)
        
main()