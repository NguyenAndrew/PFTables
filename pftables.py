""" PFTables creates a fake table CSV file in Python """
import sys
import csv
import os
import errno
from faker import Faker
FAKE = Faker()

def main():
    """ Entry point of this script. This function is executed at the bottom of this script. """
    if len(sys.argv) != 2:
        print("python pftables.py fake_row_count -> Example: python pftables.py 10")
        return

    csv_row_count = int(sys.argv[1])
    csv_header, faker_executables = parse_input_csv()

    silent_remove('output.csv')
    with open('output.csv', 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(csv_header)

        for _ in range(csv_row_count):
            csv_writer.writerow(generate_fake_list(faker_executables))

### Helper Functions located below ###

def parse_input_csv():
    """ Returns the headers and the faker executables"""
    with open('input.csv') as input_file:
        csv_reader = csv.reader(input_file, delimiter=',')    
        csv_header = next(csv_reader)
        faker_executables = [
            'FAKE.' + function_name + '()'
            for function_name in next(csv_reader)
        ]
        return [csv_header, faker_executables]

def generate_fake_list(faker_executables):
    """ Returns an array with fake data """
    return [
        exec_and_return(executable) for executable in faker_executables
    ]

def exec_and_return(executable):
    """ Uses Python's exec command, and obtains its return value """
    # To understand this code: https://bugs.python.org/issue4831
    fresh_locals = {}
    exec('return_value = ' + executable, globals(), fresh_locals)
    return fresh_locals['return_value']

def silent_remove(filename):
    """ Remove the file silently if exists, for all scenarios toss an error """
    try:
        os.remove(filename)
    except OSError as error:
        if error.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occurred

### Execute the Main Function ###
if __name__ == '__main__':
    main()
