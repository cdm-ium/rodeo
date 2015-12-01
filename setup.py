from setuptools import find_packages, setup

project = "rodeo"
version = "0.1.0"

setup(
    name=project,
    version=version,
    description="Art Management Service",
    author="Dino Moraites",
    author_email='dino.moraites@globality.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    keywords='rodeo',
    install_requires=[
        'Flask>=0.10.1',
        'Flask-Admin>=1.3.0',
        'Flask-Cache>=0.13.1',
        'Flask-Migrate>=1.3.0',
        'Flask-SQLAlchemy>=2.0',
        'Flask-Script>=2.0.5',
        'Flask-Testing>=0.4.2',
        'Flask-UUID>=0.2',
        'pyparsing>=2.0.5',
        'PyYAML',
        'psycopg2>=2.6.1',
        'requests>=2.5.3',
        'sqlalchemy-utils>=0.31.0',
        'webargs>=0.11.0',
        'uwsgi>=2.0.10',
    ],
    extras_require={
        'aws': [
            'boto>=2.38.0',
        ],
    },
    setup_requires=[
        'nose>=1.3.6',
    ],
    dependency_links=[
    ],
    entry_points={
        'console_scripts': [
            'createall = rodeo.cmd:createall',
        ]
    },
    test_suite='tests',
    tests_require=[
        'coverage>=3.7.1',
        'mock>=1.0.1',
    ],
)
