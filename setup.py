#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from aldryn_disqus import __version__


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Communications',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
]

setup(
    name='aldryn-disqus',
    version=__version__,
    description='Allows embeding Disqus threads into the site',
    author='Divio AG',
    author_email='info@divio.ch',
    url='https://github.com/aldryn/aldryn-disqus',
    packages=['aldryn_disqus'],
    license='LICENSE.txt',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    include_package_data=True,
    zip_safe=False
)
