.PHONY: clean
clean:
	rm -fr build/
	rm -fr dist/
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete
	find . -name '*~' -delete

.PHONY: docs
docs:
	sphinx-build -W -n -b html docs ./build/sphinx/html

.PHONY: quality
quality:
	check-manifest
	isort --check-only --diff src tests
	pylint --reports=no setup.py src tests
	check-branches
	check-fixmes
	python setup.py sdist >/dev/null 2>&1 && twine check dist/*

.PHONY: clean
release: clean
	fullrelease

.PHONY: test
test:
	pytest

.PHONY: coverage
coverage:
	pytest --cov cid

.PHONY: coverage-html
coverage-html:
	pytest --cov cid --cov-report html
	python -c "import webbrowser; webbrowser.open('htmlcov/index.html')"
