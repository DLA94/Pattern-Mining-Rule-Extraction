## Rule Extraction from Artificial Neural Network
[Using Rule Extraction to Improve the Comprehensibility of Predictive Models](https://poseidon01.ssrn.com/delivery.php?ID=963020092123085102015083126070016073033078047010022006094074113002102117011026113007006058039044111113028119004087124067013008071094078049013109122072093107071065055095089121099096127104073012122126103117086101098027093001090079126113030015090126&EXT=pdf)

The taxonomy contains three main criteria for evaluation of algorithms: 

- the scope of use ( regression or classification)
- the type of dependency on the blackbox (independent versus dependent)
- the format of the extracted description () 

A rule extraction algorithm **Predictive** when the extracted rules allow the analyst to make a prediction for each possible observation
from the input space. More specifically, every possible input observation should be covered by exactly one rule, which means that the extracted rules should be both exclusive and exhaustive. By having both exclusive and exhaustive rules, the order in which the rules are processed is of no importance. For classification problems, exhaustivity is often realized by creating only rules for the minority class and adding an additional rule that specifies a default class when the input observation was not covered by any of the other rules.

**Descriptive** algorithm rules are either notexhaustive or not-exclusive. Non-exhaustivity might provide problems as there will be input observations for which none of the rules fires and no forecast can be delivered. Non-exclusivity might also provide problems because observations can be covered by multiple rules when non-exclusive rules are present.

Some algorithms-

1. [VIA-algorithm](https://papers.nips.cc/paper/924-extracting-rules-from-artificial-neural-networks-with-distributed-representations.pdf): It is an approach for the extraction of if-then rules from artificial neural networks. It creates rules by propagating intervals through the network. VIA can not be applied to other models than neural networks.[Dependent,Classification,Descdriptive]

2. Decision Trees: [CART, C4.5, TREPAN](http://papers.nips.cc/paper/1152-extracting-tree-structured-representations-of-trained-networks.pdf)extracts comprehensible, symbolic representations from trained neural networks. The algorithm uses queries to induce a decision tree that approximates the concept represented by a given network. The algorithm is general in its applicability and scales well to large networks and problems with high-dimensional input spaces.[Independent,Classification,Predictive]

3. [LEARNING ACCURATE AND UNDERSTANDABLE RULES FROM SVM CLASSIFIERS](https://pdfs.semanticscholar.org/ec7c/0ff68dbe73ed2ff1944b53070b223a371c25.pdf) a set of If-Then rules that are generally considered to be understandable and that allow an explicit control of their complexity to meet user-supplied requirements.

4. [REFNE](https://pdfs.semanticscholar.org/609c/f16352322905e6716ca1b1f41e06dec1dbae.pdf)

5. Rule Learners: [CN2](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.23.736&rep=rep1&type=pdf) designed for the efficient induction of simple, comprehensible production rules in domains where problems of poor description language and/or noise may be present.[Independent] 

6. [ANN-DT](http://ieeexplore.ieee.org/document/809084/) ) algorithm is describedby its authors as ‘an algorithm that extracts binary decision trees from a trained neural network’

7. [DecText](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.16.6788&rep=rep1&type=pdf) a new splitting techniques for extracting classical Decision Trees from trained Neural Networks. It was designed specifically for the extraction of a classification decision tree from a neural network and to obtain this goal several different splitting criteria were proposed.
