import numpy as np
import scipy
from sklearn.cluster import KMeans

print "K Means Algorithm"

#Read in data from the file
stats = np.loadtxt('parsed_cleaned_stats.txt', delimiter=' ')

km = KMeans(n_clusters=3, init=stats, n_init=1)

#print km
#centers = km.centroid
print km# centers
