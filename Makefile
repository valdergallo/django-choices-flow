# Make content for developer

setup:
	pip install -r example/requirements.txt

test:
	python example/manage.py test -v 2

clean:
	find . -name '*.pyc' -delete
