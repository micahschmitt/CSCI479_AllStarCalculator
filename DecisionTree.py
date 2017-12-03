import numpy as np
from sklearn import cross_validation
from sklearn import tree
import graphviz


# %% Read data from the file
A = np.loadtxt('parsed_cleaned_stats.txt', delimiter=' ')
#Get the classes (-1, 1)
y = A[:, 0]
#Remove classes from data
A = A[:, 1:]

decisionTree = tree.DecisionTreeClassifier()
decisionTree.fit(A, y)

print('Results: ')
#Performs and prints k-folds validation
accuracy = cross_validation.cross_val_score(decisionTree, A, y, cv=10, scoring='accuracy').mean()
precision = cross_validation.cross_val_score(decisionTree, A, y, cv=10, scoring='precision').mean()
recall = cross_validation.cross_val_score(decisionTree, A, y, cv=10, scoring='recall').mean()
print("Average Accuracy: ")
print(accuracy)
print("Precision: ")
print(precision)
print("Recall: ")
print(recall)

dot_data = tree.export_graphviz(decisionTree, out_file=None)
graph = graphviz.Source(dot_data)
graph.render("decision_tree")
