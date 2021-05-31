# Author: Yaman Malik
# Data Analytics Project that analyzes a yelp dataset


import csv, argparse
import sys

# setting up parser
parser = argparse.ArgumentParser()
parser.add_argument("a")


args = parser.parse_args()


# taking file names
print("Start of program")
filename = args.a

print('File Read: ' + filename)

csv.field_size_limit(2147483647)

userSet = set()
output = open('yelp-network.txt', 'w')

with open(filename, encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile)
    totalRows = 0

# checking each row, if user is already in list, then the friendship already existed
# if the user is not in the list, print the friendship as an edge
    for row in reader:
        if row['friends'] != 'None':

            currentUser = row['user_id']
            userSet.add(currentUser)

            friends = row['friends'].split(', ')
            for word in friends:
                    if word in userSet:
                        continue

                    else:
                        output.write(currentUser + ' ' + word + '\n')





