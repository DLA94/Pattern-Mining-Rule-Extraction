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

![Image](https://github.com/2021rahul/Pattern-Mining-Rule-Extraction/blob/master/img/rule_extraction_decision_tree.png)

## Rule Extraction from Random Forest: The RF+HC Methods
Random forest (RF) is a tree-based learning method, which exhibits a high ability to generalize on real data sets. Nevertheless, a possible limitation of RF is that it generates a forest consisting of many trees and rules, thus it is viewed as a black box model. In this paper, the RF+HC methods for rule extraction from RF are proposed. Once the RF is built, a hill climbing algorithm is used to search for a rule set such that it reduces the number of rules dramatically, which significantly improves comprehensibility of the underlying model built by RF. The experimental results show that the proposed methods outperform one of the state-of-the-art methods in terms of scalability and comprehensibility while preserving the same level of accuracy.

See [link](https://www.researchgate.net/publication/272742180_Rule_Extraction_from_Random_Forest_the_RFHC_Methods) for the complete paper.

## Rule extraction from Support Vector Machines
 The Support Vector Machine(SVM) is a state-of-the-art classification technique that generally provides accurate models, as it is able to capture non-linearities in the data. However, this strength is also its main weakness, as the generated non-linear models are typically regarded as incomprehensible black-box models. By extracting rules that mimic the black box as closely as possible, we can provide some insight into the logics of the SVM model.

-[Rule extraction from support vector machines](https://pdfs.semanticscholar.org/1a12/9126a237c69cf110132f2742b55d82dae38f.pdf)

In this work, a procedure for rule extraction from support vector machines is proposed: the SVM+Prototypes method. Once determined the decision function by means of a SVM, a clustering algorithm is used to determine prototype vectors for each class. These points are combined with the support vectors using geometric methods to define ellipsoids in the input space, which are later transfers to if-then rules. 

-[Rule Extraction from Support Vector Machines: An Overview of Issues and Application in Credit Scoring](https://www.google.co.in/url?sa=t&rct=j&q=&esrc=s&source=web&cd=4&cad=rja&uact=8&ved=0ahUKEwibytHBi_PRAhVIurwKHcgHCyIQFggxMAM&url=http%3A%2F%2Fwww.springer.com%2Fcda%2Fcontent%2Fdocument%2Fcda_downloaddocument%2F9783540753896-c1.pdf%3FSGWID%3D0-0-45-470107-p173762623&usg=AFQjCNEsMgeIjrMOrcbznfxv8VdkuMj6lA&bvm=bv.146094739,d.dGc)

This chapter provides an overview of recently proposed SVM rule extraction techniques, complemented with the pedagogical Artificial Neural Network (ANN) rule extraction techniques which are also suitable for SVMs. These issues are explained and further illustrated with a credit scoring case, where we extract a Trepan tree and a RIPPER rule set from the generated SVM model.

[Re-RX](https://www.researchgate.net/publication/221598955_Risk_Management_and_Regulatory_Compliance_A_Data_Mining_Framework_Based_on_Neural_Network_Rule_Extraction) is a recursive algorithm that has been developed to generate such rules from a neural network classifier [53]. Being pedagogical in its approach, it can be easily applied for rule extraction from SVM
