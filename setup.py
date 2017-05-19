#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


requirements = [
    'Flask>=0.12',
    'flask-cors>=3.0.2'
]

test_requirements = [
    'pytest',
    'pytest-flask',
]


setup(
    name='TouristFriend',
    version='v0.2.0',
    description="Query Google Places, Yelp and Foursquare",
    long_description="Query Google Places, Yelp and Foursquare simultaneously with ratings bayesian estimates",
    author="Gustavo Rodríguez",
    author_email='gustavrod@gmail.com',
    url='https://github.com/octohedron/TouristFriend',
    packages=find_packages(),
    include_package_data=False,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='TouristFriend',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    extras_require={
        'test': test_requirements
    },
    setup_requires=['pytest_runner']
)
