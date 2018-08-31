#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A pure Python drop-in replacement for the vorbiscomment command line tool based on mutagen
"""

from setuptools import find_packages, setup

install_requires = ['mutagen']

setup(
    name='pyvorbiscomment',
    version='0.1.0',
    url='https://github.com/SpotlightKid/pyvorbiscomment',
    license='MIT',
    author='Christopher Arndt',
    author_email='info@chrisarndt.de',
    description=__doc__.splitlines()[0],
    long_description="".join(__doc__.splitlines()[2:]),
    py_modules=['pyvorbiscomment'],
    zip_safe=False,
    platforms='any',
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'pyvorbiscomment = pyvorbiscomment:main',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Sound/Audio :: Editors',
    ]
)
