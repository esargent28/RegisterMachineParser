# Register Machine Parser
##### Erik Sargent (esargent28)

A Python-based parser that reads an encoding of a register machine from an input file and creates an object that can run
said register machine on various inputs.

### Input File Format
(TODO): Explain input file format

### Use of register_machine.py
The register_machine.py file contains a RegisterMachine class. To create a register machine based on a specific
input file ./path/to/infile.txt, you simply need to construct an instance of this class based on said file
-- e.g. 'machine = RegisterMachine("./path/to/infile.txt")'. The input file specifies the number of arguments it
takes and how many outputs it produces, so to run your machine, you just need to call the class's 'run' method on
the arguments you want to pass in -- e.g. 'results = machine.run(3, 12, 17)'.

**Note:** The inputs to your register machine must be non-negative numbers. Negative numbers can cause infinite
looping, especially when involving _dec_ instructions.
