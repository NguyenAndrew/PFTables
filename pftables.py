""" PFTables creates a fake table CSV file in Python """
import csv
import errno
import os
import random
import sys
from tqdm import tqdm
from faker import Faker
FAKE = Faker()

def main():
    """ Entry point of this script. This function is executed at the bottom of this script. """
    if len(sys.argv) != 2:
        print("python pftables.py fake_row_count -> Example: python pftables.py 10")
        return

    csv_row_count = int(sys.argv[1])
    csv_header, array_or_executables_list = parse_input_csv()

    print("Generating output.csv...")
    silent_remove('output.csv')
    with open('output.csv', 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(csv_header)
        for _ in tqdm(range(csv_row_count)):
            csv_writer.writerow(generate_fake_list(array_or_executables_list))
    print("... and finished! Created output.csv with " + str(csv_row_count) + " fake data rows.")

### Helper Functions located below ###

def parse_input_csv():
    """ Returns the headers and the faker executables"""
    with open('input.csv') as input_file:
        csv_reader = csv.reader(
            input_file,
            quotechar='"',
            delimiter=',',
            quoting=csv.QUOTE_ALL,
            skipinitialspace=True)
        csv_header = next(csv_reader)
        array_or_executables_list = [
            make_array_or_function_string(function_name)
            for function_name in next(csv_reader)
        ]
        return [csv_header, array_or_executables_list]

def make_array_or_function_string(cell):
    """
    Either selects an array element at random, or
    create the faker function string, depending on the input format
    """
    if (cell.startswith('[') and cell.endswith(']')):
        return cell[1:-1].split(' | ') # Removes the brackets before split

    if (cell.startswith('{') and cell.endswith('}')):
        return cell[1:-1]

    return 'FAKE.' + cell

def silent_remove(filename):
    """ Remove the file silently if exists, for all scenarios toss an error """
    try:
        os.remove(filename)
    except OSError as error:
        if error.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occurred

def generate_fake_list(faker_executables):
    """ Returns an array with fake data """
    return [
        select_array_or_exec_function(executable) for executable in faker_executables
    ]

def select_array_or_exec_function(cell):
    """
    Either selects an array element at random, or
    executes the function, depending on the input format
    """
    if isinstance(cell, list):
        return random.choice(cell)

    return exec_and_return(cell)

def exec_and_return(executable):
    """ Uses Python's exec command, and obtains its return value """
    # To understand this code: https://bugs.python.org/issue4831
    fresh_locals = {}
    exec('return_value = ' + executable, globals(), fresh_locals)
    return fresh_locals['return_value']

### Custom Functions (Hooks) ###

def first_custom_function_example():
    """ Code Used to Demonstrate Hooks """
    return random.choices(
        population=['Fire', 'Earth', 'Wind', 'Water'],
        weights=[0.4, 0.3, 0.1, 0.2],
        k=1
    )[0]

def second_custom_function_example(choices):
    """ Code Used to Demonostrate Hooks (with parameters) """
    return random.choice(choices)

### Execute the Main Function ###
if __name__ == '__main__':
    main()
