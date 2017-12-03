import numpy as np
from sklearn import linear_model
from sklearn import cross_validation

print("Logistic Regression Algorithm")

stats = np.loadtxt('parsed_cleaned_stats.txt', delimiter=' ')
y = stats[:, 0]
stats = stats[:, 1:]

logreg = linear_model.LogisticRegression()
logreg.fit(stats, y)

print("Results: ")

accuracy = cross_validation.cross_val_score(logreg, stats, y, cv=10, scoring='accuracy').mean()
precision = cross_validation.cross_val_score(logreg, stats, y, cv=10, scoring='precision').mean()
recall = cross_validation.cross_val_score(logreg, stats, y, cv=10, scoring='recall').mean()

print("Average Accuracy: ")
print(accuracy)
print("Precision: ")
print(precision)
print("Recall: ")
print(recall)