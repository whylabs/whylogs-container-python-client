wheel = whylogs_container_client-1.0.0-py3-none-any.whl

.PHONY: all install test

all:$(wheel)

$(wheel):
	python setup.py bdist_wheel


install:
	pip install -r requirements.txt


test:
	pip install -r test-requirements.txt
	python setup.py test 

