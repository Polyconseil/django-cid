.PHONY: clean docs test

clean:
	rm -fr build/
	rm -fr dist/
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete
	find . -name '*~' -delete

docs:
	sphinx-build -W -n -b html docs ./build/sphinx/html

test:
	py.test tests
