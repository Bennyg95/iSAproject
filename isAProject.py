register = dict()
accumulator = 0

def add(inst):
    print(int(inst[1]) + int(inst[2]))

def subt(inst):
    print(int(inst[1]) - int(inst[2]))

def mult(inst):
    print(int(inst[1]) * int(inst[2]))

def div(inst):
    print(float(inst[1]) / float(inst[2]))

def main():
    
    bencounter = 0 
    print "Welcome!"
    
    fin = open("TestingFile.txt", "r")
    
    for line in fin.readlines():
        inst_list = line.split()
        if len(inst_list) == 0:
            continue
        if inst_list[0] == "ADD":
            add(inst_list)

        elif inst_list[0] == "SUBT":
	        subt(inst_list)

        elif inst_list[0] == "MULT":
	        mult(inst_list)

        elif inst_list[0] == "DIV":
	        div(inst_list)
        
    '''

    inst_list = instruction.split()

    
	 '''
	 
	
main()


