"""
functions to read the a CSV file
and put it into a dictionary
"""

import csv

def read_palette_from_file(palette_filename):
    """
    read the palette from the csv file.
    Each row is a key and an RGB triple.  Make that RGB triple
    into a TUPLE and then put into a dictionary with the key.
    """

    my_dict = dict()

    with open(palette_filename, 'r') as infile:
        my_reader = csv.reader(infile)
        for row in my_reader:
            key = int(row[0])
            #print(key)
            red = int(row[1])
            green = int(row[2])
            blue = int(row[3])
            tuple = (red, green, blue)
            #print(key, '=', tuple)

            my_dict[key] = tuple
    return(my_dict)
