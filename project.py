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

def formula(tuples):
    newlist = []
    dictionary = {}
    newlist.append(tuples[0])
    tuples = tuples[1:]
    for tup in tuples:
        x = tup
        y = list(x)
        for i in range(len(tup)):
            if i == 0:
                pass
            elif i == 1:
                y[1] = int(x[1])*2
            elif i == 2:
                y[2] = int(int(x[2])*3)
            elif i == 3:
                y[3] = int(x[3])*5
        x = tuple(y)
        total_score = int(x[1]) + int(x[2]) + int(x[3])
        print(f'{x[0]}: {total_score}')
        dictionary[x[0]] = total_score
        newlist.append(x)
        print(dictionary)
        print({k: v for k, v in sorted(dictionary.items(), key = lambda item: item[1], reverse=True)})
        print()
    print(newlist)
    return dictionary

def updated_list(dictionary):
    with open('Testing.txt', 'w') as files:
        dictionary = {k: v for k, v in sorted(dictionary.items(), key = lambda item: item[1], reverse=True)}
        dictionary = str(dictionary)
        files.write(dictionary)
        files.close()

if __name__ == "__main__":
    main()
