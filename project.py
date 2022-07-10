#!/user/bin/env python3
import re
import csv
from csv import reader
def main():

# open file in read mode
def read_file():
    with open('C:\\Users\Jorda\OneDrive\Desktop\VSCode\\New folder\Capstone\Capstonespreadsheet.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Get all rows of csv from csv_reader object as list of tuples
        list_of_tuples = list(map(tuple, csv_reader))
        # display all rows of csv
        return list_of_tuples



if __name__ == "__main__":
    main()
