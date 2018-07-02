from Modules.QuantumClasses import *
from Modules.AuxiliaryClasses import *
from Modules import Perliminary
from Modules import Grapher

"""Main Running Function Everything runs from this file and links to a total of 5 other 
modules in the modules directory, there is alot of stuff so just to keep organised"""

def read_qubit_file():
    """
    Function to create Qubit File Object. Also asks how many tests are to
    be run so that different numbers of qubits can be easily compared without
    rerunning the entire program.    
    """
    number_of_tests = int(
        raw_input("Enter how many tests you would like to take place: "))
    qubit_file = QubitFile(number_of_tests)         # creates the file object by calling the class
    qubit_tests = qubit_file.choose_qubit_numbers() # runs method to choose qubit numbers for each test
    return qubit_tests, number_of_tests             # returns the list of tests and the amount chosen

def desired_state(qubit_number, choose_state, test):
    """
    Function for user to pick a desired state for grovers algorithm. This
    defaults to the middle state if the user does not wish to pick a state.
    
    :param qubit_number: The number of qubits which are being simulated.
    :param choose_state: Boolean to determine whether the state is being chosen manually or not.
    :param test: An int used to print the message about the default option at the correct point.
    """
    if choose_state == True:  
        while True: # infinite loop
           # prompts user to enter their desired value for the correct state 
           chosen_state = int(raw_input("Please enter desired state value: "))
           # exceptions to make sure the correct value is entered. 
           if chosen_state < 0:
               print "Desired state must be greater than one"
           elif chosen_state > 2 ** qubit_number:
               print "Desired state cannot exceed the total number number of states"
           else:
               print "State Chosen"
               break
    else: 
        chosen_state = int((2 ** qubit_number) / 2.0) 
        if test == 0:
            print "Default state chosen of half the number of states"
            #takes half of the total qubit states as the desired state
    return chosen_state

def quantum_loop(qubits, chosen_state, test, data_file, 
    figure_show_choice, figure_save_choice, calculate_or_manual):
    """
    Function to loop the qauntum computation algorithms and where
    the steps themselves for grover's algorithms are performed.
    
    :param chosen_state:  The state which is being searched for.
    :param test:          Number of simulations being performed.
    :param data_file:     Data file object where results are saved.
    :figure_show_choice:  If figures are displayed.
    :figure_save_choice:  If figures are saved.
    :calculate_or_manual: To run the simulation for a custom number of 
    cycles, instead of the optimal number.
    """
    start_time = time.time()
    grovers_register = GroversAlgorithm(qubits)
    grovers_register.hadamard_gate() # calls the hadamar gate method in the quantum register class
    if calculate_or_manual == True:
        cycles =  int(raw_input("Pleae enter the desired number of cycles: "))
    else:
        cycles = np.pi / 4 * np.sqrt(2 ** qubits) # calculates the number of cycles
        print "Approimate number of cycles to for optimal solution is : {}".format(np.round(cycles))
    for j in range(int(np.round(cycles))):
        print "Cycle {}".format(j + 1)
        grovers_register.measure_values(figure_show_choice, figure_save_choice, j)
        grovers_register.oracle(chosen_state)
        grovers_register.hadamard_gate()
        grovers_register.conditional_phase_shift()
        grovers_register.hadamard_gate()  
    result = grovers_register.measure_values(figure_show_choice, figure_save_choice, j)
    elapsed_time  = time.time() - start_time # calculates total time of test
    if data_file != None: # writes the parameters and results to file if desired
        data_file.write_to_file(qubits, elapsed_time, 
        chosen_state, test, result)

def main():
    """
    The function which runs every aspect of the program.
    """
    qubit_container, number_of_tests = read_qubit_file() # runs function to create qubit file
    print "\n Perliminary Questions: \n"
    data_file, figure_show_choice, figure_save_choice, choose_state, calculate_or_manual = Perliminary.preliminary_questions()
    for test in range(number_of_tests):
        print "Test Number : {} for {} Qubits".format(test + 1, qubit_container[test])
        chosen_state = desired_state(qubit_container[test], choose_state, test) # runs function for user to choose desired state
        quantum_loop(qubit_container[test], chosen_state, test, 
        data_file, figure_show_choice, figure_save_choice, calculate_or_manual)  # runs made qunatum computing loop           
    Grapher.running_grapher()   #only runs grapher if multiple tests performed
    print "End of programme"
main()
