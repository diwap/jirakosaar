.PHONY: init pylint build publish clean
init:
	pip install pipenv --upgrade
	pip install --dev
pylint:
	pip install -r requirements.txt
	pipenv run pylint src/
build:
	python setup.py sdist bdist_wheel
publish:
	pip install 'twine>=3.2.0'
	python setup.py sdist bdist_wheel
	twine upload dist/*
	rm -fr build dist .egg jirakosaar.egg-info
clean:
	rm -rf build dist .egg jirakosaar.egg-info
