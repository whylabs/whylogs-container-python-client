wheel = whylogs_container_client-1.0.0-py3-none-any.whl

.PHONY: all install test clean

all:$(wheel)

$(wheel):
	pip install wheel
	python setup.py bdist_wheel --universal

install:
	pip install -r requirements.txt

test:
	pip install -r test-requirements.txt
	python setup.py test 

clean:
	rm -rf build dist whylogs_container_client.egg-info
