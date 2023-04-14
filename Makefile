#################################################################################
#
# Makefile to build the project
#
#################################################################################

PROJECT_NAME = python-katas
REGION = eu-west-2
PYTHON_INTERPRETER = python
WD=$(shell pwd)
PYTHONPATH=${WD}
SHELL := /bin/bash
PROFILE = default
PIP:=pip

## Create python interpreter environment.
create-environment:
	@echo ">>> About to create environment: $(PROJECT_NAME)..."
	@echo ">>> checking python3 version"
	( \
		$(PYTHON_INTERPRETER) --version; \
	)
	@echo ">>> Setting up VirtualEnv."
	( \
	    $(PIP) install -q virtualenv virtualenvwrapper; \
	    virtualenv venv --python=$(PYTHON_INTERPRETER); \
	)


################################################################################################################
# Set Up

## Install pytest
pytest:
	$(PIP) install pytest

## Run a single test
unit-test:
	PYTHONPATH=${PYTHONPATH} pytest -v ${test_run}

## Run all the unit tests
unit-tests:
	PYTHONPATH=${PYTHONPATH} pytest -v

## Run all checks
run-checks: unit-tests