MODULES=releaseme

all: pep8 flakes test

test:: clear_coverage run_integration_tests run_acceptance_tests

unit_test:: run_unit_tests

acceptance_test:: run_acceptance_tests

analysis:: pep8 flakes

pep8:
	@echo Checking PEP8 style...
	@pep8 --statistics ${MODULES} tests

flakes:
	@echo Searching for static errors...
	@pyflakes ${MODULES}

coveralls::
	coveralls

publish: run_publish run_tag

run_publish::
	@python setup.py sdist --formats zip,gztar upload

run_tag::
	python -m releaseme --git --file releaseme/__init__.py

run_unit_tests:
	@echo Running Tests...
	@py.test -v -l --cov releaseme tests/unit

run_integration_tests:
	@echo Running Tests...
	@py.test -v -l --cov releaseme tests/unit tests/integration

run_acceptance_tests:
	@echo Running Tests...
	@py.test -v -l tests/acceptance

clear_coverage:
	@echo Cleaning previous coverage...
	@coverage erase