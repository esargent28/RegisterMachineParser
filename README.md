# Register Machine Parser
##### Erik Sargent (esargent28)

A Python-based parser that reads an encoding of a register machine from an input file and creates an object that can run
said register machine on various inputs.

### Input File Format
The input files start by specifying the total number of registers, as well as the input and output registers. To do this, start lines with the tags '#REGISTERS', '#INPUT', and '#OUTPUT', respectively. From there, specify all states / instructions, each on its own line, enclosed by lines with '#BEGIN STATES' and '#END STATES'. Each state (aside from the **halt** instruction) is either of the form **inc r s** or **dec r s t**.
- **inc** instructions increment register **r** by 1 and then go to state **s**.
- **dec** instructions try to decrement register **r** by 1. If it's nonzero, then the decrement is successful and it goes to state **s**. Otherwise, it goes to state **t**.
- The convention of the evaluator / parser is that there is only ever 1 **halt** instruction, and that the **halt** instruction is the machine's last one.

For examples, look at the _addition.txt_ and _multiplication.txt_ files in the _examples_ folder.

### Use of register_machine.py
The register_machine.py file contains a RegisterMachine class. To create a register machine based on a specific
input file ./path/to/infile.txt, you simply need to construct an instance of this class based on said file
-- e.g. 'machine = RegisterMachine("./path/to/infile.txt")'. The input file specifies the number of arguments it
takes and how many outputs it produces, so to run your machine, you just need to call the class's 'run' method on
the arguments you want to pass in -- e.g. 'results = machine.run(3, 12, 17)'.

**Note:** The inputs to your register machine must be non-negative numbers. Negative numbers can cause infinite
looping, especially when involving _dec_ instructions.
