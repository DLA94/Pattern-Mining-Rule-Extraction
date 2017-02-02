# Rule Extraction from different Architectures

## Rule Extraction from a Decision Tree
- Rules are easier to understand than large trees
- One rule is created for each path from the root to a leaf
- Each attribute-value pair along a path forms a conjunction: the leaf holds the class prediction
- Rules are mutually exclusive and exhaustive
- Example: Rule extraction from our buys_computer decision-tree
  - IF age = young AND student = no THEN buys_computer = no
  - IF age = young AND student = yes THEN buys_computer = yes
  - IF age = mid-age THEN buys_computer = yes
  - IF age = old AND credit_rating = excellent THEN buys_computer = no
  - IF age = old AND credit_rating = fair THEN buys_computer = yes

See [this](http://slidewiki.org/slide/24191) for more details.

## Rule Extraction from Random Forest: The RF+HC Methods
Random forest (RF) is a tree-based learning method, which exhibits a high ability to generalize on real data sets. Nevertheless, a possible limitation of RF is that it generates a forest consisting of many trees and rules, thus it is viewed as a black box model. In this paper, the RF+HC methods for rule extraction from RF are proposed. Once the RF is built, a hill climbing algorithm is used to search for a rule set such that it reduces the number of rules dramatically, which significantly improves comprehensibility of the underlying model built by RF. The experimental results show that the proposed methods outperform one of the state-of-the-art methods in terms of scalability and comprehensibility while preserving the same level of accuracy.

See [link](https://www.researchgate.net/publication/272742180_Rule_Extraction_from_Random_Forest_the_RFHC_Methods) for the complete paper.

## Rule extraction from support vector machines

## rule extraction from neural network
