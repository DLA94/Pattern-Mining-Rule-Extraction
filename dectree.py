# -*- coding: utf-8 -*-

from sklearn.datasets import load_iris
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import KFold
from sklearn import tree
import numpy as np

iris = load_iris()
X, y = iris.data, iris.target
features = iris.feature_names
crossvalidation = KFold(n=X.shape[0], n_folds=5,shuffle=True, random_state=1)
for depth in range(1,10):
	tree_classifier = tree.DecisionTreeClassifier(max_depth=depth, random_state=0)
	if tree_classifier.fit(X,y).tree_.max_depth < depth:
		break
	score = np.mean(cross_val_score(tree_classifier,X,y,scoring='accuracy',cv=crossvalidation,n_jobs=1))
	print('Depth: %i Accuracy: %.3f' % (depth,score))
	outfile = 'tree_' + str(depth) + '.dot'
	tree.export_graphviz(tree_classifier,out_file=outfile)