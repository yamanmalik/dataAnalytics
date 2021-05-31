This program was a project completed for my Big Data Systems course. The files analyze the yelp data and generate statistics, visualizations, and edge lists. 
CSV Reader and Matplotlib libs were used. Programs are run using command line args where the yelp_business.csv or user csv is provided as well as the city to be analyzed. 
The yelp_business.csv and yelp_user.csv may be found at: https://www.kaggle.com/yelp-dataset/yelp-dataset/version/6

Sample runs:
dstats: 

	python3 dstats.py yelp_business.csv Toronto

dist-stast:

	python3 dstats.py yelp_business.csv Toronto

yelp-network:

	python3 yelp-network.py yelp_user.csv

graph-stats:

	 python3 graph-stats.py yelp-network.txt

(yelp-network.txt is generated from running yelp-network.py)

