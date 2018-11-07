from setuptools import setup, find_packages

try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

import setuptools

install_reqs = parse_requirements('requirements.txt', session='hack')
reqs = [str(ir.req) for ir in install_reqs]

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='gitstatic',
    version='0.0.1',
    author='Timothy',
    author_email='ygmpkk@gmail.com',
    description='Git pages for hosting repository',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ygmpkk/git-static',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=reqs,
    python_requires='>=2.7',
)
