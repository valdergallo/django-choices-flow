# Make content for developer

setup:
	pip install -r example/requirements.txt

test:
	python example/manage.py test django_choices_flow -v2

coverage:
	python example/manage.py test django_choices_flow -v2 --with-coverage

send_package:
	python setup.py register sdist bdist upload

clean:
	find . -name '*.pyc' -delete
	rm -rf django_choices_flow.egg-info
	rm -rf dist
