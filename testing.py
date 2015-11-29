def add(inst):
    print(int(inst[1]) + int(inst[2]))

def subt(inst):
    print("Hello, world")

def main():
    instruction = raw_input("Enter instruction: \n")

    print(instruction.split())    

    inst_list = instruction.split()

    if inst_list[0] == "ADD":
        add(inst_list)

main()
