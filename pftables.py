""" PFTables creates a fake table CSV file in Python """
import csv
import os
import errno
from faker import Faker
FAKE = Faker()

def main():
    """ Entry point of this script. This function is executed at the bottom of this script. """
    silentremove('output.csv')
    csv_header = ['Company', 'Color']
    csv_row_count = 10

    with open('output.csv', 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(csv_header)

        for _ in range(csv_row_count):
            csv_writer.writerow(generate_fake_list())

### Helper Functions located below ###

def generate_fake_list():
    """ Returns an array with fake data """
    returned_list = [
        FAKE.company(),
        FAKE.color_name()
    ]
    return returned_list

def silentremove(filename):
    """ Remove the file silently if exists, for all scenarios toss an error """
    try:
        os.remove(filename)
    except OSError as error:
        if error.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occurred

### Execute the Main Function ###
if __name__ == '__main__':
    main()
