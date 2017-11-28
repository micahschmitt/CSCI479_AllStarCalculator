import numpy as np
from sklearn import cross_validation
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import precision_score, accuracy_score, make_scorer

FOLDS = 10

# %% Read data from the file
A = np.loadtxt('parsed_cleaned_stats.txt', delimiter=' ')
#Get the classes (-1, 1)
y = A[:, 0]
#Remove classes from data
A = A[:, 1:]

lda = LinearDiscriminantAnalysis()
lda.fit(A, y)
lda.transform(A)

print('Results: ')
#Performs and prints k-folds validation
accuracy = cross_validation.cross_val_score(lda, A, y, cv=10, scoring='accuracy').mean()
precision = cross_validation.cross_val_score(lda, A, y, cv=10, scoring='precision').mean()
recall = cross_validation.cross_val_score(lda, A, y, cv=10, scoring='recall').mean()
print("Average Accuracy: ")
print(accuracy)
print("Precision: ")
print(precision)
print("Recall: ")
print(recall)
