# Author: Yaman Malik
# Data Analytics Project that analyzes a yelp dataset


import csv, argparse
import sys

# setting up parser
parser = argparse.ArgumentParser()
parser.add_argument("a")
args = parser.parse_args()

# csv.field_size_limit(sys.maxsize)

print("Start of program")
filename = args.a
print('File Read: ' + filename)

output = open('nodeDegreeDist.txt', 'w')

totalRows = 0
nodes = dict()
csv.field_size_limit(2147483647)

# reading file row by row
with open(filename) as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        totalRows += 1
        users = row[0].split(' ')

# if user is in nodes dict, increase degree, if not add to dict with degree of one
        for word in users:
            if word in nodes:
                nodes[word] += 1

            else:
                nodes[word] = 1

totalDegree = sum(nodes.values())
avgDegree = round(float(totalDegree) / float(len(nodes)), 2)

print('nodes: |' + str(len(nodes)) + '| edges: |' + str(totalRows)+'|')


# part2: printing node degree dist

sorted_nodes = dict(sorted(nodes.items(), key=lambda item: item[1], reverse=True))

for k, v in sorted_nodes.items():
    output.write(k + ':' + str(v) + '\n')

# part3: printing average node degree

print('avgNodeDegree: ' + str(avgDegree))
