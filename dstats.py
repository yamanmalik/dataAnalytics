# Author: Yaman Malik
# Data Analytics Project that analyzes a yelp dataset

import csv, argparse
import sys

# setting up parser
parser = argparse.ArgumentParser()
parser.add_argument("a")
parser.add_argument("b")
args = parser.parse_args()




#reading file
print("Start of program")
filename = args.a
city = args.b
print('File Read: '+ filename)
print('City: '+ city)


with open(filename, encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile)
    totalRows = 0

# initializing
    numOfBus = 0
    avgStarTotal = 0
    avgStar = 0
    numOfRes = 0
    reviewTotal = 0
    reviewBusTotal = 0
    reviewBusCount = 0
    reviewCount = 0
    avgStarRes = 0
    avgStarResTotal = 0

# reading each row and performing requested calculations
    for row in reader:
        totalRows = totalRows+1

        if row['city'] == city or row['city'] == city.lower():
            numOfBus = numOfBus +1
            avgStarTotal = avgStarTotal + float(row['stars'])
            reviewTotal = reviewTotal + int(row['review_count'])
            if 'Restaurants' in row['categories']:
                numOfRes = numOfRes + 1
                reviewBusTotal = reviewBusTotal + int(row['review_count'])
                avgStarResTotal = avgStarResTotal + float(row['stars'])

# calculations
    reviewCount = round(reviewTotal / numOfBus, 2)
    reviewBusCount = round(reviewBusTotal / numOfRes, 2)
    avgStar = round(avgStarTotal / numOfBus, 2)
    avgStarRes = round(avgStarResTotal / numOfRes, 2)


# printing
    print('numOfBus: '+ str(numOfBus))
    print('avgStars: ' + str(avgStar))
    print('numOfRestaurants: ' + str(numOfRes))
    print('avgStarsRestaurants: ' + str(avgStarRes))
    print('avgNumOfReviews: ' + str(reviewCount))
    print('avgNumOfReviewsBus: ' + str(reviewBusCount))