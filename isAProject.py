import sys

#Global variable names
ram = dict()
# dictionary that holds user-defined functions
func_dict = dict()
loop_dict = dict()
accumulator = 0
datatype_list = ["Dec", "Str", "Array"]
opcode_list = ["ADD", "SUBT", "MULT", "DIV", "LOAD", "OUTPUT", "INPUT", "STORE", "CLEAR", "CALL", "LOOP", "ARRADD", "ARRAT", "ARRSIZE", "ARRREPLACE", "ARRREMOVE", "ARRFIND"]

def findVal(inst):
    arrName = inst[1]
    val = int(inst[2])
    
    if arrName + "_d" in ram.keys():
        arr = ram[arrName+"_d"]
        for i in range(len(arr)):
            if arr[i] == val:
                print "Number was found"

def runLoop(inst):
    loopName = inst[1]
    loopCounter = int(raw_input("How many times do you want to loop? "))
    
    if loopName in loop_dict.keys():
        loopInst = loop_dict[loopName]
        
        for i in range(loopCounter):
            for inst in loopInst:
                checkInst(inst)

def arrayReplace(inst):
    arrName = inst[1]
    index = inst[2]
    replaceVal = inst[3]
    
    try:
        index = int(inst[2])
        if arrName + "_d" in ram.keys():
            try:
                replaceVal = int(inst[3])
                global ram
                ram[arrName+"_d"][index] = replaceVal
            except:
                print "FALLAS"
        elif arrName + "_s" in ram.keys():
            try:
                global ram
                ram[arrName+"_d"][index] = replaceVal
            except:
                print "FALLAS: ", index, " is not a valid index."
    except:
        print "FALLAS: " + index + " is not a valid index."
    
    

def loadArrayAt(inst):
    arrName = inst[1]
    index = None

    try:
        index = int(inst[2])
        if arrName + "_d" in ram.keys():
            try:
                global accumulator
                accumulator = ram[arrName+"_d"][index]
                print accumulator
            except:
                print "FALLAS:", index, "is not a valid index."
        elif arrName + "_s" in ram.keys():
            try:
                global accumulator
                accumulator = ram[arrName+"_s"][index]
                print accumulator
            except:
                print "FALLAS:", index, "is not a valid index."
    except:
        print "FALLAS: " + index + " is not a valid index."
        sys.exit()

def initArray(inst):
    arrName = inst[2]
    arrType = inst[1]
    
    if arrType == "Str":
        arrName += "_s"
    elif arrType == "Dec":
        arrName += "_d"

    global ram
    ram[arrName] = list()

def loadArraySize(inst):
    arrName = inst[1]
    
    if arrName + "_d" in ram.keys() or arrName + "_s" in ram.keys():
        try:
            global accumulator
            accumulator = ram[arrName+"_d"]
            print len(ram[arrName+"_d"])
        except:
            global accumulator
            accumulator = ram[arrName+"_d"]
            print len(ram[arrName+"_s"])
        

def clearAcc():
    accumulator = 0
    print "The accumulator is set to 0"
    
def haltProgram():
    sys.exit()

def addToArray(inst):
    arrName = inst[1]
    
    try:
        arrVal = int(inst[2])
        if arrName + "_d" in ram.keys():
            ram[arrName+"_d"].append(arrVal)
        elif arrName + "_s" in ram.keys():
            print "FALLAS: cannot add Dec values into string array."
            sys.exit()
        else:
            print "FALLAS: array " + arrName + " has not been initialized."
    except:
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
    
    global ram
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
            
        elif opcode == "LOOP" and len(inst) == 2:
            runLoop(inst)
    
        # Checks for instruction with length of 3
        elif opcode == "ADD" and len(inst) == 3:
            add(inst)
        elif opcode == "SUBT" and len(inst) == 3:
            subt(inst)
        elif opcode == "MULT" and len(inst) == 3:
            mult(inst)
        elif opcode == "DIV" and len(inst) == 3:
            div(inst)
            
        elif opcode == "ARRSIZE" and len(inst) == 2:
            loadArraySize(inst)
        elif opcode == "ARRADD" and len(inst) == 3:
            addToArray(inst)
        elif opcode == "ARRAT" and len(inst) == 3:
            loadArrayAt(inst)
        elif opcode == "ARRFIND" and len(inst) == 3:
            findVal(inst)
        elif opcode == "ARRREPLACE" and len(inst) == 4:
            arrayReplace(inst)
        
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
    
    
    print "Welcome! to the world's most amazing ISA"
    
    instruction_file = raw_input("Enter the file name: ")
    
    isFunc = 0
    isLoop = 0
    
    funcName = None
    loopName = None
    
    funcLines = list()
    loopLines = list()
    
    fin = open(instruction_file, "r")
    
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
            
        if "loop" in inst:
            # print inst
            if inst[0] == "loop" and inst[2] == ":" and len(inst) == 3:
                loopName = inst[1]
                # print funcName
                isLoop = 1
                continue
            
        if isLoop == 1 and inst[0] == "end":
            loop_dict[loopName] = loopLines
            isLoop = 0
            print loop_dict[loopName]
            loopLines = list()
            continue
        
        if isFunc == 1 and inst[0] == "end":
            func_dict[funcName] = funcLines
            # print inst[0]
            isFunc = 0
            # print func_dict
            funcLines = list()
            continue
                
        if isFunc == 1:
            # print "inside isFunc: ", inst
            funcLines.append(inst)
        elif isLoop == 1:
            loopLines.append(inst)
        else:
            checkInst(inst)

main()