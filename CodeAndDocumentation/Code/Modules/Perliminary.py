from AuxiliaryClasses import DataFile

"""Standalone for answering the various questions for how the programme should be run, it
is to keep the main file organised and decrease duplicated code, while still having error handlers"""

def preliminary_questions():
    """
    Function that contains all perliminary questions for the programme.
    These are whether a data file is created, figures are displayed, 
    figures are saved, the desired state is chosen, the number of cycles
    is chosen manually or optimised. Each question has its own error 
    handler that is by the while true loop.
    """
    results = []
    
    while True:
        create_file = [raw_input("Create file for data? 'Yes' or 'No': "), 1]
        result = answer_decider(create_file)
        if result[1] == 1:
            results.append(result[0])
            break
    while True:
        show_figures = [raw_input("Display figures? 'Yes' or 'No': "), 2]
        result = answer_decider(show_figures)
        if result == True or result == False:
            results.append(result)
            break
    while True:
        save_figures = [raw_input("Save figures? 'Yes' or 'No': "), 3]
        result = answer_decider(save_figures)
        if result == True or result == False:
            results.append(result)
            break
    while True:
        choose_state = [raw_input("Choose desired state(s) for tests? 'Yes' or 'No': "), 4]
        result = answer_decider(choose_state)
        if result == True or result == False:
            results.append(result)
            break
    while True:
        calculate_or_manual = [raw_input("Input number of cycles manually?: 'Yes' or 'No': "), 5]
        result = answer_decider(calculate_or_manual)
        if result == True or result == False:
            results.append(result)
            break
    return results

def answer_decider(parameter):
    """
    Function to decide which question is being asked and act accordingly.
    Also is used to sanitise inputs.
    """
    if parameter[0].lower() == "yes":
        if parameter[1] == 1:
            data_file = DataFile()
            return data_file, 1
        else:
            print "Feature Enabled"  #Shows that the feature will be used
            return True
    elif parameter[0].lower() == "no":
        if parameter[1] == 1:
            data_file = None
            return data_file, 1
        else:
            print "Feature Disabled" #Shows that the feature will not be used
            return False
    else:
        print "Please enter a valid answer of yes or no"
