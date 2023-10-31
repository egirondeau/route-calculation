install:
	pip install -e .

build:
	pip install -r requirements.txt
	python -m pip install --upgrade build
	python -m build

upload:
	twine upload --repository pypi dist/*
