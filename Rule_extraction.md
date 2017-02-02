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
