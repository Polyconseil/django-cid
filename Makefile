.PHONY: clean docs test

clean:
	rm -fr build/
	rm -fr dist/
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete
	find . -name '*~' -delete

docs:
	sphinx-build -W -n -b html docs ./build/sphinx/html

quality:
	check-manifest
	isort --check-only --diff cid tests
	pylint --reports=no setup.py cid tests
	check-branches
	check-fixmes
	python setup.py sdist >/dev/null 2>&1 && twine check dist/*

release: clean
	fullrelease

test:
	py.test tests
