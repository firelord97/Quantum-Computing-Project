from Modules.Imports import *

class QubitFile(object):
    """
    Class To Create the Qubit File Object from the text file of available
    qubits.
    
    :param number_of_tests: How many tests to be performed. Allows easy
    comparison of number of qubits as this negates the need for the script
    to be run multiple times.
    """
    def __init__(self, number_of_tests):
        self.dir_path = os.path.abspath("QubitFile") # define file path
        self.qubit_amounts = np.genfromtxt(
            os.path.join(self.dir_path, "Qubit_amounts.txt"), dtype=int)
        self.number_of_tests = number_of_tests
        self.qubit_tests = []
        self.index = 0

    def print_numbs(self):
        """
        Method to print contents of qubit amounts file
        """
        print "These are the numbers of qubits that can be chosen from"
        print "More choices can be added by editing the Qubit_amounts.txt file"
        print "in the QubitFile Directory"
        for item in self.qubit_amounts:
            print "|{}".format(item),
        print "\n"
        
    def choose_qubit_numbers(self):
        """
        Method to choose what amount of qubits to be used for each test.
        """
        self.print_numbs()
        for i in range(self.number_of_tests):
            while True:
                desired_q_amount = int(
                    raw_input("Test {}: Enter number of qubits for list: ".format(i + 1)))
                boolean = self.check_number(desired_q_amount)
                if boolean == True:
                    self.qubit_tests.append(desired_q_amount)
                    break
        print "All Qubit Values Have Been Chosen"
        return self.qubit_tests
            
    def check_number(self, desired_q_amount):
        """
        Method to check if the number of qubits is above a certain value
        
        :param desired_q_amount: an int used to determine whether the long
        computation time warning is displayed.
        """
        if desired_q_amount >= 10: # if amount of qubits chosen for a test is more or equal to 10 
            return self.number_warning() # then run the warning function
        elif desired_q_amount < 10: 
            return True
        elif desired_q_amount < 1 or desired_q_amount > len(self.qubit_amounts):
            return False 

    def number_warning(self):
        """
        Method to warn user about computation times.
        """
        if self.index == 0:  # it ensures this function sequnece is called only once 
            print "This amount of qubits requires a large amount of computational power"
            while True:
                check_answer = raw_input(
                    "Continue with qubit numbers above 10? 'Yes' or 'No': ")
                response = self.mod_data(check_answer)
                if response == None:
                    print "Please enter a valid answer of 'yes or 'no'"
                elif response == True:
                    return True
                    break
                else:
                    return False
        else: 
            return True

    def mod_data(self, check_answer):
        """
        Method to modify the numbers depending on what is chosen.
        """
        if check_answer.lower() == "yes":
            self.index += 1 # increases index so this function sequence can only happen once
            print "Indicies above 10 are now enabled by default"
            return True
        elif check_answer.lower() == "no":
            self.index += 1
            indexes_to_remove = [i for i in range(9, len(self.qubit_amounts))]
            # removes corresponding indexes for higher amounts of qubits
            self.qubit_amounts = np.delete(self.qubit_amounts, indexes_to_remove)
            print "Choices of 10 and above have now been removed"
            self.print_numbs()
            return False
        else:
            return None # used to show something invalid was enteres as answer

class DataFile(object):
    """
    Class to create a data file to save simulation results.
    
    :param save_path: The directory in which the data file will be saved.
    :param data_file: The name of the data file including the time when 
    the simulation began.
    """
    def __init__(self):
        self.save_path = os.path.abspath("Data Files")
        self.data_file = "Test Results {}.txt".format(
            datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))  
            
    def write_to_file(self, 
        qubit_number, elapsed_time, chosen_state, test, result):
        """
        Method to write data to file. 
        
        :param qubit_number: Number of qubits which are being simulated.
        :param elapsed_time: The time it took for the simulation to run.
        :param chosen_state: The state which was desired to be found.
        :param result:       The state which the simulation found.
        """
        with open(os.path.join(self.save_path, self.data_file), "a+") as quantum_file:
            if test == 0:
                 quantum_file.write("Number Of Qubits | Number of States | Elapsed Time | State Chosen | State Measureed")
            quantum_file.write("\n{} | {} | {} | {} | {}".format(
                qubit_number, 2 ** qubit_number, elapsed_time, chosen_state, result))
