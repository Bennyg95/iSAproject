# iSAproject

### Description

    In this project we will be designing our own instruction set architecture.
    Our choice of byte-organization is big endian, due to the fact that it would 
    be easier to understand and easier to debug. Our ISA also contains an accumulator.
    
#### Instructions

    variables and functions should be declared before the main function.

Editing text file
    
    The code has to be written in the the program.py file. If you need to reference 
    a file take a look at TestingFile.txt. In order to run your code type in the 
    following command on a terminal:
        
        python isAProject.py

Initializing a variable:

    all variables must be created at the begining of the file
    
    Initializing an integer variable:
        Dec var = 3
    
    Initializing a string:
        Str var = "fallas"
    
### List of possible operations:
    
    INPUT
        This will input a value into the accumulator.
        
    OUTPUT
        Will ouput a value. 
        
    HALT
        Stops the program.
        
    func functionName :
    
    end
        This is the syntax for creating a function. Remember to state 'func'
            because that is the key that initializes the function. Instead of 'functionName
            state your own function name. NOTE: Don't forget to add a space after 
            'functionName' otherwise you will get a syntax error. The 'end' keyword
            states the end of the function.
            
    
    ADD 
        This will add two values together and put the sum in the accumulator.
        Ex: 
            ADD val1 val2
            
        NOTE: This operation would substitute anything in the accumulator to the new result.
        
    SUBT
        Subtracts two values and puts the result in the accumulator.
        
            SUBT val1 val2
            
        NOTE: This operation would substitute anything in the accumulator to the new result.
    
    MULT
        Multiplies two values together and puts the result in the accumulator.
        
            MULT val1 val2
            
        NOTE: This operation would substitute anything in the accumulator to the new result
    
    DIV
        Divides two values and the result is inserted into the accumalator.
            
            DIV val1 val2
        
        NOTE: This operation would substitute anything in the accumalator to the result.
        
    STORE
        Will substitute the value in the variable with the current value in the accumalator.
        
    LOAD
        Will load the given variable into the accumalator.
        
            Example : LOAD var1
        
        NOTE: This will replace anything in the accumalator with the loaded value.
        
    <, > , ==, !=
        Comparison operators. This will need two values on each side.
        
        <
            
            val1 < val2
            Returns true if val1 is less than val2.
            Otherwise, it returns false.
        >
        
            val1 > val2
            Returns true if val2 is greater than val1.
            Otherwise, it returns false.
        
        ==
        
            val1 == val2
            Returns true if val1 is equal to val2.
            Otherwise, it returns false.
        
        !=
        
            val1 != val2
            Returns true if val1 does not equal to val2.
            
        
        
    STOREI // should we have STOREI?
    // It hasn't been implemented
    
        
        
        Loop(start : end)
        
        ARRAY:
            ARRAY_NAME.add(value)
            ARRAY_NAME.at(location)
            ARRAY_NAME.size()
            ARRAY_NAME.replace(place : value)
            ARRAY_NAME.remove(location)
