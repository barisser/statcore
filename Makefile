clean:
	rm -rf build; rm -rf dist; rm -rf *.egg-info; rm -rf statcore/*.so;rm -rf statcore/*.c;rm -rf *.so

venv:
	virtualenv venv && . venv/bin/activate && pip install setup.py

build: clean
	python setup.py build_ext --inplace

test: venv
	python setup.py install && pytest -s -vvv --pdb tests

publish:
	rm -rf dist && python setup.py sdist bdist_wheel && \
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
