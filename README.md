# Neighborhoods.com Cookiecutter Data Science

Neighborhoods.com's fork of Cookiecutter Data Science to standardize experimental workflows.

#### [Cookiecutter homepage](http://drivendata.github.io/cookiecutter-data-science/)

### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

### To start a new project, run:
------------

    cookiecutter https://github.com/neighborhoods/cookiecutter-experiment

### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
├── Dockerfile         <- Dockerfile for building experimental container.
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── logs               <- Logs from run experiments.
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │                     predictions
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│
├── create_notebook_config.py <- script for creating Jupyter notebook configuration.
└── tox.ini            <- tox file with settings for running tox; see tox.testrun.org
```

### Useful Make rules
------------

The Makefile is self-documenting, so simply typing `make` will provide the user with a list of
available Make rules. Some of the more useful are listed here.

* `sync_data_from_s3`: sync local copy of data with the version on the congifured S3 bucket.
* `sync_data_to_s3`: sync the version of the data on the congifured S3 bucket with the local copy.
* `create_docker`: Build the experiment's Docker image.
* `run_docker`: Run a Docker container of the experiment's image in interactive mode.
* `start_jupyter`: Start Jupyter Notebook running in a Docker container.

### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests
