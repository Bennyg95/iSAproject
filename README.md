# iSAproject


    In this project we will be designing our own instruction set architecture.
    Our choice of byte-organization is big endian, due to the fact that it would be easier to understand and easier to debug.
    Our ISA also contains an accumulator.
    List of possible operations:
        Input
        Output
        Halt
        fallas()
        ADD
        Subtract
        Multiply
        Divide
        STORE
        ACC
        LOAD
        LOADI
        STOREI
        <, > , =, !=
        Loop(start : end)
        ARRAY:
            NA.add(value)
            .at(location)
            .size()
            .replace(place : value)
            .remove(location)

#### Instructions

Editing text file
    
    The code has to be written in the the program.py file. If you need to reference a file take a looka t TestingFile.txt.
    In order to fun you're code type in the following command on a terminal:
        
        python isAProject.py

Initializing a variable:

    * all variables must be created at the begining of the file
    
    * Initializing an integer variable:
        Dec var = 3
    
    * Initializing a string:
        Str var = "fallas"
        


User Input:

    * INPUT value

Stop the program
    
    HALT

Creating a function:

    func nameFunction(
    
    )


Operations:
    
    Adding two numbers:
        ADD num1 num2   // will replace anything in the accumulator to the output value
        
    Subtracting two numbers:
        SUBT    num1 num2 // will replace anything in the accumulator to the output value
    
    Mulpliplying two numbers:
        MULT    num1 num2   // will replace anything in the accumulator to the ouput value
    
    Dividing two numbers:
        DIV num1 num2   // will replace anything in the accumulator to the output value
    
    
    