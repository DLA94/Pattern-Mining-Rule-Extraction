# -*- coding: utf-8 -*-

from sklearn.datasets import load_iris
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import KFold
from sklearn import tree
import numpy as np

iris = load_iris()
X, y = iris.data, iris.target
features = iris.feature_names
classes = iris.target_names
crossvalidation = KFold(n=X.shape[0], n_folds=5,shuffle=True, random_state=1)
for depth in range(1,10):
	tree_classifier = tree.DecisionTreeClassifier(max_depth=depth, random_state=0)
	if tree_classifier.fit(X,y).tree_.max_depth < depth:
		break
	score = np.mean(cross_val_score(tree_classifier,X,y,scoring='accuracy',cv=crossvalidation,n_jobs=1))
	print('Depth: %i Accuracy: %.3f' % (depth,score))
	outfile = 'tree_' + str(depth) + '.dot'
	tree.export_graphviz(tree_classifier, out_file=outfile, feature_names=features,class_names=classes,filled=True,rounded=True,special_characters=True)

from sklearn.ensemble import RandomForestClassifier
rf_classifier = RandomForestClassifier(max_depth=4)
rf_classifier.fit(X,y)
score = np.mean(cross_val_score(rf_classifier,X,y,scoring='accuracy',cv=crossvalidation,n_jobs=1))
print('Depth: 4 Accuracy: %.3f' % (score))
i_tree = 0
for tree_in_forest in rf_classifier.estimators_:
	print ("here")
	outfile = 'rftree_' + str(i_tree) + '.dot'
	tree.export_graphviz(tree_in_forest, out_file=outfile, feature_names=features,class_names=classes,filled=True,rounded=True,special_characters=True)
	i_tree = i_tree + 1


import os
cwd = os.getcwd()
listfile=[]
for file in os.listdir(cwd):
    if file.endswith(".dot"):
    	listfile.append(file)