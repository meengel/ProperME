# ProperME
Small package for implementing Python classes with dependent attributes/methods!
That is, if you have attributes which rely on others and should be re-computed if these were changed, for example, this package is your tool of choice to never do the management by yourself again!

Please note that it relies on getters and setters which could be considered less pythonic.
But in that case, it is the best solution.
Further, do not mix the standard property-decorator and the properme one as to untested behavior (if you find a way of how to combine these properly, let us know!).
It is highly recommended to implement classes having only acyclic dependency graphs (even without using ProperME).

## Installation
You only need numpy and dill (a very useful package for pickling as a side note) to use the package.

## Usage
Simply write down which other getting-methods you used for each getter and relax!
That depending-dictionary is necessary for initializing a class attribute which is used for decorating tha class methods afterwards.
The dependency graph, i.e. which attributes affect others, is computed automatically then - even across multiple levels of dependency.

The attributes given or set by the respective methods have to be labelled starting with an underscore, e.g. "_radius".
Further, the getters and setters have to be labelled accordingly, e.g. "get_radius" or "set_radius".

Please have a look at [TEST_ProperME.py]() which gives a small example of how to use ProperME properly.

## Future
It is planned to implement an automatic parsing for the dependent getters and setters.

## Citation
If you use this software in any way, please reference the repository and the following people in the given order:
Michael Engel

Please note that there is NO warranty or anything similar for what you do with it!