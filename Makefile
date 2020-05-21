default: | help

develop: ## install with develop
	pip install --force-reinstall -e .[dev]
	python setup.py develop

format: ## auto format
	autoflake --in-place --remove-all-unused-imports --remove-unused-variables --recursive flask_boilerplate && \
		isort -rc flask_boilerplate && \
		black --line-length 119 flask_boilerplate

test: ## run all test
	pytest flask_boilerplate/tests

help:  ## Show all of tasks
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
