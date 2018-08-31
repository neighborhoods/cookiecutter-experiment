{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

# Running Experiments in a Docker Image

## Viewing experiment in a Docker container:

### Step 1: Download data

Download the required datasets and models using the make rules: 

```
make sync_data_from_s3
make sync_models_from_s3

# OR

make data
make models
```

### Step 2: Set base image VERSION variable

Ensure that the version number of the base image is set as an environment variable in the project's Makefile:

```
IMAGE_VERSION = {{ cookiecutter.base_image_version }}
```

Substitute "{{ cookiecutter.base_image_version }}" with the appropriate version number (e.g. "0.0.0").

### Step 3: Build the extended image

Build this project's image with the make rule:

```
make create_docker
```

### Step 4: Use the extended image

Run the docker container using the following make rule:

```
make run_docker
```

Alternatively, run the docker container and automatically start an accessible Jupyter session in Chrome via:

```
make start_jupyter
```

# Adding Reports to Data Science Documentation Site

Refer to the instructions in the [data-science-documentation repo](https://github.com/neighborhoods/data-science-documentation).

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
