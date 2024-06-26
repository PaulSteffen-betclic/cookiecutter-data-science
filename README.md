# Cookiecutter Data Science

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._


#### [Project homepage](http://drivendata.github.io/cookiecutter-data-science/)


### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:
------------

    cookiecutter https://github.com/PaulSteffen-betclic/cookiecutter-data-science


[![asciicast](https://asciinema.org/a/244658.svg)](https://asciinema.org/a/244658)


### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── Makefile               <- Makefile with commands like `make data` or `make tests`.
├── README.md              <- The top-level README for developers using this project.
├── data       
│   ├── input
│   │   ├── raw            <- The original, immutable data dump.
│   │   └── processed      <- The final, canonical data sets for modeling.
│   │                  
│   └── output             <- The original, immutable data dump.
│      
├── docs                   <- A default mkdocstrings project
│      
├── models                 <- Trained and serialized models
│      
├── notebooks              <- Jupyter notebooks. Naming convention is a number (for ordering),
│                             the creator's initials, and a short `-` delimited description, e.g.
│                             `1.0-jqp-initial-data-exploration`.
│      
├── reports                <- Generated analysis as HTML, PDF, LaTeX, etc...
│   └── figures            <- Generated graphics and figures to be used in reporting.
|
├── resources       
│   └── sql_queries       <- Used .sql file queries
│      
├── pyproject.toml         <- This file contains build system requirements and information, 
│                             which are used by pip to build the package.
│
├── {{ cookiecutter.package_name }}
│   └── src                <- Source code for use in this project.
│       ├── __init__.py    <- Makes src a Python module.
│       │
│       ├── data           <- Scripts to download or generate data and turn raw data into 
│       │   │                 features for modeling.
│       │   ├── get_data.py
│       │   └── preprocess.py
│       │
│       └── models         <- Scripts to train models and then use trained models to make
│          │                 predictions.
│          ├── predict.py
│          └── train.py
│       
└── tox.ini                <- tox file with settings for running tox; see tox.readthedocs.io
```

## Contributing

We welcome contributions! [See the docs for guidelines](https://drivendata.github.io/cookiecutter-data-science/#contributing).

### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests
