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
	python setup.py check --strict --metadata --restructuredtext
	pylint --reports=no setup.py cid

release: clean
	fullrelease

test:
	py.test tests
