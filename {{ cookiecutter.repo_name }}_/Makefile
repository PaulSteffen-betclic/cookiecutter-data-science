.PHONY: create_venv add_dev_dependencies add_codequality_dependencies add_test_dependencies add_doc_dependencies \
	add_venv_to_kernels install_dependencies lint check_typing check_missing_docstring clean_notebooks pre-commit test doc

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PACKAGE_NAME = {{ cookiecutter.package_name }}
PYTHON_VERSION = {{ cookiecutter.python_version }}

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Set up python interpreter environment using Poetry
create_venv:
	( \
    pyenv install ${PYTHON_VERSION}; \
    pyenv local ${PYTHON_VERSION}; \
    poetry env use ${PYTHON_VERSION}; \
    poetry shell; \
    )

## Add dev dependencies
add_dev_dependencies:
	poetry add jupyter ipykernel --group dev

## Add codequality dependencies
add_codequality_dependencies:
	poetry add ruff interrogate pre-commit "black[jupyter]" nbqa nox mypy --group codequality

## Add test dependencies
add_test_dependencies:
	poetry add pytest --group test

## Add test dependencies
add_doc_dependencies:
	poetry add "mkdocstrings[python]" mkdocs-jupyter pymdown-extensions mkdocs-section-index mkdocs-literate-nav mkdocs-material mkdocs-gen-files --group doc

## Install Python Dependencies
install_dependencies: 
	poetry install

## Add venv to jupyter kernels
add_venv_to_kernels:
	python -m ipykernel install --user --name=${PACKAGE_NAME}

## Lint using ruff
lint:
	@echo "Lint code..."
	ruff check ${PACKAGE_NAME}
	nbqa ruff notebooks

## Check typing using mypy
check_typing:
	mypy ${PACKAGE_NAME}

## Check missing docstring using interrogate
check_missing_docstring:
	interrogate -vv ${PACKAGE_NAME}/src

## Clean notebooks using nb-clean
clean_notebooks:
	nb-clean clean notebooks

## Update & run pre-commit
pre-commit:
	@echo "Update & run pre-commit..."
	pre-commit autoupdate
	git add .pre-commit-config.yaml
	pre-commit run

## Execute tests
test:
	@echo "Test code..."
	pytest ${PACKAGE_NAME}/tests/ --hypothesis-show-statistics

## Generate documentation using MkDocs
doc:
	@echo "Make symbolic link to library for easy documentation building..."
	cd docs; ln -sfn ../${PACKAGE_NAME}/ ${PACKAGE_NAME}
	@echo "Generate documentation..."
	mkdocs serve

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
.PHONY: help
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
