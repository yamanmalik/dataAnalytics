# Author: Yaman Malik
# Data Analytics Project that analyzes a yelp dataset


import csv, argparse
import sys
import matplotlib.pyplot as plt

# setting up parser
parser = argparse.ArgumentParser()
parser.add_argument("a")
parser.add_argument("b")
args = parser.parse_args()

# reading file and city name

print("Start of program")
filename = args.a
city = args.b
print('File Read: ' + filename)
print('City: ' + city)

counts = dict()
totalReviews = dict()
totalStars = dict()

# opening file
with open(filename, encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile)
    totalRows = 0

    # checking if city matches entered city, then checking if restaurants is present in category
    for row in reader:
        if row['city'] == city or row['city'] == city.lower():
            totalRows = totalRows + 1
            if 'Restaurants' in row['categories']:

                # splitting categories into list and checking if it is dict, if not, it is added to dict, if it is,
                # then count of occurences increased, similar process for total reviews and total stars

                types = row['categories'].split(';')
                for word in types:
                    if word in counts:
                        counts[word] += 1
                        totalReviews[word] += int(row['review_count'])
                        totalStars[word] += float(row['stars'])
                    else:
                        counts[word] = 1
                        totalReviews[word] = int(row['review_count'])
                        totalStars[word] = float(row['stars'])
# sorting the dicts

sorted_category = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
sorted_stars = dict(sorted(totalStars.items(), key=lambda item: item[1], reverse=True))
sorted_reviews = dict(sorted(totalReviews.items(), key=lambda item: item[1], reverse=True))

#removing first restaurants entry, do not want that in data

del sorted_category['Restaurants']
del sorted_stars['Restaurants']
del sorted_reviews['Restaurants']



#part 1

print('restaurantCategoryDist: ')
for k, v in sorted_category.items():
    print(k,':',v)

# part 2
print('\nRestaurantReviewDist: ')

for k, v in sorted_reviews.items():
    print(k,':',v,':',round(float(sorted_stars[k] / sorted_category[k]), 1))


categories = list(sorted_category.keys())
frequency = list(sorted_category.values())

#part 3, top 10 items in matplotlib bar graph popup, window must be closed to end program
categories = categories[:10]
frequency = frequency[:10]


plt.bar(range(10), frequency, tick_label=categories)
plt.show()
