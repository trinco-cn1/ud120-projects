#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import train_test_split
labels_train, labels_test, features_train, features_test = train_test_split(labels, features, test_size=0.3, random_state=42)

clf = DecisionTreeClassifier()
clf.fit(features, labels)
print 'POI true positive:', sum(labels * clf.predict(features))

clf.fit(features_train, labels_train)
print clf.score(features_test, labels_test)
pred = clf.predict(features_test)
print sum([item for item in pred if item == 1])
print 'POI true positive:', sum(labels_test * pred)

from sklearn.metrics import accuracy_score
import numpy
preds_0 = numpy.linspace(0, 0, len(features_test))
print accuracy_score(labels_test, preds_0)

from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
print 'precision score:', precision_score(labels_test, pred)
print 'recall score:', recall_score(labels_test, pred)

predx = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
realx = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

print precision_score(realx, predx)