THIS FILE INCLUDES A LIST OF ALL FILES THAT ARE PART OF THE PROGRAM:
(1) _init_.py 
(2) AuxillaryClasses.py
(3) Grapher.py
(4) Imports.py
(5) Perliminary.py
(6) QuantumClasses.py
(7) QuantumRun.py

(1) __init__.py:
This file allows the interpreter to recognize any other python files in 
the directory as a library, so it can be imported easily from another directory.

(2) AuxillaryClasses.py:
- Contains 2 Classes - 
Contains classes that govern the file handling in the programme. This includes 
reading and modifying the file that contains all the qubit numbers to be used in 
the tests. As well as a file that is used to create a file for the data from tests.

(3) Grapher.py:
Modular file used to create graph visualisations from the data file created in the 
code. 

(4) Imports.py:
This file is used as a central point for all the imports in the programme to save on 
reapeated lines in different files. Also it is an easy way to keep track of what 
libraries are being used.

(5) Perliminary.py:
Handles the majority of the user inputs for the programme with a function that also 
handles custom exceptions.

(6) QuantumClasses.py:
- Contains 2 Classes -
Contains the classes for both creating the class for the quantum register and the 
implementation of Grover's Algorithm. This contains method for plotting visualisations
and saving to the chosen directory "Figures".

(7) QuantumRun.py:
The main running file, all the other files lead to this one. So a user does not have to 
be concerned with what the others are doing as this govern the whole programme. 

AND THE DIRECTORIES
(1) Data Files
(2) Documentation
(3) Figures
(4) Modules
(5) QubitFile

(1) Data Files:
Holds all the saved data files for a run of the programme if the user decides they want 
5) file)

(2) Documentation:
Contains the python documentation files in html that summarise the parameters contained in
the function and class for the programme.

(3) Figures:
Holds all the saved figures for a run of the programme if the user decided they want to(
Perliminary.py(5) file)

(4) Modules:
Contains all the coded libraries for the programme to run files (1) through (6)

(5) QubitFile:
Contains the file that holds the sequence of numbers for choosing qubit amounts.

