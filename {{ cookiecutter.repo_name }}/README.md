{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization
------------

```
├── Makefile           <- Makefile with commands like `make data` or `make tests`.
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocstrings project
│
├── models             <- Trained and serialized models
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc...
│   └── figures        <- Generated graphics and figures to be used in reporting.
│
├── pyproject.toml     <- This file contains build system requirements and information, 
│                         which are used by pip to build the package.
│
├── {{ cookiecutter.package_name }}
│   ├── src                <- Source code for use in this project.
│   │   ├── __init__.py    <- Makes src a Python module.
│   │   │
│   │   ├── data           <- Scripts to download or generate data and turn raw data into 
│   │   │   │                 features for modeling.
│   │   │   ├── get_data.py
│   │   │   └── preprocess.py
│   │   │
│   │   ├── models         <- Scripts to train models and then use trained models to make
│   │   │   │                 predictions.
│   │   │   ├── predict.py
│   │   │   └── train.py
│   │   │
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
