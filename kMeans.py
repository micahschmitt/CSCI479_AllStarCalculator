import numpy as np
from sklearn import cross_validation
from sklearn.cluster import KMeans, MiniBatchKMeans

print "K Means Algorithm"

#Read in data from the file
stats = np.loadtxt('parsed_cleaned_stats.txt', delimiter=' ')

y = stats[:, 0]
stats = stats[:, 1:]

km = KMeans(n_clusters=2)
km.fit(stats, y)#, init=stats, n_init=1)

accuracy = cross_validation.cross_val_score(km, stats, y, cv=10, scoring='accuracy').mean()
precision = cross_validation.cross_val_score(km, stats, y, cv=10, scoring='precision').mean()
recall = cross_validation.cross_val.score(km, stats, y, cv=10, scoring='recall').mean()

print "Results: "
print
#print scores
print 
print "Average accuracy: "
print accuracy
print "Average precision: "
print precision
print "Average recall: "
print recall
#print "Average precision: "
#print precision
#print km
#centers = km.centroid
#print km# centers
