## TREPAN
TREPAN, for extracting comprehensible, symbolic representations from trained neural networks. TREPAN queries a given network to induce a decision tree that describes the concept represented by the network.

![Image](https://github.com/2021rahul/Pattern-Mining-Rule-Extraction/blob/master/img/Screen%20Shot%202017-02-08%20at%209.31.33%20PM.png)

### The Oracle
The role of the oracle is to determine the class (as predicted by the network) of each instance that is presented as a query. Queries to the oracle do not have to be complete instances, but instead can specify constraints on the values that the features can take. In the latter case, the oracle generates a complete instance by randomly selecting values for each feature, while ensuring that the constraints are satisfied. In order to generate these random values, TREPAN uses the training data to model each feature's marginal distribution using a kernel density estimation method (Silverman, 1986) to model continuous features. The oracle is used for three different purposes: 

- to determine the class labels for the network's training examples
- to select splits for each of the tree's internal nodes
- to determine if a node covers instances of only one class. 

### Tree Expansion
TREPAN grows trees using a best-first expansion i.e. the one at which there is the greatest potential to increase the fidelity of the extracted tree to the network is considered the best node. The function used to evaluate node n is 

**f(n) = reach(n) x (1 - fidelity(n))** 

where reach(n) is the estimated fraction of instances that reach n when passed through the tree and fidelity(n) is the estimated fidelity of the tree to the network for those instances.

### Split Types
The internal nodes in a decision tree are used to partition to separate instances of different classes. It forms trees that use m-of-n expressions i.e. a Boolean expression that is specified by an integer threshold, m, and a set of n Boolean conditions for its splits. An m-of-n expression is satisfied when at least m of its n conditions are satisfied.

### Split Selection
Split selection involves deciding how to partition the input space at a given internal node in the tree. A limitation of conventional tree-induction algorithms is that splits near the bottom of a tree are often poorly chosen due to decrease in the amount of training data used to select splits. In contrast, because TREPAN has an oracle available, it is able to use as many instances as desired to select each split. TREPAN chooses a split after considering at least Smin instances, where Smin is a parameter of the algorithm.

### Stopping Criteria
TREPAN uses two separate stopping criteria:

1. A given node becomes a leaf in the tree if, with high probability, the node covers only instances of a single class. To make this decision, TREPAN determines the proportion of examples, Pc, that fall into the most common class at a given node, and then calculates a confidence interval around this proportion. The oracle is queried for additional examples until prob(pc < 1 - e) < d, where e and d are parameters of the algorithm.

2. TREPAN also accepts a parameter that specifies a limit on the number of internal nodes in an extracted tree. This parameter can be used to control the comprehensibility of extracted trees, since in some domains, it may require very large trees to describe networks to a high level of fidelity.
