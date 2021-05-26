# INGOT-DR

**INGOT-DR** ( **IN**terpretable **G**r**O**up **T**esting for **D**rug **R**esistance) is an interpretable rule-based
predictive model base on **Group Testing** and **Boolean Compressed Sesing**. For more details and citation please see
the [paper](#paper).

## Install
INGOT-DR can be installed from [PyPI](https://pypi.org/project/ingotdr/). 
```python
pip install ingotdr
```
## Train and evaluate an INGOT-DR classifier

Sample data in the following example is available [here](https://github.com/hoomanzabeti/INGOT_DR_project/tree/master/data).
```python
from sklearn.model_selection import train_test_split
from sklearn.metrics import balanced_accuracy_score
import pandas as pd
import ingot

feature_matrix = 'SNPsMatrix_ciprofloxacin.csv'
label_vector =  'ciprofloxacinLabel.csv'

X = pd.read_csv(feature_matrix, index_col=0)
y = pd.read_csv(label_vector, index_col=0).to_numpy().ravel()

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33, test_size=0.2, stratify=y)

clf = ingot.INGOTClassifier(lambda_p=10, lambda_n=0.01, false_positive_rate_upper_bound=0.1, max_rule_size=20, solver_name='CPLEX_PY')
clf.fit(X_train,y_train)

y_pred = clf.predict(X_test)

print("Balanced accuracy: {}".format(balanced_accuracy_score(y_test, y_pred)))

print("Features in the learned rule: {}".format(clf.learned_rule()))
```
## Arguments

```python
ingot.INGOTClassifier( w_weight=1, lambda_p=1, lambda_z=1, lambda_e=1, false_positive_rate_upper_bound=None,
                       false_negative_rate_upper_bound=None, max_rule_size=None, rounding_threshold=1e-5,
                       lp_relaxation=False, only_slack_lp_relaxation=False, lp_rounding_threshold=0,
                       is_it_noiseless=False, solver_name='PULP_CBC_CMD', solver_options=None)
```


|Name|Type|Description|Default|
|:---:|:---:|:---:|:---:|
|w_weight|vector, float|A vector, float to provide prior weight to <img src="https://render.githubusercontent.com/render/math?math=w"> | 1.0 |
|lambda_p| float| Regularization coefficient for positive labels|1.0|
|lambda_z| float| Regularization coefficient for negative/zero labels|1.0|
|lambda_e| float| Regularization coefficient for all slack variables|1.0|
|false_positive_rate_upper_bound| float| False positive rate (FPR) upper bound| None|
|false_negative_rate_upper_bound| float| False negative rate(FNR) upper bound| None|
|max_rule_size| int | Maximum rule size| None |
rounding_threshold (float): Threshold for ilp solutions for Rounding to 0 and 1. Default to 1e-5
lp_relaxation (bool): A flag to use the lp relaxed version. Default to False.
only_slack_lp_relaxation (bool): A flag to only use the lp relaxed slack variables. Default to False.
lp_rounding_threshold (float): Threshold for lp solutions for Rounding to 0 and 1. Default to 0.
Range from 0 to 1.
is_it_noiseless (bool): A flag to specify whether the problem is noisy or noiseless. Default to True.
solver_name (str): Solver's name provided by Pulp. Default to 'PULP_CBC_CMD'.
solver_options (dic): Solver's options provided by Pulp. Default to None.
## Solver 
INGOT-DR supports a variety of solvers through the [PuLP](https://pypi.org/project/PuLP/) application programming interface (API). 
Solvers such as [GLPK](http://www.gnu.org/software/glpk/glpk.html),
[COIN-OR CLP/CBC](https://github.com/coin-or/Cbc),
[CPLEX](http://www.cplex.com/),
[GUROBI](http://www.gurobi.com/),
[MOSEK](https://www.mosek.com/),
[XPRESS](https://www.fico.com/es/products/fico-xpress-solver),
[CHOCO](https://choco-solver.org/),
[MIPCL](http://mipcl-cpp.appspot.com/),
[SCIP](https://www.scipopt.org/).

List of available solvers on your machine:
```python
import pulp as pl
solver_list = pl.listSolvers(onlyAvailable=True)
```

Name and properties of the solver can be specified via ```solver_name``` and 
```solver_options```. e.g:
```python
clf = ingot.INGOTClassifier(solver_name='CPLEX_PY', solver_options={timeLimit: 1800})
```
In the [INGOT-DR](#paper) paper, ```'CPLEX_PY'``` is the main solver. IBM CPLEX for academic use is available
[here](https://www.ibm.com/academic/technology/data-science). 
## Paper:

[INGOT-DR: an interpretable classifier forpredicting drug resistance in M. tuberculosis](https://www.biorxiv.org/content/10.1101/2020.05.31.115741v2.full).
([bibtex](https://scholar.googleusercontent.com/scholar.bib?q=info:bQ6FP1AQpvkJ:scholar.google.com/&output=citation&scisdr=CgXpW1OOEIO721E6sjI:AAGBfm0AAAAAYKw_qjKcmF8c1XZV57JWSMoDkwpaXPr8&scisig=AAGBfm0AAAAAYKw_qrApE1nCy1ns_BxQVZG_vrbY2Ot3&scisf=4&ct=citation&cd=-1&hl=en))
