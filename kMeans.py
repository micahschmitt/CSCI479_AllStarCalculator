import numpy as np
from sklearn import cross_validation
from sklearn.cluster import KMeans, MiniBatchKMeans

print "K Means Algorithm"

#Read in data from the file
stats = np.loadtxt('parsed_cleaned_stats.txt', delimiter=' ')

y = stats[:, 0]
stats = stats[:, 1:]

mb = MiniBatchKMeans(n_clusters=2)
km = KMeans(n_clusters=2)
mb.fit(stats, y)
km.fit(stats, y)#, init=stats, n_init=1)
#km.transform(stats)

accuracy1 = cross_validation.cross_val_score(km, stats, y, cv=10, scoring='accuracy').mean()
accuracy2 = cross_validation.cross_val_score(mb, stats, y, cv=10, scoring='accuracy').mean()
#precision = cross_validation.cross_val_score(km, stats, y, cv=10, scoring='precision').mean()

print "Results: "
print
#print scores
print 
print "Average accuracy kmeans: "
print accuracy1
print "Average accuracy minibatchkmeans: "
print accuracy2
#print "Average precision: "
#print precision
#print km
#centers = km.centroid
#print km# centers
