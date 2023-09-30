.PHONY: clean data lint requirements sync_data_to_s3 sync_data_from_s3

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROJECT_NAME = {{ cookiecutter.repo_name }}

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Set up python interpreter environment using Poetry
create_venv:
	@echo "Creating .venv..."
	${PYTHON_INTERPRETER} -m venv .venv
	poetry config virtualenvs.in-project true --local

## Install Python Dependencies
install_dependencies: 
	@echo "Installing dependencies..."
	poetry install

## Lint using ruff
lint:
	@echo "Lint code..."
	ruff check ${PROJECT_NAME}
	nbqa ruff cashout/notebooks

## Check typing using mypy
check_typing:
	@echo "Check typing..."
	mypy ${PROJECT_NAME}

## Check missing docstring using interrogate
check_missing_docstring:
	@echo "Check missing docstring..."
	interrogate -vv ${PROJECT_NAME}/src

## Clean notebooks using nb-clean
clean_notebooks:
	@echo "Clean notebook outputs, metadata etc..."
	nb-clean clean cashout/notebooks

## Update & run pre-commit
pre-commit:
	@echo "Update & run pre-commit..."
	pre-commit autoupdate
	git add .pre-commit-config.yaml
	pre-commit run

## Start data versionning
test:
	@echo "Start data versionning..."
	dvc init

## Execute tests
test:
	@echo "Test code..."
	pytest ${PROJECT_NAME}/tests/ --hypothesis-show-statistics

## Generate documentation using MkDocs
doc:
	@echo "Make symbolic link to library for easy documentation building..."
	cd docs; ln -sfn ../${PROJECT_NAME}/ ${PROJECT_NAME}
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
