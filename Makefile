# Make content for developer

setup:
	pip install -r requirements.txt

test:
	pytest django_choices_flow

coverage:
	pytest django_choices_flow --cov=django_choices_flow

send_package:
	python setup.py register sdist upload

clean:
	find . -name '*.pyc' -delete
	ptyhon setup.py clean --all
	rm -rf django_choices_flow.egg-info
	rm -rf dist
