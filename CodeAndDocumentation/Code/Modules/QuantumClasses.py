"""File that contians the classes necessary to simulate the quantum register"""

from Modules.Imports import *

class QuantumRegister(object):
    """
    Class for initialsing the quantum register. Included are general methods
    to implement a Hadamard (H) gate and to measure and calculate probabilities.
    """
    def __init__(self, number_of_qubits):
        """
        Initialises a quantum register with an array of qubit states.
        
        :param number_of_qubits: total number of qubits being simulated
        :param states: total number of quantum states
        :s_qubits: array of qubit states
        """
        self.qubits = number_of_qubits 
        self.states = 2 ** self.qubits 
        self.s_qubits = np.zeros(self.states, dtype=complex) 
        self.s_qubits[0] = 1.0 # set first index to 1

    def hadamard_gate(self):
        """Method to implement the hadamard gate."""
        qubitstates = [1] * self.qubits
        h_matrix = 1. / np.sqrt(2) * np.array([[1., 1.], [1., -1.]])
        mul = np.array([1])
        for i in reversed(qubitstates):
            if i:
                mul = np.kron(h_matrix, mul)
        self.s_qubits = mul.dot(self.s_qubits)
        return self

    def measure_values(self, figure_show_choice, figure_save_choice, i):
        """
        Method to calculate and plot the probabilities.
        
        :param figure_show_choice: This is included to reduce memory usage 
        by only performing these operations if user selects.
        :param figure_save_choice: Option to initialise figure objects if 
        user selects.
        """
        probabilities = np.absolute(self.s_qubits) ** 2
        save_directory = os.path.abspath("Figures")
        file_name = "{} Qubits - Cycle {}.png".format(self.qubits, i + 1)
        
        if figure_show_choice == True or figure_save_choice == True: 
            print "Plotting Function"  # test line and piece of mind that the conditional works
            f = interp1d(range(1,len(probabilities)+1), probabilities, kind='cubic')
            plt.figure(figsize=(20,10))
            plt.title("Probabilities Grover's Algortithm")
            plt.plot(range(1, len(probabilities)+1), probabilities, 'ro', range(1, len(probabilities)+1),
                     f(range(1, len(probabilities)+1)), '--')
            plt.axis([1, len(probabilities), -0.1, 1.1])
            plt.text(max(xrange(len(probabilities)), key=probabilities.__getitem__)+1, max(probabilities)+0.05, 
                     "Probability="+str(round(max(probabilities), 3))+", Most probable State="+str(
                         max(xrange(len(probabilities)), key=probabilities.__getitem__)+1)+")")
        if figure_save_choice == True:
            plt.savefig(os.path.join(save_directory, file_name))
        if figure_show_choice == True:
            plt.show()
        plt.close()
        return np.random.choice(len(probabilities), p = probabilities.flatten())

class GroversAlgorithm(QuantumRegister):
    """
    Class to use grover's algorithm which extends the Quantum Register
    to contain methods specific to this algorithm, namely the conditional phase shift
    and oracle operator.
    """
    def conditional_phase_shift(self):
        """
        Updates the qubit array by performing the conditional phase shift gate.
        """
        for i in range(1, self.states):
            self.s_qubits[i] = - 1 * self.s_qubits[i]
        return self
    
    def oracle(self, correct_state):
        """
        Updates the the qubit array at the correct state index in order
        to implement the oracle operator."
        """
        self.s_qubits[correct_state] = -1 * self.s_qubits[correct_state]
        return self

# class ShoresAlgorithm(QuantumRegister):
