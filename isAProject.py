#Global variable names
ram = dict()
accumulator = 1
datatype_list = ["Dec", "Str"]
opcode_list = ["ADD", "SUBT", "MULT", "DIV", "LOAD", "OUTPUT", "INPUT", "STORE"]

def addToArray():
    pass
    
def addToRam(inst):
    varName = inst[1]
    varValue = inst[3]
    
    try:
        ram[varName] = int(varValue)
    except:
        ram[varName] = varValue
        
def loadVar(inst):
    varKey = inst[1]
    
    if varKey in ram.keys():
        global accumulator
        accumulator = ram[varKey]
        print "LOAD: ", accumulator
    else:
        print "FALLAS Variable " + varKey + " was not declared."
        
def storeVal(inst):
    varName = inst[1]
    
    print "storeVal:", accumulator
    ram[varName] = accumulator
    print ram
    ram[varName] = 23
    print ram

# This function will output a variable 
# OUTPUT var
def outputVar(inst):
    varName = inst[1]
    varVal = None
    
    if varName in ram.keys():
        varVal = ram[varName]
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
        ram[varName] = int(userVal)
    except:
        ram[varName] = userVal
    
# Checking the format of the opcodes
def checkInst(inst):
    opcode = inst[0]
    
    # Checks for instructions of length 2
    if opcode in opcode_list:
        if opcode == "LOAD" and len(inst) == 2:
            loadVar(inst)
        elif opcode == "OUTPUT" and len(inst) == 2:
            outputVar(inst)
        elif opcode == "INPUT" and len(inst) == 2:
            inputVar(inst)
        elif opcode == "STORE" and len(inst) == 2:
            storeVal(inst)
    
        # Checks for instruction with length of 3
        elif opcode == "ADD" and len(inst) == 3:
            add(inst)
        elif opcode == "SUBT" and len(inst) == 3:
            subt(inst)
        elif opcode == "MULT" and len(inst) == 3:
            mult(inst)
        elif opcode == "DIV" and len(inst) == 3:
            div(inst)
        
    elif opcode in datatype_list:
        # Checks for instructions of length 4
        if inst[2] == "=" and len(inst) == 4:
            addToRam(inst)
        
    
    
#Addition function
#Takes in a list which is an instruction then determines if the left and right operations are variables or values.
def add(inst):
    left_num = 0
    right_num = 0
    
    try:
        left_num = int(inst[1])
    except:
        if inst[1] in ram.keys():
            left_num = ram[inst[1]]
        else:
            var1 = inst[1]
            print "FALLAS: Variable " + var1 + " was not declared."
        
    try:
        right_num = int(inst[2])
    except:
        if inst[2] in ram.keys():
            right_num = ram[inst[2]]
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
        if inst[1] in ram.keys():
            left_num = ram[inst[1]]
        else:
            var1 = inst[1]
            print "FALLAS: Variable " + var1 + " was not declared."
            
    try:
        right_num = int(inst[2])
    except:
        if inst[2] in ram.keys():
            right_num = ram[inst[2]]
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
        if inst[1] in ram.keys():
            left_num = ram[inst[1]]
        else:
            var1 = inst[1]
            print "FALLAS: Variable " + var1 + " was not declared."
            
    try:
        right_num = int(inst[2])
    except:
        if inst[2] in ram.keys():
            right_num = ram[inst[2]]
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
        if inst[1] in ram.keys():
            left_num = ram(inst[1])
        else:
            var1 = inst[1]
            print "FALLAS: Variable " + var1 + "vwas not declared."
        
    try:
        right_num = int(inst[2])
    except:
        if inst[2] in ram.keys():
            right_num = ram[inst[2]]
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