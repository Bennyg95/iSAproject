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
    instruction = raw_input("Enter instruction: \n")

    print(instruction.split())    

    inst_list = instruction.split()

    if inst_list[0] == "ADD":
        add(inst_list)

    elif inst_list[0] == "SUBT":
	 subt(inst_list)

    elif inst_list[0] == "MULT":
	 mult(inst_list)

    elif inst_list[0] == "DIV":
	 div(inst_list)
	
main()


