import numpy as np
from sklearn import cross_validation
from sklearn.naive_bayes import GaussianNB

FOLDS = 10

# %% Read data from the file
A = np.loadtxt('class_first_parsed_cleaned_stats.txt', delimiter=' ')
#Get the classes (-1, 1)
y = A[:, 0]
#Remove classes from data
A = A[:, 1:]

nb = GaussianNB()
nb.fit(A, y)

print('Results: ')
#Performs and prints k-folds validation
scores = cross_validation.cross_val_score(nb, A, y, cv=10, scoring='accuracy')
print(scores)
print("Average: ")
print(scores.mean())
