"""
Standalone functions for manupulating data files. The choose graph functions exist 
just so expanding the file to incorproate more grapher would be easy as you add its
name and the function. 
"""

from Imports import *

def choose_file():
    """
    Function to choose which file to graph by displaying the data files available.
    """
    x = os.listdir(os.path.abspath("Data Files"))
    if len(x) == 0:
        print "No Data Points to compare"
        print "Please make file by using the save to file feature"
    else:
        print "Choose File"
        file_directory = os.path.abspath("Data Files")
        for i, item in enumerate(x):
            print "{} : Results on Date {}".format(i + 1, item.replace("Test Results",""))
        while True:
            file_to_use = int(raw_input("Enter number that corresponds to desired file: "))
            if file_to_use > len(x):
                print "Enter a valid number inside the amount provided"
            elif file_to_use < 1:
                print "Enter sensible value"
            else:
                break
        file_name = x[file_to_use - 1]
        file_data = np.genfromtxt(
            os.path.join(file_directory, file_name), dtype=float, skip_header=1)
        output = [file_data, file_name]
        shape_of_array = str(file_data.shape)
        if  shape_of_array == "(9L,)":
            print "File contains only one test so no comparisons can be plotted"
            output =  False
        return output

def choose_graph(file_data, file_name):
    """
    Function to choose which graphing function to use. This is written 
    to be easily expandable.
    
    :param file_data: Contains the data which is to be plotted.
    :param file_name: The name of the data file which is being plotted.
    """
    grapher_functions = ["Time Comparison Graph"]
    print "Graphs to choose from:"
    for i, item in enumerate(grapher_functions):
        print "{}: {}".format(i + 1, item)
    while True:
        graph_number = int(raw_input("Enter number for desired plot: "))
        if grapher_functions[graph_number - 1] == "Time Comparison Graph":
            times_graph(file_data, file_name)
            break
        else:
            print "please enter a valid number"

def times_graph(data, file_name):
    """
    The first graphing mode, a function to plot computation times 
    against qubit numbers for any file chosen. This figure is then saved
    in the correct directory.
    """
    save_directory = os.path.abspath("Figures")
    save_name = "Time Comparison for Date {}.png".format(
      file_name.replace(".txt",""))
    plt.figure()
    plt.title("Computation Times Against Qubits For File {}".format(
            file_name.replace(".txt","")))
    plt.plot(data[:,0], data[:,4])
    plt.xlabel('Number of Qubits')
    plt.ylabel('Computation Times / Seconds')
    print "Saving Figure to Figures Directory"
    plt.savefig(os.path.join(save_directory, save_name))
    plt.show()

def running_grapher():
    """
    Function to let the user decide whether they wish to plot data files.
    """
    while True:
        run = raw_input("Run graphing module? 'Yes' or 'No': ")
        if run.lower() == "yes": 
            output = choose_file()
            if output == False:
                break
            else:
                choose_graph(output[0], output[1])
            break
        elif run.lower() == "no":
            break
        else:
            print "Please enter a valid answer of yes or no"


    


    
        
        


    
