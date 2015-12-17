import sys

#Global variable names
ram = dict()
# dictionary that holds user-defined functions
func_dict = dict()
accumulator = 0
array_operations = ["ADD", "AT", "SIZE", "REPLACE", "REMOVE"]
datatype_list = ["Dec", "Str", "Array"]
opcode_list = ["ADD", "SUBT", "MULT", "DIV", "LOAD", "OUTPUT", "INPUT", "STORE", "CLEAR", "CALL"]

def initArray(inst):
    arrName = inst[2]
    arrType = inst[1]
    
    if arrType == "Str":
        arrName += "_s"
    elif arrType == "Dec":
        arrName += "_d"
    
    ram[arrName] = list()

def clearAcc():
    accumulator = 0
    print "The accumulator is set to 0"
    
def haltProgram():
    sys.exit()

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
        # print "LOAD: ", accumulator
    else:
        print "FALLAS Variable " + varKey + " was not declared."
        sys.exit()
        
def storeVal(inst):
    varName = inst[1]
    
    print "storeVal:", accumulator
    ram[varName] = accumulator
    '''
    print ram
    ram[varName] = 23
    print ram
    '''

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
        sys.exit()
    
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
        
def callFunc(inst):
    funcName = inst[1]
    
    if funcName in func_dict.keys():
        funcInst = func_dict[funcName]
        
        for inst in funcInst:
            checkInst(inst)
    
# Checking the format of the opcodes
def checkInst(inst):
    opcode = inst[0]
    

    if opcode in opcode_list:
        #Checks for instructions of length 1
        if opcode == "CLEAR" and len(inst) == 1:
            clearAcc()
        elif opcode == "HALT" and len(inst) == 1:
            haltProgram()
            
    # Checks for instructions of length 2
        elif opcode == "LOAD" and len(inst) == 2:
            loadVar(inst)
        elif opcode == "OUTPUT" and len(inst) == 2:
            outputVar(inst)
        elif opcode == "INPUT" and len(inst) == 2:
            inputVar(inst)
        elif opcode == "STORE" and len(inst) == 2:
            storeVal(inst)
        
        elif opcode == "CALL" and len(inst) == 2:
            callFunc(inst)
    
        # Checks for instruction with length of 3
        elif opcode == "ADD" and len(inst) == 3:
            add(inst)
        elif opcode == "SUBT" and len(inst) == 3:
            subt(inst)
        elif opcode == "MULT" and len(inst) == 3:
            mult(inst)
        elif opcode == "DIV" and len(inst) == 3:
            div(inst)
            
        elif inst[1] in array_operations and 
            
        
    elif opcode in datatype_list:
        # Checks for instructions of length 4
        if inst[2] == "=" and len(inst) == 4:
            addToRam(inst)
            
        elif inst[1] in datatype_list and len(inst) == 3:
            initArray(inst)
            
    else:
        print "FALLAS: " + opcode + " is not a valid opcode."
        sys.exit()
        
    
    
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
            sys.exit()
        
    try:
        right_num = int(inst[2])
    except:
        if inst[2] in ram.keys():
            right_num = ram[inst[2]]
        else:
            var2 = inst[2]
            print "FALLAS: Variable " + var2 + " was not declared."
            sys.exit()
      
    global accumulator      
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
            sys.exit()
            
    try:
        right_num = int(inst[2])
    except:
        if inst[2] in ram.keys():
            right_num = ram[inst[2]]
        else:
            var2 = inst[2]
            print "FALLAS: Variable " + var2 + " was not declared."
            sys.exit()
            
    global accumulator
    accumulator = left_num - right_num
    
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
            sys.exit()
            
    try:
        right_num = int(inst[2])
    except:
        if inst[2] in ram.keys():
            right_num = ram[inst[2]]
        else:
            var2 = inst[2]
            print "FALLAS: Variable " + var2 + " was not declared."
            sys.exit()
            
    global accumulator
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
        global accumulator
        accumulator = left_num / right_num
        print accumulator
    else:
        print "FALLAS: Cannot divide by 0."
        sys.exit()

#Main function of the program
def main():
    bencounter = 0
    isFunc = 0
    funcName = None
    funcLines = list()
    print "Welcome! to the world's most amazing ISA"
    
    fin = open("TestingFile.txt", "r")
    
    file = fin.readlines()

    for line in file:
        inst = line.split()
        
        if len(inst) == 0:
            continue
        
        if "func" in inst:
            # print inst
            if inst[0] == "func" and inst[2] == ":" and len(inst) == 3:
                funcName = inst[1]
                # print funcName
                isFunc = 1
                continue
        
        if inst[0] == "end":
            func_dict[funcName] = funcLines
            # print inst[0]
            isFunc = 0
            # print func_dict
            funcLines = list()
            continue
                
        if isFunc == 1:
            # print "inside isFunc: ", inst
            funcLines.append(inst)
        else:
            checkInst(inst)
        
        
main()