import numpy

trainingFile = "train.txt"
testingFile = "test.txt"
Xtrain = numpy.loadtxt(trainingFile)
n = Xtrain.shape[0]
d = Xtrain.shape[1] - 1

# Training... Collect mean and standard deviation for each dimension for each class..
# Also, calculate P(C+) and P(C-)

posList = []
negList = []
posMeans = []
negMeans = []
posStdDev = []
negStdDev = []
tp = 0  # True Positive
fp = 0  # False Positive
tn = 0  # True Negative
fn = 0  # False Negative


def listFromIndex(index, list):
    output = []
    for item in list:
        output.append(item[index])
    return output


def pdfDistribution(mean, stdDev, input):
    stdDevSqr = numpy.power(stdDev, 2)
    denom = numpy.sqrt((2 * numpy.pi * stdDevSqr))
    exponNumer = numpy.power((input - mean), 2)
    exponDenom = 2 * stdDevSqr
    expon = numpy.exp(-(exponNumer / exponDenom))
    output = (1 / denom) * expon
    return output


def determineProbability(pClass, meanArr, stdDevArr, inputArr):
    output = []
    for i in range(d):
        output.append(pdfDistribution(meanArr[i], stdDevArr[i], inputArr[i]))
    return numpy.prod(output) * pClass


def predict(item):
    pClassPos = determineProbability(probPlus, posMeans, posStdDev, item)
    pClassNeg = determineProbability(probNeg, negMeans, negStdDev, item)
    if (pClassPos > pClassNeg):
        return 1
    return -1


for item in Xtrain:
    if item[d] == -1:
        negList.append(item)
    else:
        if item[d] == 1:
            posList.append(item)

probPlus = len(posList) / n
probNeg = len(negList) / n

# This assigns a mean/std dev for each class, in an array in the same order as each individual entry
for i in range(d):
    posIndexList = listFromIndex(i, posList)
    negIndexList = listFromIndex(i, negList)
    posMeans.append(numpy.mean(posIndexList))
    posStdDev.append(numpy.std(posIndexList))
    negMeans.append(numpy.mean(negIndexList))
    negStdDev.append(numpy.std(negIndexList))

# Testing .....
Xtest = numpy.loadtxt(testingFile)
nn = Xtest.shape[0]  # Number of points in the testing data.

for item in Xtest:
    actual = item[d]
    predicted = predict(item)
    if predicted == 1 and actual == 1:
        tp += 1
    if predicted == 1 and actual == -1:
        fp += 1
    if predicted == -1 and actual == 1:
        fn += 1
    if predicted == -1 and actual == -1:
        tn += 1

# Iterate over all points in testing data
# For each point find the P(C+|Xi) and P(C-|Xi) and decide if the point belongs to C+ or C-..
# Recall we need to calculate P(Xi|C+)*P(C+) ..
# P(Xi|C+) = P(Xi1|C+) * P(Xi2|C+)....P(Xid|C+)....Do the same for P(Xi|C-)
# Now that you've calculate P(Xi|C+) and P(Xi|C-), we can decide which is higher
# P(Xi|C-)*P(C-) or P(Xi|C-)*P(C-) ..
# increment TP,FP,FN,TN accordingly, remember the true lable for the ith point is in Xtest[i,d]


# Calculate all the measures required..


print("False Positive:")
print(fp)
print("True Positive:")
print(tp)
print("True Negative:")
print(tn)
print("False Negative:")
print(fn)

totalTrue = tp + tn
precision = (tp / (tp + fp)) * 100
recall = (tp / (tp + fn)) * 100
classificationAccuracy = (totalTrue / nn) * 100
print("Accuracy:")
print(classificationAccuracy)
print("Precision:")
print(precision)
print("Recall:")
print(recall)
