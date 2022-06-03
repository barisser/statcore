clean:
	rm -rf build; rm -rf dist; rm -rf *.egg-info; rm -rf statcore/*.so;rm -rf statcore/*.c;rm -rf *.so

venv:
	virtualenv venv && . venv/bin/activate && pip setup.py develop

build: clean
	python setup.py build_ext --inplace

test: venv
	python setup.py develop && pytest -s -vvv --pdb tests --cov statcore

publish:
	rm -rf dist && python setup.py sdist bdist_wheel && \
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
