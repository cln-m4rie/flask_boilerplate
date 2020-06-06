from setuptools import setup, find_packages

requirements = [
    'flask>=1.1.2',
    'environs',
    'jsonschema',
    'flask_cors',
]

develop_requirements = [
    'coverage',
    'autopep8',
    'flake8',
    'mypy',
    'autoflake',
    'isort',
    'black',
    'pytest',
]

uwsgi_requirements = [
    'uwsgi',
]

extras_require = {
    'dev': develop_requirements,
    'uwsgi': uwsgi_requirements,
}

setup(
    name='flask_boilerplate',
    version='0.1.0',
    description='Flask Boilerplate for me',
    author='cln-m4rie',
    author_email='',
    url='https://github.com/cln-m4rie/flask_boilerplate',
    install_requires=requirements,
    extras_require=extras_require,
    packages=find_packages(exclude=[])
)
