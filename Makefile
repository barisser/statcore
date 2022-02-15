venv:
	virtualenv venv && . venv/bin/activate && pip install setup.py

test: venv
	python setup.py install && pytest -s --cov statcore --pdb tests

publish:
	rm -rf dist && python setup.py sdist bdist_wheel && \
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
